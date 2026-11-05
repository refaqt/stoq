# MK21 thermal sensor

The MK21 coil has a heat sensor. It is three PTC thermistors (resistors whose resistance rises
steeply when they get hot) wired in series. The sensor uses two wires. The MK21 data sheet names
it "3 PNC SNM120 in series". "PNC" is a misprint for PTC.

## Source

MAXWELL sent a table of PTC thermistor data. The values below are from its "three-core PTC in
series" column (三芯 PTC 串联). The table covers all rated response temperatures from 60 °C to
180 °C. The values below are stated against that temperature, so they are true for the MK21
whatever it is.

The rated response temperature (Tk) of the MK21 sensor is very likely 120 °C. This comes from
the name "SNM120" and from the 120 °C coil limit in the data sheet. MAXWELL did not state it in
the table. Confirm it with MAXWELL before you depend on the exact switch point.

## Values for three sensors in series

| Property | Symbol | Value | Unit |
| --- | --- | --- | --- |
| Highest voltage without damage | Umax | 30 | V |
| Normal measuring voltage | | ≤ 2.5 | V |
| Rated response temperature | Tk | 60 to 180 (MK21: 120, not confirmed) | °C |
| Tolerance of Tk | | ±5 | °C |
| Repeatability of Tk | ΔT | ±0.5 | °C |
| Resistance at 25 °C ± 1 °C (U ≤ 2.5 V) | R25 | ≤ 300 | Ω |
| Resistance at Tk − 5 K (U ≤ 2.5 V) | | ≤ 1 650 | Ω |
| Resistance at Tk + 5 K (U ≤ 2.5 V) | | ≥ 3 990 | Ω |
| Resistance at Tk + 15 K (U ≤ 7.5 V) | | ≥ 12 | kΩ |
| Resistance from −20 °C to Tk − 20 K (U ≤ 2.5 V) | | ≤ 750 | Ω |
| Response time | Td | < 5 | s |
| Insulation strength | V | 2.5 | kV |
| Highest storage temperature | Tlmax | 125 | °C |
| Lowest storage temperature | Tlmin | −25 | °C |

With Tk = 120 °C this means:

- Below 100 °C the sensor reads 750 Ω or less.
- At 115 °C it reads 1 650 Ω or less.
- At 125 °C it reads 3 990 Ω or more.
- At 135 °C it reads 12 kΩ or more.

One sensor alone has one third of each value (for example R25 ≤ 100 Ω, ≥ 1 330 Ω at Tk + 5 K).

## What this means for a drive

- A drive input for a PTC sensor works. Set its trip resistance between 1 650 Ω and 3 990 Ω.
  Then it trips between Tk − 5 K and Tk + 5 K.
- A drive input for a KTY, PT100 or PT1000 sensor (a sensor that measures the temperature in a
  straight line) does not fit. It would read a wrong temperature.
- Never put more than 30 V on the sensor. Values in this table are for 2.5 V or less.
