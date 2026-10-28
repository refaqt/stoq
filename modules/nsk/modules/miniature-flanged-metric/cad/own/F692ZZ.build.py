"""Our own NSK F692ZZ flanged ball bearing, drawn from the NSK table only.

NSK gives the CAD file only through a log-in, so this model is ours. Every
size comes from the NSK table "Extra Small Ball Bearings and Miniature Ball
Bearings, Metric Series With Flange" on the NSK website (see
`F692ZZ.params.csv`). Change a value there and rebuild headless from the
library root:

    FreeCADCmd modules/nsk/modules/miniature-flanged-metric/cad/own/F692ZZ.build.py

The bearing is one solid: the bore, the outside diameter, the width and the
flange on the outer ring. The balls, the shields and the edge chamfers are
inside that shape and are not modelled.

Axes: Z along the bearing axis. The face on the flange side is at Z = 0, and
the bearing runs from there to Z = +B (width_b). The origin is on the axis.
"""

import sys
from pathlib import Path

try:
    _HERE = Path(__file__).resolve().parent
except NameError:  # exec()'d from the FreeCAD console
    _HERE = Path.cwd()


def _doqs_scripts(start):
    for base in [start, *start.parents]:
        candidate = base / "doqs" / "scripts"
        if (candidate / "cad_build.py").is_file():
            return candidate
    raise RuntimeError(f"doqs/scripts/cad_build.py not found above {start}")


sys.path.insert(0, str(_doqs_scripts(_HERE)))

from cad_build import bind, body, frame, main  # noqa: E402

#: The axes and origin of this model.
AXES = (
    "Z along the bearing axis, from the face on the flange side (Z = 0) to "
    "the other face (Z = +width_b); origin on the axis, in the flange-side face."
)

DERIVED = [
    ("r_bore", "=bore_d / 2", "Radius of the bore"),
    ("r_out", "=outer_d / 2", "Outside radius of the outer ring"),
    ("r_flange", "=flange_d1 / 2", "Outside radius of the flange"),
    ("flip", "=180", "Frame turn, in degrees around X: frame Z points out of the flange side"),
]


def _clear(doc):
    """The .FCStd is generated output: rebuild it from nothing every time."""
    while doc.Objects:
        top = [o for o in doc.Objects if not o.InList] or doc.Objects
        for obj in top:
            if hasattr(obj, "removeObjectsFromDocument"):
                obj.removeObjectsFromDocument()
            if obj.isValid() and doc.getObject(obj.Name):
                doc.removeObject(obj.Name)


def _params_sheet(doc, params):
    sheet = doc.addObject("Spreadsheet::Sheet", "Params")
    sheet.set("A1", "alias")
    sheet.set("B1", "value")
    sheet.set("C1", "note")
    row = 2
    for alias, value in params.items():
        sheet.set(f"A{row}", alias)
        sheet.set(f"B{row}", str(value))
        sheet.setAlias(f"B{row}", alias)
        row += 1
    for alias, expr, note in DERIVED:
        sheet.set(f"A{row}", alias)
        sheet.set(f"B{row}", expr)
        sheet.set(f"C{row}", note)
        sheet.setAlias(f"B{row}", alias)
        row += 1
    sheet.set(f"A{row + 1}", "Source: NSK table, metric miniature ball bearings with flange. "
              "Change values in F692ZZ.params.csv and rebuild.")
    return sheet


def build(doc, params):
    _clear(doc)
    _params_sheet(doc, params)
    doc.recompute()

    bearing = body(doc, "Bearing")
    ring = bearing.newObject("PartDesign::AdditiveCylinder", "OuterRing")
    bind(ring, "Radius", "Params.r_out")
    bind(ring, "Height", "Params.width_b")
    flange = bearing.newObject("PartDesign::AdditiveCylinder", "Flange")
    bind(flange, "Radius", "Params.r_flange")
    bind(flange, "Height", "Params.flange_c1")
    bore = bearing.newObject("PartDesign::SubtractiveCylinder", "Bore")
    bind(bore, "Radius", "Params.r_bore")
    bind(bore, "Height", "Params.width_b")

    # Joints attach to these frames. Their Z axes point out of the bearing on
    # the flange side. IF_flange_face sits on the face of both rings on the
    # flange side, where a washer or a shoulder touches the inner ring.
    # IF_seat sits on the inner face of the flange, where the flange rests on
    # the end of a housing.
    frame(doc, "IF_flange_face", x="0", y="0", z="0",
          angle="Params.flip", axis=(1, 0, 0))
    frame(doc, "IF_seat", x="0", y="0", z="Params.flange_c1",
          angle="Params.flip", axis=(1, 0, 0))


# Keep this line as it is. FreeCADCmd 1.1 sets __name__ to the file name,
# so a test on "__main__" would skip the build without a word.
main(build, globals(), cad_dir=_HERE)
