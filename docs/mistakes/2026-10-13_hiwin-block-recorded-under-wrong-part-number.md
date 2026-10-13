# 2026-10-13 — A HIWIN block was recorded under the wrong part number

## What happened

The QE block was added as QEH15CAZAP+E2. The real part is QEH15SAZAP+E2, the light
load block. The HIWIN configurator gave the file the CA name. The block in the file has
2 mounting holes, and the catalogue shows 4 for a CA block. Instead of questioning the
name, we explained the difference with a guess: that the E2 lubrication unit took the
place of one hole row. The row also had the CA length and load ratings, so a design
sized on it would have expected about 45 % more dynamic load capacity than the block has.

## Why it went wrong

The part number was copied from the supplier's file name and not checked against the
catalogue table. When the model did not match the table, the model was explained away
and the part number was not questioned.

## Prevention rule

Check the part number against the catalogue table before you record it. If the
supplier's model does not match the table for that number (holes, length, shape),
first suspect the part number, and ask the person who orders the part.

## Related

- [Log 2026-10-13: HIWIN EG rail and QE block](../log/2026-10-13_hiwin-eg-rail-qe-block.md)
- [`modules/hiwin/modules/qeh-block/bom/parts.csv`](../../modules/hiwin/modules/qeh-block/bom/parts.csv)
