# 2026-11-20 — HIWIN answers on the QEH15 blocks are in the library

**Role(s):** mechanical engineering, purchasing

## What changed

The HIWIN answers about the QEH15 guide blocks are now written next to the block family, in
`modules/hiwin/modules/qeh-block/bom/parts.csv`. Before, they were only in an email and in an
aqtuator log entry. The answers are:

- HIWIN delivers the blocks without grease, or with its standard grease G05. HIWIN greases them only
  when rail and blocks are ordered as one set. The oil in the E2 lubrication unit was not named.
- Each block comes on a mounting aid. The aid works as a dummy rail, so the balls stay in the block.
- A block may come off the rail and go back. Accuracy, preload and lubrication stay if the
  reference sides of rail and block face the same way. The warranty stays.
- Preload ZA in accuracy class H is in stock. Class P takes longer.

## Why it matters

Whoever builds a stage reads the part family, not the email. The answers on grease and on taking a
block off the rail matter at assembly.

## What was not added

- No part row for the class H block QEH15SAZAH+E2. A row needs the HIWIN CAD file from the product
  configurator. Download it before the first order.
- No HIWIN drive. The library has the E1 manual but no drive family. The E1 is still a candidate
  in the aqtuator drive list. HIWIN's new answers on the drive are in the aqtuator log
  `docs/log/2026-11-20_hiwin-loop-bandwidth-answers.md`. (Corrected on 2026-11-20: an earlier
  version of this entry said the HIWIN drives were dropped. That was a misreading. HIWIN gave a
  speed loop bandwidth, not a loop rate.)
- Prices, stock and delivery times stay out of this library. They belong in the purchasing
  database.

<details>
<summary>Sources</summary>

- Email thread "Offerteaanvraag – servodrive E2 Advanced en lineaire geleidingen EGR15U /
  QEH15SA", Harjot Singh (HIWIN GmbH, application engineer), 2026-11-05 and 2026-11-10. In Dutch.
- `bash doqs.sh check`: all gates passed.

</details>
