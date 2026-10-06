# ADR-004 — Share brand CAD files and documents until the brand objects

- **Date:** 2026-10-06
- **Status:** Proposed. Niels Bosmans approves it in the pull request.
- **Replaces:** the HIWIN part of [ADR-003](2026-10-02_hiwin-stop-sharing.md)
- **Changes:** [ADR-002](2026-09-29_component-intake.md), which asked for a
  written yes before sharing

## Context

ADR-003 stopped sharing the HIWIN files, because the HIWIN terms do not allow
it. Our own models of the HIWIN rail and block replaced them. Those models
are simple. Machine designs that use them look basic and unprofessional next
to designs with the brand's own models.

Most brands share their CAD files and documents freely on their websites. A
design that shows their product is free publicity for them. We expect few
brands to object.

## Decision

- We share brand CAD files and documents in STOQ, until the brand asks us to
  stop. This is Niels Bosmans's decision. It is not a reading of the terms.
- HIWIN files come back to STOQ: the catalogue, the three STEP files and the
  two FreeCAD documents built from them. They are the same files as before
  2026-10-02, with the same checksums.
- A new `public` decision with `basis = "none"` is recorded for both kinds of
  HIWIN file. The old entries stay, because entries are never edited.
- MAXWELL files stay in STOQ. Their decision was already `public` with
  `basis = "none"`, so nothing changes for MAXWELL.
- `stoq-private` stays. It keeps our own copy of every file and the saved
  terms. If a brand objects, its files move there again, as ADR-003 did for
  HIWIN.
- Files that came under a confidentiality agreement (NDA) are never shared
  this way.
- The method in [`docs/adding-components.md`](../adding-components.md) gets a
  Route D for this.

## Consequences

Machine designs can use the real brand models, and look professional.

The HIWIN terms still say no. Clause 2.4 of the HIWIN sales terms says
drawings and documents "may not be made accessible to third parties". HIWIN
could ask us to remove the files. A file in the history stays there, because
history here is never rewritten. The check shows a warning for each brand
with `basis = "none"`, so this risk stays visible.

The rule in the mistake note of 2026-10-02 ("never record a `public` decision
without a quoted clause that allows sharing") no longer applies to brand
files. Saving a dated copy of the terms still applies.

Our own HIWIN models stay in `cad/own/`. They are the fallback if HIWIN
objects, and the rail model also works for lengths we have no HIWIN file for.

If a brand objects: add an `internal` entry, move the files to
`stoq-private`, and point the machines at our own models. ADR-003 shows how.

This page is not legal advice. A lawyer who knows EU intellectual property law
should check this approach if a brand objects or if the stakes grow.
