# 2026-11-05 — The MK21 thermal sensor values are in the library

**Role(s):** electrical engineering

## What changed

The MK21 forcer (the moving coil part of the Maxwell MK2 linear motor) now has a page with the
values of its heat sensor. The sensor is three PTC thermistors in series. A PTC thermistor is a
resistor whose resistance rises steeply when it gets too hot. The values come from a table that
MAXWELL sent.

The most important values: at 25 °C the sensor reads 300 Ω or less. Just below the switch point
it reads 1 650 Ω or less. Just above it reads 3 990 Ω or more. It must never see more than 30 V.

## Why it matters

The data sheet only named the sensor "3 PNC SNM120 in series". Without the values, nobody could
say if a servo drive reads it correctly. Now a drive can be checked against the sensor: any drive
with a PTC input and a trip point between 1 650 Ω and 3 990 Ω fits.

## Next Steps

- Ask MAXWELL to confirm that the switch point (rated response temperature) of the MK21 sensor is
  120 °C. The name "SNM120" points to it, but the table does not say it.
- Ask MAXWELL whether the MK22, MK23 and MK24 have the same sensor. Only the MK21 row has it now.

<details>
<summary>Technical notes</summary>

- New page: `modules/maxwell/modules/mk2-mover/docs/mk21-thermal-sensor.md`. It holds the whole
  "three-core PTC in series" column of the MAXWELL table, with Tk as a variable.
- `modules/maxwell/modules/mk2-mover/bom/parts.csv`: the MK21 spec has a short thermal sensor
  part, and the notes point to the new page.
- The MAXWELL table arrived as a screenshot in chat. It is not committed. Its values are typed out
  in the page.
- `bash doqs.sh check` passes.

</details>
