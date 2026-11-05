"""Our own piece of neodymium magnet tape, 3 x 0.5 mm, cut to 21.5 mm.

The tape is sold without a brand name, so this model is ours. Width and
thickness come from the seller's product page; the length is the cut length
we chose for the magnet ring in the base of the aqtuator compact stage
(short piece, four in each end leg of the magnet ring, one on each piece
of solid floor between the damper slots, the corners and the split). All values are in `3X0.5X21.5.params.csv`. Change a value there and
rebuild from the library root, inside the FreeCAD window (see
docs/mistakes/2026-10-20_headless-models-open-hidden.md), or headless:

    FreeCADCmd modules/generic/modules/ndfeb-magnet-tape/cad/own/3X0.5X21.5.build.py

The piece is a plain bar. The adhesive layer is not drawn on its own: the
seller does not say whether the 0.5 mm includes it.

Axes: X along the length, from one cut end (X = 0) to the other. Y across the
width, from one edge (Y = 0) to the other. Z through the thickness, from the
adhesive face (Z = 0) to the free face. The origin is a corner of the
adhesive face.
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
    "X along the length from one cut end (X = 0); Y across the width from one "
    "edge (Y = 0); Z through the thickness from the adhesive face (Z = 0); "
    "origin at a corner of the adhesive face."
)


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
    row = 2
    for alias, value in params.items():
        sheet.set(f"A{row}", alias)
        sheet.set(f"B{row}", str(value))
        sheet.setAlias(f"B{row}", alias)
        row += 1
    sheet.set(f"A{row + 1}", "Source: seller's product page of the 3 x 0.5 mm "
              "tape; cut length chosen for the compact stage base. "
              "Change values in 3X0.5X21.5.params.csv and rebuild.")
    return sheet


def build(doc, params):
    _clear(doc)
    _params_sheet(doc, params)
    doc.recompute()

    tape = body(doc, "Tape")
    bar = tape.newObject("PartDesign::AdditiveBox", "Bar")
    bind(bar, "Length", "Params.tape_l")
    bind(bar, "Width", "Params.tape_w")
    bind(bar, "Height", "Params.tape_t")

    # Joints attach to this frame: a corner of the adhesive face, with Z
    # pointing into the tape. In the base, this face lies on the floor of
    # the ring pocket.
    frame(doc, "IF_end", x="0", y="0", z="0")


# Keep this line as it is. FreeCADCmd 1.1 sets __name__ to the file name,
# so a test on "__main__" would skip the build without a word.
main(build, globals(), cad_dir=_HERE)
