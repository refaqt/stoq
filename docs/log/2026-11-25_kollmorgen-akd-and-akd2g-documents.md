# 2026-11-25 — The Kollmorgen AKD and AKD2G drives and their documents are in the library

**Role(s):** electrical engineering, purchasing, legal

## What changed

The library now has the brand Kollmorgen, with two drive families:

- **AKD2G**, with the part AKD2G-SPE-6V03S-A1F3-0000-A (3 A rms, single axis, EtherCAT, Safe
  Torque Off). 15 documents: the installation manual for our safety option (FS1), the EtherCAT and
  CANopen manual, the Modbus manual, the part number scheme, the Smart Feedback Adapter datasheet,
  the EU Declaration of Conformity, the TÜV safety certificate, the UL certificate, the EtherCAT
  conformance certificate, safety notes, and the RoHS and REACH declarations.
- **AKD** (first generation), with the part AKD-P00306-NDCC-E000 (3 A rms, EtherCAT and CANopen).
  10 documents: the installation manual, the user guide, the EtherCAT manual, the part number
  scheme, the STO product notice of 1 October 2026, the UKCA Declaration, the RoHS declaration,
  the UL certificate, safety notes and the quick start guide.
- The accessories guide for Europe sits in the brand folder, because it covers both families.

Each family record lists the loop rates, the brake resistor, the mains filter, the encoder input,
the motor temperature input, the filters, the service port, the safety rating and the
manufacturer, with the page of the manual for each.

Two AKD2G installation manuals (for the safety options FS2 and FS3) are recorded with their
address and checksum, but are not committed. They are 35 MB and 45 MB, and they do not describe our
drive. Our copy is in `stoq-private`.

The manuals say they may not be copied without written permission from Kollmorgen. They are free
downloads from the Kollmorgen product pages, with no login. The proposal is to share them under
ADR-004 (share until the brand objects), as we did for Copley and HIWIN. Niels Bosmans approves
this in the pull request.

## Why it matters

We must choose between Kollmorgen and Copley this week for the AQTUATOR CS stage. The documents
answer most questions about the brake resistor, the connectors, the filters and the safety
certificate. The comparison is in the aqtuator log of the same day.

## What was not added

- No CAD files. Kollmorgen offers its 3D models through a portal that needs a login.
- No price and no distributor.

## Next Steps

- Niels Bosmans approves the `public` decision with `basis = "none"` for the documents.
- Save a dated copy of page 3 of the AKD2G FS1 manual (the copyright clause) in `stoq-private`,
  with the FS2 and FS3 manuals.

<details>
<summary>Sources</summary>

- Downloads of 2026-11-25 from the Kollmorgen AKD2G and AKD product pages. Addresses and
  checksums are in each family's `vendor-index.csv`.
- Copyright clause: AKD2G-S Installation Manual FS1 Rev G, page 3.
- Online help read the same day: webhelp.kollmorgen.com/AKD2G (tuning, filters, terminal, IP
  ports, motor temperature, regeneration).
- `bash doqs.sh generate` wrote the usage graph. `bash doqs.sh check`: all gates passed.

</details>
