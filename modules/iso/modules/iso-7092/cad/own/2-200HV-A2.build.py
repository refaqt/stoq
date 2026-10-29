"""Our own ISO 7092 plain washer, small series, size 2 (for M2), 200 HV, A2.

A standard part has no brand model, so this model is ours. The sizes come
from the Wuerth data sheet of this washer (see `2-200HV-A2.params.csv`).
Change a value there and rebuild headless from the library root:

    FreeCADCmd modules/iso/modules/iso-7092/cad/own/2-200HV-A2.build.py

The washer is a flat ring. Its edge burrs are not modelled.

Axes: Z along the washer axis. One face is at Z = 0, the other at Z = +h.
The origin is on the axis.
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
    "Z along the washer axis, from one face (Z = 0) to the other (Z = +h); "
    "origin on the axis, in the first face."
)

DERIVED = [
    ("r_in", "=washer_d1 / 2", "Radius of the hole"),
    ("r_out", "=washer_d2 / 2", "Outside radius"),
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
    sheet.set(f"A{row + 1}", "Source: ISO 7092, size 2, Wuerth data sheet. "
              "Change values in 2-200HV-A2.params.csv and rebuild.")
    return sheet


def build(doc, params):
    _clear(doc)
    _params_sheet(doc, params)
    doc.recompute()

    washer = body(doc, "Washer")
    disc = washer.newObject("PartDesign::AdditiveCylinder", "Disc")
    bind(disc, "Radius", "Params.r_out")
    bind(disc, "Height", "Params.washer_h")
    hole = washer.newObject("PartDesign::SubtractiveCylinder", "Hole")
    bind(hole, "Radius", "Params.r_in")
    bind(hole, "Height", "Params.washer_h")

    # Joints attach to this frame. It sits on the axis in the face at Z = 0,
    # with Z pointing into the washer.
    frame(doc, "IF_face", x="0", y="0", z="0")


# Keep this line as it is. FreeCADCmd 1.1 sets __name__ to the file name,
# so a test on "__main__" would skip the build without a word.
main(build, globals(), cad_dir=_HERE)
