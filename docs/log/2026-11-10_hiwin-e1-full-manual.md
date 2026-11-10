# 2026-11-10 — The full HIWIN E1 drive manual is in the library

**Role(s):** electrical engineering, purchasing, legal

## What changed

The full user manual of the HIWIN E1 servo drive (663 pages, edition MD09UE01-2607 V3.3) is now in
the HIWIN folder of the library. HIWIN GmbH had sent only three pages of it by email. Those pages
are already in the library from the earlier pull request. They stay, because nothing is ever removed.

The row in `modules/hiwin/vendor-index.csv` has the public download address on the HIWIN Taiwan
site, the size, and the checksum.

## Why it matters

The three pages did not show which method finds the commutation angle with a BiSS-C encoder. The
full manual does. Section 7.5.2 and Table 7.5.2.1 list the method "STABS test/tune" for a linear
motor with a serial EnDat or BiSS-C signal, on the ESC-SS box. The answer is in the aqtuator log
`docs/log/2026-11-10_hiwin-answers-e1-drive-and-guides.md`.

## What you need to do

Read the legal note. Then review and merge. The file is not in the main branch until the pull
request is merged.

## Legal note

- The newest HIWIN decision for documents is `public`, with `basis = "none"`. That is Route D in
  [`docs/adding-components.md`](../adding-components.md). This file comes from the public download
  page of HIWIN Mikrosystem in Taiwan, not from HIWIN GmbH. The recorded terms are those of HIWIN
  GmbH. The Taiwan terms were not read.
- The private copy in `stoq-private` and the dated terms evidence are not part of this change.
  Someone with access to `stoq-private` must add them.
- `bash doqs.sh check` was not run in this session. The tooling folders are empty.

<details>
<summary>Notes for reviewers</summary>

- File: `modules/hiwin/docs/datasheets/hiwin-e1-servo-drive-user-manual-MD09UE01-2607-V3.3.pdf`,
  25,780,004 bytes.
- Source page: <https://www.hiwinmikro.tw/Downloads/ManualOverview_EN.htm>, "E1 Series Servo Drive
  User Manual". Downloaded on 2026-11-10.
- The three pages from the email belong to a different edition, ED1-01-5-EN-2610-MA (HIWIN GmbH,
  376 pages in total). Table numbers differ: Table 7.2 and 7.4 there are Table 7.4.2.1 and 7.5.1.1
  here.
- The E series Thunder software manual (MD12UE01-2605 V3.7, 435 pages) is also on that page. It is
  not added in this change.

</details>
