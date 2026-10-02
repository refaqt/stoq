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

A separate step compared each dimension with the HIWIN files. The rail passes
all 9 checks. The block passes 6 of 12. The other 6 could not be confirmed:
the HIWIN block file has no rail to measure the heights from, and no separate
E2 lubrication unit. Nothing failed.

## Why it matters

Machines that use this library get models we are allowed to share. The rail
model works for any length, so a new machine does not need a new download.

## Next Steps

- Point the AQTUATOR X axis at the new models in `cad/own/`.
- Confirm the E2 unit length with HIWIN. The catalogue gives 75.4 mm for the
  block with one E2 unit; the HIWIN file shows no separate unit.
- Optional: ask HIWIN for written permission to share the files.

## Related

- [ADR-003](../decisions/2026-10-02_hiwin-stop-sharing.md)
- [Mistake note](../mistakes/2026-10-02_hiwin-shared-without-saved-terms.md)
