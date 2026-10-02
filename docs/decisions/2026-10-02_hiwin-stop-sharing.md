# ADR-003 — Stop sharing the HIWIN files and use our own models

- **Date:** 2026-10-02
- **Status:** Proposed. Niels Bosmans approves it in the pull request.
- **Replaces:** the HIWIN part of [ADR-001](2026-09-21_committing-supplier-cad.md)

## Context

ADR-001 marked the HIWIN files as files we may share. Nobody saved or quoted
the terms at the time. On 2026-10-02 the terms were read and saved as dated
PDFs in `stoq-private/evidence/hiwin/`:

- The HIWIN sales terms, clause 2.4: HIWIN keeps the copyright in drawings
  and other documents, and "they may not be made accessible to third parties".
- The HIWIN website disclaimer: copying diagrams or texts into other
  publications needs the author's agreement.
- The linear guideways catalogue, last page: copying it, in full or in part,
  needs HIWIN's permission.
- The STEP files come from the HIWIN configurator, which needs a customer
  login. The files carry no licence text.

For both the CAD files and the documents, the answers are: publish no, give to
customers no, keep yes, make derived files no (not clearly allowed).

## Decision

- A new `internal` decision for both kinds of HIWIN file. The old entries stay,
  because entries are never edited.
- The catalogue, the three STEP files and the two FreeCAD documents built from
  them leave the current version of this library. They stay in the history
  before this date, because history is never rewritten. Our copies are in
  `stoq-private` at the same paths.
- The catalogue row becomes `fetch-only`, with the address of the PDF on the
  HIWIN download page. The STEP rows become `private`, because the
  configurator needs a login.
- The rail and the block get our own models, drawn from the catalogue only.
  The rail model takes its length from one value; the number of holes and the
  end distances follow HIWIN's rule for that length.

## Consequences

Anyone who clones this library gets models we may share, under our licence.
The models show the outer shape and the mounting holes, not the raceways or
the grease nipple.

The AQTUATOR machine repository links the two old FreeCAD documents by path.
Those links break on a fresh clone until the machine points at the new models
in `cad/own/`, or until someone copies the files from `stoq-private` with
`bash doqs.sh restore-private --from ../stoq-private`.

If HIWIN gives written permission later, a new `public` entry with
`basis = "permission"` can bring the files back.
