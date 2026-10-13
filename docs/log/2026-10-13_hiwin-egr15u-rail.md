# 2026-10-13 — The HIWIN EGR15U rail is in the library

**Role(s):** mechanical engineering, purchasing

## What changed

The EGR15U418H rail is now in the library, as a second row of the `egr-rail` family. It is the
EGR15 rail with large mounting holes, for M4 screws instead of M3. It has the HIWIN STEP file and a
FreeCAD part with the same two frames as the EGR15R418H rail: `IF_mount_bottom` on the first hole
and `IF_block` at the rail start. X runs along the rail and Z points up.

## Why it matters

A machine can use this rail in place of the EGR15R rail without changing its assembly: the frames,
the profile and the hole positions are the same. The QEH15 block runs on both.

## Next Steps

- None.

<details>
<summary>Technical notes</summary>

- File: `modules/hiwin/modules/egr-rail/cad/parts/EGR15U418H.FCStd`, built in the FreeCAD 1.1
  window with the same steps as the EGR15R418H part (see
  [2026-10-13_hiwin-eg-rail-qe-block.md](2026-10-13_hiwin-eg-rail-qe-block.md)).
- The HIWIN shape has the same axes as the R rail: 0…418 mm in Y, 12.5 mm high, holes at
  y = 29 + 60·k. Holes are 4.5 mm with a 7.5 mm counterbore (catalogue table 3.48).
- Same family, not a new one: the profile and the hole pitch are the same as the R rail; only the
  screw size differs.
- Mass: 1.23 kg/m × 0.418 m = 514 g.
- The rows were added by hand, because the pinned `doqs` version on `main` has no `add-part`.
  The private rows are `internal`; the retrieval date is the STEP header time.
- `bash doqs.sh check` passes.

</details>
