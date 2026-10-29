"""Our own ISO 8734 parallel pin, 2 mm (m6) x 28 mm, type A, hardened steel.

A standard part has no brand model, so this model is ours. The sizes are the
ones in the ISO 8734 designation of the part, ISO 8734 - 2 x 28 - A - St (see
`2X28-A.params.csv`). Change a value there and rebuild headless from the
library root:

    FreeCADCmd modules/iso/modules/iso-8734/cad/own/2X28-A.build.py

The pin is a plain cylinder. The chamfer at one end and the rounded other end
are inside that shape and are not modelled.

Axes: Z along the pin axis. The origin is the centre of the pin, so the pin
runs from Z = -l / 2 to Z = +l / 2.
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
    "Z along the pin axis; origin at the centre of the pin, which runs from "
    "Z = -l / 2 to Z = +l / 2."
)

DERIVED = [
    ("pin_r", "=pin_d / 2", "Radius of the pin"),
    ("z_start", "=-pin_l / 2", "Position of the first end face on the axis"),
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
    sheet.set(f"A{row + 1}", "Source: ISO 8734, designation ISO 8734 - 2 x 28 - A - St. "
              "Change values in 2X28-A.params.csv and rebuild.")
    return sheet


def build(doc, params):
    _clear(doc)
    _params_sheet(doc, params)
    doc.recompute()

    pin = body(doc, "Pin")
    shank = pin.newObject("PartDesign::AdditiveCylinder", "Shank")
    bind(shank, "Radius", "Params.pin_r")
    bind(shank, "Height", "Params.pin_l")
    bind(shank, ".Placement.Base.z", "Params.z_start")

    # Joints attach to this frame. It sits on the axis, in the middle of the
    # pin, with Z along the axis.
    frame(doc, "IF_centre", x="0", y="0", z="0")


# Keep this line as it is. FreeCADCmd 1.1 sets __name__ to the file name,
# so a test on "__main__" would skip the build without a word.
main(build, globals(), cad_dir=_HERE)
