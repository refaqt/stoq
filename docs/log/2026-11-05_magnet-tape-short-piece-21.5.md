# 2026-11-05 — The short magnet strip is now 21.5 mm

**Role(s):** mechanical engineering, purchasing

## What changed

The short piece of magnet tape for the compact stage base is now 21.5 mm long, not 80 mm. The
base needs eight of them, not four.

| Part number | What it is | Per base | Status |
| --- | --- | --- | --- |
| `3X0.5X21.5` | Short piece: four in each end leg of the magnet ring | 8 | new |
| `3X0.5X80` | The old short piece | 0 | `eol` |

The 80 mm piece was never cut or used. It stays in the table as `eol`, because nothing is ever
removed from this library.

## Why it matters

When the strips were put in the aqtuator assembly, Niels saw that each 80 mm piece lay over a
damper slot in the end wall of the base. There the strip has no floor under it. Each end leg has
four pieces of solid floor, between a cavity at the corner, the two damper slots and the split at
the preload screw. One strip now sits on each of them.

The order does not change: 3 rolls per base. One roll gives one long piece and three short pieces
(417.5 + 3 x 21.5 = 482 mm of 500 mm). The third roll gives the last two short pieces.

## Next Steps

- Measure a real piece, as the log of the first pieces asks.

<details>
<summary>Technical notes</summary>

- Measured on the aqtuator base (`b4a342b`, after the rail tab was removed): holes in the floor of
  the ring end legs (x 7 to 10 and 430 to 433, just under z 39.35) at y 18 to 29, 52.5 to 76.5
  (damper slot), 133.5 to 157.5 (damper slot) and 181 to 192. Solid floor: 29 to 52.5 (23.5 mm),
  76.5 to 98.5 (22 mm), 111.5 to 133.5 (22 mm), 157.5 to 181 (23.5 mm). One length for all
  four: 22 − 2 x 0.25 = 21.5 mm. Niels chose one length over two lengths (34 + 21.5 mm).
- `3X0.5X21.5.*` are copies of the `3X0.5X80.*` sources with the new length and text.
- Built in the FreeCAD 1.1 window: the `.FCStd` was saved empty, built by its script, saved with
  `cad_build.save()`, `IF_end` hidden, saved again, and fingerprinted with the parameters. It was
  opened again in the window: the bar shows, `IF_end` is hidden, size 21.5 x 3 x 0.5 mm. The file
  starts with `PK`.
- The `doqs/` folder of this repository was out of date (no `cad_build.save()`). `bash
  setup-tooling.sh` brought it to the newest `main`; the gitlinks are not committed.

</details>
