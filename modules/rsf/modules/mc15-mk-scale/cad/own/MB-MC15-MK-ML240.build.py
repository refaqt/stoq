"""Our own MC 15 MK scale, drawn from the RSF drawing only.

RSF publishes a STEP file of the MK scale only for a 100 mm measuring length,
so this 240 mm model is ours. Every size comes from the RSF drawing "MC15 MK
mating dimensions", D1158017-04 (one sheet). Change `ML` in
`MB-MC15-MK-ML240.params.csv`, then rebuild inside the FreeCAD window (see
docs/mistakes/2026-10-20_headless-models-open-hidden.md): start FreeCAD with
no document open and run this file from the Python console with

    exec(open(r"<library root>/modules/rsf/modules/mc15-mk-scale/cad/own/MB-MC15-MK-ML240.build.py").read(), {"__file__": r"<same path>"})

The scale is a steel tape on a narrower adhesive tape. The code track and the
graduation on the tape are not modelled.

Axes: the tape runs along +X from 0 to OL = ML + 20, Y is up with the bottom
of the adhesive (the surface it is stuck to) at Y = 0, and the tape is centred
on Z = 0. Ascending position values run along +X.
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

from cad_build import body, frame, main  # noqa: E402

#: The axes and origin of this model.
AXES = (
    "X along the tape, from 0 to OL = ML + 20, ascending positions along +X; "
    "Y up, bottom of the adhesive at Y = 0; Z across, tape centred on Z = 0."
)

DERIVED = [
    ("Length", "=ML + ol_extra", "Overall length OL of the tape"),
    ("x_ml_start", "=sensor_x - head_start", "Position sensor at the start of the measuring length"),
    ("x_ml_end", "=sensor_x - head_start + ML", "Position sensor at the end of the measuring length"),
    ("H_top", "=adh_t + scale_t", "Height of the top of the tape above the surface it is stuck to"),
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
    sheet.set(f"A{row + 1}", "Source: RSF drawing MC15 MK mating dimensions D1158017-04, sheet 1. "
              "Change values in MB-MC15-MK-ML240.params.csv and rebuild.")
    return sheet


def build(doc, params):
    _clear(doc)
    _params_sheet(doc, params)
    doc.recompute()

    adhesive = body(doc, "Adhesive")
    backing = adhesive.newObject("PartDesign::AdditiveBox", "AdhesiveTape")
    backing.setExpression("Length", "Params.Length")    # X, along the tape
    backing.setExpression("Width", "Params.adh_t")       # Y, up
    backing.setExpression("Height", "Params.adh_w")      # Z, across
    backing.setExpression(".Placement.Base.z", "-Params.adh_w / 2")

    scale = body(doc, "Scale")
    tape = scale.newObject("PartDesign::AdditiveBox", "SteelTape")
    tape.setExpression("Length", "Params.Length")
    tape.setExpression("Width", "Params.scale_t")
    tape.setExpression("Height", "Params.scale_w")
    tape.setExpression(".Placement.Base.y", "Params.adh_t")
    tape.setExpression(".Placement.Base.z", "-Params.scale_w / 2")

    # Joints attach to these frames. On all of them, X runs along the tape
    # (ascending positions) and Z points up, away from the surface the tape is
    # stuck to. IF_ml_start and IF_ml_end sit on the top of the tape, on its
    # centre line, where the position sensor of the scanning head is at the two
    # ends of the measuring length.
    frame(doc, "IF_mount_bottom", x="0", y="0", z="0",
          angle="Params.frame_up", axis=(1, 0, 0))
    frame(doc, "IF_ml_start", x="Params.x_ml_start", y="Params.H_top", z="0",
          angle="Params.frame_up", axis=(1, 0, 0))
    frame(doc, "IF_ml_end", x="Params.x_ml_end", y="Params.H_top", z="0",
          angle="Params.frame_up", axis=(1, 0, 0))


# Keep this line as it is. FreeCADCmd 1.1 sets __name__ to the file name,
# so a test on "__main__" would skip the build without a word.
main(build, globals(), cad_dir=_HERE)
