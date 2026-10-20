"""Our own RUS-ET A-B end clamp pair, drawn from the datasheets only.

The two clamps hold the ends of an ALZ scale. LAMOTION publishes no CAD file
of them. The plan sizes come from the ABS read head datasheet V1.44 (BiSS-C),
page 10. The thickness comes from the RX2 grating rules V2.57, page 14, which
shows the same RUS-ET-A/B part. Rebuild headless from the library root:

    "C:\\Program Files\\FreeCAD 1.1\\bin\\freecadcmd.exe" modules/lamotion/modules/rus-et-clamp/cad/own/RUS-ET-A-B.build.py

Each clamp is a flat plate with rounded corners. The adhesive backing on its
underside has a notch, open at one end, where the end of the scale lies. Clamp
A and clamp B are mirror images. The brand name printed on the top is left out.

Axes: the same as the ALZ scale model. X runs along the scale, Y is up with the
surface the clamps are stuck to at Y = 0, and the clamps are centred on Z = 0.
The origin is the start of the scale: clamp A covers it, and clamp B covers
the other end at X = scale_len. So the pair fits a scale of that length when
the frame IF_scale_start is joined to the frame IF_mount_bottom of the scale.
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

from cad_build import body, frame, main, part  # noqa: E402

#: The axes and origin of this model: those of our ALZ scale model.
AXES = (
    "X along the scale, origin at the scale start; Y up, the surface the clamps are "
    "stuck to at Y = 0; Z across, clamps centred on Z = 0. The same as the ALZ scale model."
)

PN = "RUS-ET-A-B"

DERIVED = [
    ("overhang", "=clamp_l - notch_l", "Length of the clamp beyond the end of the scale"),
    ("frame_up", "=-90", "Frame turn, in degrees around X: frame Z points along part +Y (up)"),
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
    sheet.set(f"A{row + 1}", "Source: LAMOTION ABS read head datasheet V1.44 (BiSS-C) page 10, and "
              "RX2 grating rules V2.57 page 14. Change values in RUS-ET-A-B.params.csv and rebuild.")
    return sheet


def _vertical_edges(feature):
    """The four corner edges of a plate: the edges that run along Y."""
    names = []
    for i, edge in enumerate(feature.Shape.Edges, start=1):
        a, b = edge.Vertexes[0].Point, edge.Vertexes[-1].Point
        if abs(a.x - b.x) < 1e-6 and abs(a.z - b.z) < 1e-6 and abs(a.y - b.y) > 1e-6:
            names.append(f"Edge{i}")
    if len(names) != 4:
        raise RuntimeError(f"Expected 4 corner edges, found {len(names)}")
    return names


def _clamp(doc, label, start, notch_start):
    """One clamp. `start` and `notch_start` are X expressions."""
    shape = body(doc, label, container=part(doc, PN))
    plate = shape.newObject("PartDesign::AdditiveBox", f"{label}_plate")
    plate.setExpression("Length", "Params.clamp_l")    # X, along the scale
    plate.setExpression("Width", "Params.clamp_t")     # Y, up
    plate.setExpression("Height", "Params.clamp_w")    # Z, across
    plate.setExpression(".Placement.Base.x", start)
    plate.setExpression(".Placement.Base.z", "-Params.clamp_w / 2")
    doc.recompute()

    corners = shape.newObject("PartDesign::Fillet", f"{label}_corners")
    corners.Base = (plate, _vertical_edges(plate))
    corners.setExpression("Radius", "Params.corner_r")
    doc.recompute()

    notch = shape.newObject("PartDesign::SubtractiveBox", f"{label}_notch")
    notch.setExpression("Length", "Params.notch_l")
    notch.setExpression("Width", "Params.notch_d")
    notch.setExpression("Height", "Params.notch_w")
    notch.setExpression(".Placement.Base.x", notch_start)
    notch.setExpression(".Placement.Base.z", "-Params.notch_w / 2")
    shape.Tip = notch
    for feature in (plate, corners):
        feature.Visibility = False
    notch.Visibility = True
    return shape


def build(doc, params):
    _clear(doc)
    _params_sheet(doc, params)
    doc.recompute()
    part(doc, PN)

    # Clamp A: over the scale start. Its notch is open towards +X, where the
    # scale runs on.
    _clamp(doc, "Clamp_A", "-Params.overhang", "0")
    # Clamp B: the mirror image, over the scale end. Its notch is open
    # towards -X.
    _clamp(doc, "Clamp_B", "Params.scale_len - Params.notch_l",
           "Params.scale_len - Params.notch_l")

    # Joins IF_mount_bottom of the scale. X along the scale, Z up.
    frame(doc, "IF_scale_start", x="0", y="0", z="0",
          angle="Params.frame_up", axis=(1, 0, 0), container=part(doc, PN))


# Keep this line as it is. FreeCADCmd 1.1 sets __name__ to the file name,
# so a test on "__main__" would skip the build without a word.
main(build, globals(), cad_dir=_HERE)
