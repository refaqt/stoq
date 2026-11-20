# 2026-11-20 — The HIWIN E1 servo drive is in the library

**Role(s):** electrical engineering, purchasing

## What changed

The library now has a family for the HIWIN E1 servo drive, in `modules/hiwin/modules/e1-drive/`.
It has one part: the ED1F-EN-0422-01-00, the 400 W drive with EtherCAT for linear motors. The row
holds the figures that matter for choosing the drive, from the manual and from HIWIN's emails:

- Speed loop bandwidth 3.2 kHz and current loop bandwidth 5 kHz. HIWIN confirmed in writing that
  both are the maximum -3 dB bandwidth, not the update rate of the loop.
- The ESC-SS-S02 encoder box adds at most 31.25 µs delay to the position signal.
- The drive gives 10 A for 1 s.
- The update rate of the position loop is still not published.

## Why it matters

Before, these answers were only in an email and in the aqtuator logs. A developer who looks up a
part looks in the parts library. The full E1 manual was already here, but no part pointed to it.

## What was not added

- No family for the ESC-SS-S02 encoder box. The drive row names it, with its delay.
- No price and no delivery time. They belong in the purchasing database.

<details>
<summary>Sources</summary>

- E1 Series Servo Drive User Manual MD09UE01-2607 V3.3, in `modules/hiwin/docs/datasheets/`.
  Mass 1.1 kg from section 4.1.1.2.
- Emails from Harjot Singh (HIWIN GmbH), 2026-11-10 and 2026-11-20. In Dutch.
- refaqt/aqtuator logs `docs/log/2026-11-05_hiwin-ed1-checked-against-the-requirements.md`,
  `docs/log/2026-11-10_hiwin-answers-e1-drive-and-guides.md` and
  `docs/log/2026-11-20_hiwin-loop-bandwidth-answers.md`.
- `bash doqs.sh check`: all gates passed. `bash doqs.sh generate` added the family to the usage
  graph.

</details>
