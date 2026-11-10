# 2026-11-10 — Two HIWIN documents are in the library

**Role(s):** mechanical engineering, purchasing, legal

## What changed

Two documents that HIWIN GmbH sent by email are now in the HIWIN folder of the library:

- The assembly instructions for linear guideways (GW-06-2-EN-2610-MA, 76 pages).
- Pages 128 to 130 of the E1 servo drive manual (ED1-01-5-EN-2610-MA). They show which encoder
  signals work with the electrical angle detection called "SW method 1".

Each file has a row in `modules/hiwin/vendor-index.csv`, with its checksum and size. The address
column is empty, because HIWIN sent the files by email and gave no download link.

## Why it matters

The assembly instructions say how to take a block off a rail and put it back, and how the
reference sides must face. The compact stage needs both. The manual pages are the only written
HIWIN answer on commutation with the E1 drive.

## What you need to do

Read the legal note below. Then review and merge. The files are not in the main branch until the
pull request is merged.

## Legal note

- The newest HIWIN decision for documents is `public`, with `basis = "none"`. That is Route D in
  [`docs/adding-components.md`](../adding-components.md). The files were not sent under a
  confidentiality agreement.
- The assembly instructions say: "Reprinting, even in part, is not permitted without our
  approval." The HIWIN terms say the same in clause 2.4. Sharing is our choice, until HIWIN
  objects.
- The private copy in `stoq-private` and the dated terms evidence are not part of this change.
  Someone with access to `stoq-private` must add them.
- `bash doqs.sh check` was not run. The tooling folders are empty in this session.

<details>
<summary>Notes for reviewers</summary>

- Branch: `claude/hiwin-answers-documents`.
- Files are in `modules/hiwin/docs/datasheets/`, next to the catalogue, so the existing licence
  file there applies.
- The 3-page PDF was attached to two emails (2026-11-10 12:29 and 12:49 UTC). Both copies are the
  same file. The retrieval time on each row is the email time of the file's first appearance for
  the manual pages, and of the only appearance for the assembly instructions.
- Source thread: "Offerteaanvraag – servodrive E2 Advanced en lineaire geleidingen EGR15U /
  QEH15SA", Harjot Singh, HIWIN GmbH.
- Answers from the thread are logged in refaqt/aqtuator:
  `docs/log/2026-11-10_hiwin-answers-e1-drive-and-guides.md`.

</details>
