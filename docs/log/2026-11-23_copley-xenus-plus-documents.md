# 2026-11-23 — The Copley Xenus Plus documents and the XEL drive are in the library

**Role(s):** electrical engineering, purchasing, legal

## What changed

The library now has the brand Copley Controls, with three documents and one drive family:

- The CME User Guide (the setup and tuning software for all Copley drives), the Xenus Plus User
  Guide and the Xenus Plus XEL datasheet. They sit in `modules/copley/docs/datasheets/`, because
  they cover more than one family.
- The Xenus Plus XEL family, with three parts: XEL-230-18, XEL-230-36 and XEL-230-40. Each row
  holds the current, the supply, the loop rates, the encoder types and the mass from the datasheet.
  The family notes list the control loops, the filters, gain scheduling and the frequency analysis
  modes of CME, with the section of the manual for each.

Later the same day, all downloads of the Copley Xenus Plus Compact page were added too:

- A new family for the XEC (the drive Eltrex offered), with three parts: XEC-230-09, XEC-230-12 and
  XEC-230-15, and the Copley STEP model of the drive.
- The XEC and XPC datasheets, the Xenus Plus Compact user guide and STO manual, the EC Declaration
  of Conformity, the UL functional safety certificate, an MTBF report, a RoHS and REACH
  certificate, and the XEC and XPC drawings (PDF and DXF).
- Five firmware files are recorded with their address and checksum, but are not committed. They
  are software, and nothing allows us to share them. Our copy is in `stoq-private`.

The documents say they may not be copied without written permission from Copley. They are free
downloads from the Copley website. The proposal is to share them under ADR-004 (share until the
brand objects), as we did for the HIWIN E1 manual. Niels Bosmans approves this in the pull request.
Our own copy, and the dated copyright clause, are in `stoq-private`.

## Why it matters

We are choosing a servo drive for the AQTUATOR CS stage, and Copley is one of the two offers from
Eltrex. The manuals answer several questions from the call with Eltrex on 2026-11-23. The answers
are in the aqtuator log of the same day.

## What was not added

- No family for the XPC (the CANopen version). Its datasheet and drawing are in the brand folder.
- No price and no distributor. They belong in the purchasing database.

## Next Steps

- Niels Bosmans approves the two `public` decisions with `basis = "none"` (documents and CAD) in
  the pull request. The XEC drawing carries a "confidential" stamp, although Copley publishes it.
- The STEP model is 87 MB. It goes through Git LFS, and uses part of the free LFS storage.

<details>
<summary>Sources</summary>

- CME User Guide 16-01157 Rev 05 (July 2026), Xenus Plus User Guide 16-01344 Rev 08 (October
  2024), Xenus Plus XEL datasheet 16-01637 Rev 02. Checksums in `modules/copley/vendor-index.csv`.
- Copyright clause: CME User Guide section 1.2 and Xenus Plus User Guide "Copyrights".
- refaqt/aqtuator log `docs/log/2026-11-23_copley-cme-loops-filters-and-bode.md`.
- `bash doqs.sh generate` wrote the licence file of the documents folder and added the family to
  the usage graph. `bash doqs.sh check`: all gates passed.

</details>
