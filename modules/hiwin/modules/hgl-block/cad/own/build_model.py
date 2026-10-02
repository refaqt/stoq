"""Our own HGL15CA low square block, drawn from the catalogue only.

Every dimension comes from the linear guideways catalogue GW-13-1-EN-2606-K,
table 3.7 on page 41 (block), table 3.9 on page 43 (rail) and table 3.13 on
page 47 (E2 unit). The brand's CAD file was not used. Rebuild headless:

    "C:\Program Files\FreeCAD 1.1\bin\freecadcmd.exe" build_model.py

Axes, the same as our rail model: the block runs along +Y from 0 to L, Z is up
with the rail bottom at 0, and it is centred on the rail (X = 0). The grease
nipple end is at Y = 0. The four M4 holes are centred on the length.

What is left out, because the catalogue does not size it: chamfers, the end
caps and seals as separate parts, the grease nipple, the lubrication ports, and
the ball grooves. The rail channel is the rail's WR x HR envelope.
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
    ("T_E2", "=Lss_E2 - L_blk", "Length one E2 unit adds (page 47)"),
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
    sheet.set(f"A{row + 1}", "Source: linear guideways catalogue GW-13-1-EN-2606-K, pages 41, 43 "
              "and 47. Change values in params.csv and rebuild.")
    return sheet


def _box(shape, name, length_x, width_y, height_z, x, y, z, subtract=False):
    kind = "PartDesign::SubtractiveBox" if subtract else "PartDesign::AdditiveBox"
    box = shape.newObject(kind, name)
    box.setExpression("Length", length_x)
    box.setExpression("Width", width_y)
    box.setExpression("Height", height_z)
    box.setExpression(".Placement.Base.x", x)
    box.setExpression(".Placement.Base.y", y)
    box.setExpression(".Placement.Base.z", z)
    return box


def build(doc, params):
    _clear(doc)
    _params_sheet(doc, params)
    doc.recompute()
    shape = body(doc)
    features = []

    features.append(_box(
        shape, "Block", "Params.W_blk", "Params.L_blk", "Params.H_inst - Params.H1_gap",
        "-Params.W_blk / 2", "0", "Params.H1_gap"))
    if int(params.get("E2_units", 0)) >= 1:
        features.append(_box(
            shape, "E2Unit", "Params.W_E2", "Params.T_E2", "Params.H_E2",
            "-Params.W_E2 / 2", "-Params.T_E2", "Params.H1_gap"))
        channel_start, channel_length = "-Params.T_E2 - 1", "Params.Lss_E2 + 2"
    else:
        channel_start, channel_length = "-1", "Params.L_blk + 2"
    features.append(_box(
        shape, "RailChannel", "Params.WR", channel_length, "Params.HR",
        "-Params.WR / 2", channel_start, "0", subtract=True))

    for i, (sx, sy) in enumerate([(1, 1), (1, -1), (-1, 1), (-1, -1)], start=1):
        hole = shape.newObject("PartDesign::SubtractiveCylinder", f"Thread{i}")
        hole.setExpression("Radius", "Params.M_tap / 2")
        hole.setExpression("Height", "Params.l_thread")
        hole.setExpression(".Placement.Base.x", f"{'' if sx > 0 else '-'}Params.B_holes / 2")
        hole.setExpression(".Placement.Base.y",
                           f"Params.L_blk / 2 {'+' if sy > 0 else '-'} Params.C_holes / 2")
        hole.setExpression(".Placement.Base.z", "Params.H_inst - Params.l_thread")
        features.append(hole)

    shape.Tip = features[-1]
    for feature in features[:-1]:
        feature.Visibility = False
    features[-1].Visibility = True


# FreeCADCmd 1.1 runs a script under its file name, not "__main__".
if __name__ in ("__main__", "build_model"):
    run(build, cad_dir=_HERE)
