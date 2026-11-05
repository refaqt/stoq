# 2026-11-05 — The magnet strips of the compact stage base are in the library

**Role(s):** mechanical engineering, purchasing

## What changed

The magnet tape that holds the seal strip down is in the library, with the two pieces we cut from
it. The tape has no brand name, so it is under a new brand folder, `generic`, and is named by its
specification (see [ADR-006](../decisions/2026-11-05_generic-brand.md)).

| Part number | What it is | Per base |
| --- | --- | --- |
| `3X0.5X500` | The bought roll: neodymium magnet tape, 3 mm wide, 0.5 mm thick, 0.5 m long | 3 |
| `3X0.5X417.5` | Long piece: one on each long side of the magnet ring | 2 |
| `3X0.5X80` | Short piece: one in each end leg of the magnet ring, between a corner and the split at a preload screw | 4 |

Each piece has our own model: a flat bar, built by a script from a table of sizes.

The specification of the tape, translated from the seller's Dutch product page, read on
2026-11-05:

| Property | Value |
| --- | --- |
| Shape | Tape on a roll |
| Width | 3 mm |
| Thickness | 0.5 mm |
| Length | Roll of 0.5 m |
| Material | Neodymium (NdFeB) in a flexible binder |
| Magnetisation | Multi-pole, with the poles side by side along the length |
| Holding force | About 150 g/cm² (about 0.015 N/mm²) |
| Maximum working temperature | 100 °C |
| Adhesive | Strong self-adhesive 3M film layer on one face |
| Colour | Anthracite |
| Bending | It bends only to a limited degree |

The seller does not give the pole pitch, the mass, the tolerances, or whether the 0.5 mm includes
the adhesive layer.

## Why it matters

The seal strip of the compact stage carries almost no pull in its middle, so the magnets must
hold it flat. The base already has the ring pocket for them: 3 mm wide and 0.5 mm deep, cut in two
at each preload screw. The tape is 3 mm wide, so it cannot bend sideways around the rounded
corners of the ring. Straight pieces are the only way to fill it.

The pieces are not in the compact stage assembly yet, because another piece of work is changing
the base. When they go in, they lie on the floor of the ring pocket, adhesive face down.

## Next Steps

- **The part files are not built yet.** This session had no FreeCAD. Build the three models on a
  computer with FreeCAD 1.1, inside the FreeCAD window (see the mistake note of 2026-10-20), and
  commit the part files and their fingerprints. Until then, the library check fails on the three
  missing files.
- Check the cut lengths against the base when its new version is ready. They come from the base
  of 2026-11-05.
- Order 3 rolls for each base. One roll gives one long piece and one short piece
  (497.5 mm of 500 mm). The third roll gives two short pieces.
- Measure a real piece: thickness with and without the adhesive layer, and the holding force on
  the 0.15 mm seal strip. The seller's 150 g/cm² is three times the 0.005 N/mm² that the
  seal strip simulations assume. It is measured on steel of unknown thickness, so on a 0.15 mm
  strip the real pull is lower.
- Save a copy of the seller's product page in stoq-private.

<details>
<summary>Technical notes</summary>

- Ring geometry, read from the fingerprint of `aqtuator/modules/compact-stage/cad/parts/base`
  at aqtuator commit 878c3b6: ring outline `Sketch006` x 7 to 433, y 14 to 196 at the top, R4
  outer corners, ring width 3 mm (`ring_w`); slot edge at x 10 and 430, y 17 and 193; ring floor
  at z 39.35 (0.15 mm strip pocket plus 0.5 mm). `MagnetRingSplitSketch`: solid split from
  y 98.5 to 111.5 at the wall, R4 arcs tangent to the wall at y 98.5 and 111.5.
- Long side: straight from x 11 to 429 (418 mm) between the corner arcs; piece 417.5 mm.
- End leg: straight from y 18 (corner arc) to y 98.5 (split arc), 80.5 mm; and from y 111.5 to
  192; piece 80 mm. Each corner keeps about 4 mm without magnet.
- The cut lengths use basis `catalogue` with the aqtuator base as the source, because the check
  allows only `catalogue`, `estimated` or `measured`.
- Model axes: X along the length from one cut end, Y across the width from one edge, Z from the
  adhesive face; origin at a corner of the adhesive face. One frame, `IF_end`, at the origin.
- `bash doqs.sh check`: fails only on the three missing part files (validate_variants and the
  own-model build check). The rest passes.

</details>
