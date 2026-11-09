"""Our own model of a 20 mm stub of Festo tubing PUN-H-4X0,75-BL (197383).

The tubing is sold by the metre. An assembly shows only a short stub at each
fitting. All values are in `197383.params.csv`. Rebuild headless from
the library root with

    FreeCADCmd modules/festo/modules/pun-h/cad/own/197383.build.py

Axes: Z along the tubing, from one cut end (Z = 0). The origin is on the axis.
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
AXES = "Z along the tubing from one cut end (Z = 0); origin on the axis."

DERIVED = [('r_out', '=hose_od / 2', 'Outside radius'),
    ('r_in', '=hose_id / 2', 'Inside radius')]


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
    sheet.set(f"A{row + 1}", "Change values in 197383.params.csv and rebuild.")
    return sheet


def build(doc, params):
    _clear(doc)
    _params_sheet(doc, params)
    doc.recompute()

    hose = body(doc, "Hose")
    wall = hose.newObject("PartDesign::AdditiveCylinder", "Tube")
    bind(wall, "Radius", "Params.r_out")
    bind(wall, "Height", "Params.hose_l")
    bore = hose.newObject("PartDesign::SubtractiveCylinder", "Bore")
    bind(bore, "Radius", "Params.r_in")
    bind(bore, "Height", "Params.hose_l")

    # Joints attach to this frame: the axis on one cut end. Z runs along
    # the hose.
    frame(doc, "IF_end", x="0", y="0", z="0")


# Keep this line as it is. FreeCADCmd 1.1 sets __name__ to the file name,
# so a test on "__main__" would skip the build without a word.
main(build, globals(), cad_dir=_HERE)
