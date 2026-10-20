"""Our own ALZ absolute scale, drawn from the datasheet only.

LAMOTION publishes no CAD file of the scale on its own. Its only file of the
scale is a short piece under a read head, so this model is ours. Every size
comes from the ABS read head datasheet V1.44 (BiSS-C), pages 4, 9 and 14.
Change `Length` in `ALZ00270G.params.csv`, then rebuild headless from the
library root:

    "C:\\Program Files\\FreeCAD 1.1\\bin\\freecadcmd.exe" modules/lamotion/modules/alz-scale/cad/own/ALZ00270G.build.py

The scale is a steel tape on a narrower adhesive backing. The 50 um code track
on the tape is not modelled.

Axes: the scale runs along +X from 0 to Length, Y is up with the bottom of the
adhesive (the surface it is stuck to) at Y = 0, and the scale is centred on
Z = 0. These are the axes of the LAMOTION head-and-scale model, so the read
head sits on this scale without turning it.
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

#: The axes and origin of this model. They are the same as in the brand's
#: head-and-scale model, so the read head fits on ours.
AXES = (
    "X along the scale, from 0 to Length; Y up, bottom of the adhesive at Y = 0; "
    "Z across, scale centred on Z = 0. The same as the LAMOTION head-and-scale model."
)

DERIVED = [
    ("H_top", "=adh_t + scale_t", "Height of the top of the scale above the surface it is stuck to"),
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
    sheet.set(f"A{row + 1}", "Source: LAMOTION ABS read head datasheet V1.44 (BiSS-C), pages 4, 9 and 14. "
              "Change values in ALZ00270G.params.csv and rebuild.")
    return sheet


def build(doc, params):
    _clear(doc)
    _params_sheet(doc, params)
    doc.recompute()

    adhesive = body(doc, "Adhesive")
    backing = adhesive.newObject("PartDesign::AdditiveBox", "Backing")
    backing.setExpression("Length", "Params.Length")    # X, along the scale
    backing.setExpression("Width", "Params.adh_t")         # Y, up
    backing.setExpression("Height", "Params.adh_w")        # Z, across
    backing.setExpression(".Placement.Base.z", "-Params.adh_w / 2")

    scale = body(doc, "Scale")
    tape = scale.newObject("PartDesign::AdditiveBox", "Tape")
    tape.setExpression("Length", "Params.Length")
    tape.setExpression("Width", "Params.scale_t")
    tape.setExpression("Height", "Params.scale_w")
    tape.setExpression(".Placement.Base.y", "Params.adh_t")
    tape.setExpression(".Placement.Base.z", "-Params.scale_w / 2")

    # Joints attach to these frames. On both, X runs along the scale and Z
    # points up, away from the surface the scale is stuck to.
    frame(doc, "IF_mount_bottom", x="0", y="0", z="0",
          angle="Params.frame_up", axis=(1, 0, 0))
    frame(doc, "IF_head", x="0", y="Params.H_top", z="0",
          angle="Params.frame_up", axis=(1, 0, 0))


# Keep this line as it is. FreeCADCmd 1.1 sets __name__ to the file name,
# so a test on "__main__" would skip the build without a word.
main(build, globals(), cad_dir=_HERE)
