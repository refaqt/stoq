"""Our own HGR15R profile rail, drawn from the catalogue only.

Every dimension comes from the linear guideways catalogue GW-13-1-EN-2606-K:
table 3.9 on page 43 and formula F 3.2 on page 44. The brand's CAD file was
not used. Change `Length` in `params.csv`, then rebuild headless:

    "C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe" build_model.py

The number of holes follows the length: as many as fit with at least E_min at
each end, and the same end distance at both ends (catalogue notes 2 and 3).

Axes: the rail runs along +Y from 0 to Length, Z is up with the rail bottom at
0, and the rail is centred on X = 0. The catalogue does not size the side
grooves, so the cross-section is the WR x HR envelope.
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

from cad_build import body, run  # noqa: E402

DERIVED = [
    ("n_holes", "=floor((Length - 2 * E_min) / Pitch) + 1",
     "n: number of holes (catalogue page 43 note 2, page 44 F 3.2)"),
    ("E_end", "=(Length - (n_holes - 1) * Pitch) / 2",
     "E1 = E2: end distance, the same at both ends (page 43 note 3)"),
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
    sheet.set(f"A{row + 1}", "Source: linear guideways catalogue GW-13-1-EN-2606-K, page 43 and 44. "
              "Change values in params.csv and rebuild.")
    return sheet


def build(doc, params):
    _clear(doc)
    _params_sheet(doc, params)
    doc.recompute()
    shape = body(doc)

    rail = shape.newObject("PartDesign::AdditiveBox", "Rail")
    rail.setExpression("Length", "Params.WR")       # X
    rail.setExpression("Width", "Params.Length")    # Y, along the rail
    rail.setExpression("Height", "Params.HR")       # Z
    rail.setExpression(".Placement.Base.x", "-Params.WR / 2")

    hole = shape.newObject("PartDesign::SubtractiveCylinder", "Hole")
    hole.setExpression("Radius", "Params.d_hole / 2")
    hole.setExpression("Height", "Params.HR")
    hole.setExpression(".Placement.Base.y", "Params.E_end")

    bore = shape.newObject("PartDesign::SubtractiveCylinder", "Counterbore")
    bore.setExpression("Radius", "Params.D_cb / 2")
    bore.setExpression("Height", "Params.h_cb")
    bore.setExpression(".Placement.Base.y", "Params.E_end")
    bore.setExpression(".Placement.Base.z", "Params.HR - Params.h_cb")
    doc.recompute()

    pattern = shape.newObject("PartDesign::LinearPattern", "HolePattern")
    pattern.Originals = [hole, bore]
    y_axis = [f for f in shape.Origin.OriginFeatures if f.Role == "Y_Axis"][0]
    pattern.Direction = (y_axis, [""])
    pattern.Mode = "Spacing"
    pattern.setExpression("Offset", "Params.Pitch")
    pattern.setExpression("Occurrences", "Params.n_holes")
    shape.Tip = pattern
    for feature in (rail, hole, bore):
        feature.Visibility = False
    pattern.Visibility = True


# FreeCADCmd 1.1 runs a script under its file name, not "__main__".
if __name__ in ("__main__", "build_model"):
    run(build, cad_dir=_HERE)
