# 2026-10-06 — HIWIN files are shared again

**Role(s):** mechanical engineering, legal

## What changed

The HIWIN catalogue, the three HIWIN STEP files and the two FreeCAD documents
built from them are back in this library. They are the same files that were
here before 2026-10-02. The rail and block rows point at the HIWIN documents
again, so machine designs can use the real HIWIN models.

New rule: we share brand CAD files and documents until the brand objects.
See [ADR-004](../decisions/2026-10-06_share-supplier-files-until-asked.md).
The method for adding components has a new Route D for this.

MAXWELL did not change. Its files were never taken out.

Our own HIWIN rail and block models stay in `cad/own/` as a fallback. The
copies in `stoq-private` also stay.

## Why it matters

Our own models looked basic. Designs with the brand's real models look
professional, and the AQTUATOR X axis links to the HIWIN documents by path,
so those links work again on a fresh clone.

## Next Steps

- If HIWIN or MAXWELL objects, follow ADR-003 to stop sharing that brand.
- Optional: ask both brands for written permission, with the email in the
  method. A yes removes the warning in the check.

## Related

- [ADR-004](../decisions/2026-10-06_share-supplier-files-until-asked.md)
- [ADR-003](../decisions/2026-10-02_hiwin-stop-sharing.md)
