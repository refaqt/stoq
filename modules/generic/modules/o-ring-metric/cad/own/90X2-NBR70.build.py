"""Our own O-ring 90 x 2 mm, NBR 70.

A plain torus: inside diameter 90 mm, cross-section 2 mm. All values are in
`90X2-NBR70.params.csv`. Rebuild headless from the library root with

    FreeCADCmd modules/generic/modules/o-ring-metric/cad/own/90X2-NBR70.build.py

Axes: Z along the ring axis. The ring lies on the XY plane (Z = 0), the way it
lies on the bottom of its groove. The origin is the centre of the ring.
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
AXES = "Z along the ring axis; the ring lies on the XY plane (Z = 0); origin at the centre of the ring."

DERIVED = [('r_cs', '=oring_cs / 2', 'Radius of the cross-section'),
    ('r_mid', '=oring_id / 2 + oring_cs / 2', 'Radius of the centre line of the ring')]


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
    sheet.set(f"A{row + 1}", "Change values in 90X2-NBR70.params.csv and rebuild.")
    return sheet


def build(doc, params):
    _clear(doc)
    _params_sheet(doc, params)
    doc.recompute()

    ring = body(doc, "ORing")
    torus = ring.newObject("PartDesign::AdditiveTorus", "Ring")
    bind(torus, "Radius1", "Params.r_mid")
    bind(torus, "Radius2", "Params.r_cs")
    bind(torus, "Placement.Base.z", "Params.r_cs")

    # Joints attach to this frame: the centre of the ring, on the plane the
    # ring lies on (the bottom of its groove). Z points through the ring.
    frame(doc, "IF_seat", x="0", y="0", z="0")


# Keep this line as it is. FreeCADCmd 1.1 sets __name__ to the file name,
# so a test on "__main__" would skip the build without a word.
main(build, globals(), cad_dir=_HERE)
