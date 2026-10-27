# 2026-10-27 — The RSF MC 15 absolute linear encoder is in the library

**Role(s):** mechanical engineering, purchasing, legal

## What changed

RSF Elektronik (Tarsdorf, Austria, HEIDENHAIN group) is a new brand in the library, with two
families for its MC 15 absolute exposed linear encoder:

| Family | Part number | What it is | CAD |
| --- | --- | --- | --- |
| `mc15-readhead` | AK-MC15-B-0.5M-SUBD15 | Scanning head, BiSS C, 0.5 m cable, 15-pin D-sub, 36 x 13.5 x 14.8 mm | RSF STEP file, with three mounting frames |
| `mc15-mk-scale` | MB-MC15-MK-ML220 | Steel tape scale with adhesive tape, 220 mm measuring length, 240 mm long | Our own model, drawn from the RSF drawing |

The RSF catalogue, the BiSS C interface description, the declaration of conformity, the read
head mounting instructions, the MK mating drawing and the tape mounting tool instructions are in
the library too.

RSF publishes the MK scale as a STEP file only for a 100 mm measuring length. The 220 mm scale is
therefore our own model. A separate comparison with the RSF 100 mm file passed for every size
it can show.

## Why it matters

The compact stage in aqtuator needs an absolute encoder with a 220 mm measuring length. A machine
can now place the head on the scale with one joint: the head frame `IF_scale` meets the scale
frame `IF_ml_start` or `IF_ml_end`, and the air gap and the side offset are then right.

## Next Steps

- Ask RSF for the ID number of the AK MC 15 B with a 0.5 m cable. The catalogue lists only 1 m
  and 3 m cables.
- RSF does not allow sharing. Item 10 of the RSF Terms of Use forbids reproduction without
  consent, and the drawings carry the ISO 16016 notice. The files are shared until RSF objects,
  the same as for HIWIN, LAMOTION and ACE. Niels Bosmans approves this in the pull request. The
  check shows a warning for it, as expected.
- Ask RSF for written permission, if the encoder stays in the design.

<details>
<summary>Technical notes</summary>

- Sizes of the scale (drawing D1158017-04, one sheet): OL = ML + 20, steel tape 8 x 0.25 mm,
  adhesive tape 6 x 0.2 mm. At the start of the measuring length the side of the head is 7 mm
  before the tape start, and the position sensor is 16.2 mm from that side, so the sensor runs
  from X = 9.2 to X = 229.2 on the tape.
- The scale model was built inside the FreeCAD window and saved there, as the mistake note of
  2026-10-20 asks. The FreeCAD window had other documents open, so the build helper treated the
  run as interactive and did not save. The document was saved by hand and the fingerprint written
  again from the saved file.
- The read head wrapper was built by hand, as for ACE: `ImportGui.insert`, the importer's Part
  container relabelled, three frames with `cad_build.frame()`, then `cad_build.show_new_objects()`.
  A fit test placed our tape on the head through the frames: air gap 0.55 mm, tape edge 11.5 mm
  from the head, tape start 7 mm past the head side, as the drawing says.
- The RSF 100 mm scale file is kept only in stoq-private, for the comparison.
- Evidence in stoq-private: `evidence/rsf/2026-10-27_terms-of-use.pdf`.

</details>
