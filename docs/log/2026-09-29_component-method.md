# 2026-09-29 — A fixed method for adding components

**Role(s):** documentation, legal

## What changed

Adding a part now follows one written method, for people and for agents. It
covers where each file goes, how the licence of each file is checked, who
approves the decision, and what to do when we may not share a file.

Work done:

- `docs/adding-components.md`: the method, a permission request email, and a
  purchase-contract clause for customer copies.
- An agent skill with hard rules. The most important rule: an agent never
  decides that a file may be public. A named person does.
- The HIWIN and MAXWELL decisions from 2026-09-21 are now recorded as licence
  reviews. MAXWELL shows as a warning, because nothing written allows sharing
  its files.
- The guides now describe `stoq-private` and the new command that copies its
  files into place.
- STOQ now uses the doqs version that checks all of this.

## Decisions

See [ADR-002](../decisions/2026-09-29_component-intake.md).

## Next Steps

- Save dated copies of the HIWIN and MAXWELL terms in `stoq-private`, and add
  reviews that name them.
- Decide what to do about MAXWELL: ask for written permission, or stop sharing.
- A FreeCAD script that fills in the pass or fail results of an own model's
  check list.

## Related

- [adding-components.md](../adding-components.md)
- [ADR-001](../decisions/2026-09-21_committing-supplier-cad.md)
