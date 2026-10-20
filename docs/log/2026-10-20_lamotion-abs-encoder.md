# 2026-10-20 — The LAMOTION ABS linear encoder is in the library

**Role(s):** mechanical engineering, purchasing, legal

## What changed

LAMOTION is a new brand in the library, with three families for its absolute optical linear
encoder:

| Family | Part number | What it is | CAD |
| --- | --- | --- | --- |
| `abs-readhead` | AL32B050-30MUL | Read head: 32 bit, BiSS-C, 50 nm, 3 m cable with a D-sub connector, cable out of the end | LAMOTION STEP file, with mounting frames |
| `alz-scale` | ALZ00270G | Steel tape scale, 270 mm, with adhesive backing | Our own model |
| `rus-et-clamp` | RUS-ET-A-B | The pair of end clamps that hold the scale ends | Our own model |

The LAMOTION STEP files had Chinese names. They are now stored under the part number. The file
that shows the read head on a short piece of scale is kept next to the read head, for reference.
The ABS datasheet is in the library. So is the RX2 datasheet, because it is the only LAMOTION
document that gives the end clamp thickness (0.5 mm).

## Why it matters

A machine can now use the encoder in an assembly: the read head sits 0.8 mm above the scale,
and the clamps hold the scale ends, all joined on frames. The scale and the clamps change with
one value each, so another scale length is a quick rebuild.

## Next Steps

- LAMOTION does not allow sharing. Page 2 of its datasheet says that nobody may copy, translate
  or spread the document without written permission. Niels Bosmans decided to share the files
  anyway, until LAMOTION objects, as for HIWIN. Asking LAMOTION for written permission would
  remove this risk.
- The part number of the read head follows our choice, not an order: the 3 m cable has the
  shortest delivery time, and 32 bit and 50 nm are the values in the datasheet drawing. Check it
  against the first purchase order.
- Four sizes of the end clamps are estimates: the notch depth, its position across the width,
  the corner radius and where the scale ends inside the notch. Measure a real clamp.
- The scale mass (3 g) is an estimate from the steel volume. The clamp mass is unknown.

<details>
<summary>Technical notes</summary>

- Read head: `modules/lamotion/modules/abs-readhead/cad/parts/AL32B050-30MUL.FCStd`, built in the
  FreeCAD 1.1 window. It holds an `App::Part` labelled `AL32B050-30MUL` with the five imported
  LAMOTION solids (with their colours) and two frames, attached `FlatFace` to the part's
  `XY_Plane`:
  - `IF_scale`: on the optical centre line (x = 0), 0.8 mm below the head (y = −0.8), on the top
    of the scale. X along the scale, Z up (−90° around X).
  - `IF_mount_side`: on the side face z = 8.25, midway between the two M3 holes (x = 1, y = 3).
    Z points into the head (180° around X).
- STEP axes, kept as they are: X along the scale, Y up (head bottom at y = 0), Z across. The
  cable leaves the −X end. M3 holes at x = −12 and x = 14, matching the 26 mm and 12 mm in the
  datasheet drawing (page 9).
- Source files: `绝对值外形.STEP` → `AL32B050-30MUL.step`; `绝对值直线栅尺组合.STEP` →
  `AL32B050-30MUL+ALZ.step`, both from `ABS+AHBS_STEP.rar` on lamotion.cn. The 90° cable exit
  file (`ABS_90°出线.STEP`) would be the R variant; it was not added.
- Own models: `ALZ00270G.build.py` and `RUS-ET-A-B.build.py` in each `cad/own/`, with
  `params.csv`, `features.csv`, `checks.csv` and a fingerprint, rebuilt headless. Same axes as the
  LAMOTION model. Scale frames: `IF_mount_bottom` (scale start, adhesive bottom) and `IF_head`
  (scale start, tape top). Clamp frame: `IF_scale_start`, which joins `IF_mount_bottom`; clamp B
  sits at `scale_len`.
- The scale model was built from the datasheet only. It was then compared with the scale piece
  in the LAMOTION head-and-scale file: width, thickness, adhesive and the 0.8 mm gap pass; the
  length cannot be compared. The clamps have no LAMOTION file, so every result is not-confirmed.
- Test assembly in a scratch document: head to scale 0.8 mm, clamps touch the scale ends with no
  overlap. Checked in a picture.
- Page numbers in the files are the numbers printed on the page; the PDF page is one more.
- Private copies: `stoq-private`, same paths, rows `internal`; evidence in
  `evidence/lamotion/` (datasheet copyright page and website home page, both 2026-10-20).
- `bash doqs.sh check` passes with the pinned doqs and with the newest doqs. The new rules
  (`features.csv`, the longer `params.csv` header) are followed.

</details>
