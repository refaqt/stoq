# 2026-10-02 — HIWIN: stop sharing, and our own rail and block models

**Role(s):** mechanical engineering, purchasing, legal

## What changed

This library no longer shares the HIWIN catalogue or the HIWIN CAD files. The
HIWIN terms do not allow it. Our copies are in `stoq-private`, and the
catalogue row now points at the PDF on the HIWIN download page.

The HGR15 rail and the HGL15 block now have our own FreeCAD models, drawn
from the catalogue only. The rail model has one value for its length. The
number of holes and the end distances follow HIWIN's rule: as many holes as
fit with at least 6 mm at each end, and the same distance at both ends. A
418 mm rail gets 7 holes, 29 mm from each end.

The block now has every dimension the catalogue table gives, including the
reference edge band, the end caps, the grease nipple and the lubrication
ports. Shapes the figure shows without a size were estimated from the figure,
which is drawn for size 25.

A separate step compared each dimension with the HIWIN files. The rail passes
all 9 checks. The block passes 16 of 33: every table value except the nipple
length G. G and 12 of the 13 estimates did not match. They are marked not
confirmed until the real block is measured; the model has placeholders for
them. Before this, the block passed 9 of 12. The three E2 rows are not confirmed:
the catalogue shows an E2 lubrication unit on one end, but the HIWIN file for
this part number has none. So the E2 unit is a parameter in our model, off by
default, until HIWIN confirms which is right.

The first version of the models was wrong: the block had the E2 unit on one
end and both models used other axes than the HIWIN models. They were rebuilt
the same day from build scripts, with the HIWIN axes and a symmetric block.
See the [mistake note](../mistakes/2026-10-02_hiwin-own-models-not-checked.md).

## Why it matters

Machines that use this library get models we are allowed to share. The rail
model works for any length, so a new machine does not need a new download.

## Next Steps

- Point the AQTUATOR X axis at the new models in `cad/own/`.
- Measure the real HGL15CA block: the grease nipple, the plug on the far end
  face, the end seal screw heads, the chamfers, the end caps and the ports.
  Then replace the est_* values in cad/own/params.csv and rebuild.
- Ask HIWIN whether the HGL15CAZBC+E2 block has an E2 unit on one end, as the
  catalogue shows, or none, as their CAD file shows.
- Optional: ask HIWIN for written permission to share the files.

## Related

- [ADR-003](../decisions/2026-10-02_hiwin-stop-sharing.md)
- [Mistake note](../mistakes/2026-10-02_hiwin-shared-without-saved-terms.md)
