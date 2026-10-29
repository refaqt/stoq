# 2026-10-28 — The bearing, pin and washer of the seal strip rollers are in the library

**Role(s):** mechanical engineering, purchasing

## What changed

Two new brands are in the library, with three parts. Each part has our own model, drawn from the
published sizes:

| Brand | Family | Part number | What it is |
| --- | --- | --- | --- |
| `nsk` | `miniature-flanged-metric` | F692ZZ | NSK flanged ball bearing, 2 × 6 × 3 mm, flange 7.5 × 0.8 mm, shields on both sides |
| `iso` | `iso-8734` | 2X28-A | Hardened dowel pin, ISO 8734, 2 mm (m6) × 28 mm, type A |
| `iso` | `iso-7092` | 2-200HV-A2 | Small plain washer, ISO 7092, for M2, 2.2 × 4.5 × 0.3 mm, A2 stainless steel |

For a standard part, the brand is the standards body, so the dowel pin and the washer are under
`iso`.

## Why it matters

The compact stage in aqtuator uses these parts in its eight seal strip rollers. Each roller has
one pin, two bearings and two washers, with a tube of our own between the bearings. The bearings
turn with about 0.2 N of drag in total, where a plastic roller on the pin would give 35 to 52 N.
See the decision in aqtuator, `docs/decisions/2026-10-28_seal-strip-rollers-on-flanged-ball-bearings.md`.

## Next Steps

- No brand files are stored. NSK gives its CAD files only after a log-in, and a standard part has
  no brand model. So the comparison rows of the three models say `not-confirmed`. Compare the
  bearing with the NSK CAD file, and measure a real pin and washer, when they arrive.
- The NSK brand has no terms review yet, because no NSK file is in the library. Add one before a
  NSK file or datasheet is committed.
- No copy of the NSK table is in stoq-private yet. Save it there as a PDF.

<details>
<summary>Technical notes</summary>

- Bearing sizes and ratings: the NSK web table "Extra Small Ball Bearings and Miniature Ball
  Bearings, Metric Series With Flange", row F692ZZ, read on 2026-10-28. The open F692 is narrower
  (B 2.3 mm, C1 0.6 mm). NSK gives no mass, so the row has none.
- Pin sizes: the ISO 8734 designation `ISO 8734 - 2 x 28 - A - St`. The end chamfer and the
  rounded end are left out, because their sizes are in the standard text, which we do not hold.
- Washer sizes: the Würth data sheet of `ISO 7092 - 2 - 200 HV - A2`.
- Aliases: `D1` and `C1` are cell addresses in a FreeCAD sheet and cannot be aliases, so the
  bearing uses `bore_d`, `outer_d`, `width_b`, `flange_d1` and `flange_c1`.
- Frames: F692ZZ `IF_flange_face` (z = 0) and `IF_seat` (z = `flange_c1`), both turned 180° about
  X so that Z points out of the flange side; 2X28-A `IF_centre`; 2-200HV-A2 `IF_face`. All saved
  hidden, as in ADR-005.
- Built headless with FreeCAD 1.1.3. A headless build leaves the document marked as changed after
  the save, because `show_new_objects()` sets the visibility after the last recompute. Then the
  fingerprint records `saved: false` and no checksum. Each file was opened again, recomputed and
  saved with `cad_build.save()`, and the fingerprint was written after that.
- `bash doqs.sh check`: all gates passed.

</details>
