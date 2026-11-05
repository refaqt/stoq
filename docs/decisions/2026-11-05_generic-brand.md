# ADR-006 — Parts without a brand go under `generic`, recorded by their specification

- **Date:** 2026-11-05
- **Status:** Accepted. Niels Bosmans asked for it.

Write this file in B2 English. Follow `.agents/rules/communication.md`.

## Context

The magnet tape for the seal strip of the aqtuator compact stage is sold without a brand name.
The seller gives only a specification. The library files every part under the brand on the part,
and a seller is not a brand. For standard parts, the standards body takes the place of the brand
(`iso`), but no standard covers this tape.

## Decision

A part with no brand name goes under the brand folder `generic`. The family names the kind of
part (`ndfeb-magnet-tape`). The part number is built from the specification, the way a standard
part is named: width x thickness x length in mm, for example `3X0.5X80`.

A piece we cut from a bought roll is its own row, with the cut length in its part number. The
row of the bought roll stays next to it.

The seller's product page may be the source of a size, as for the ISO washer. The seller's name,
price and stock never go in the part table.

## Consequences

- A machine can name the tape in its bill of materials, like any other part:
  `stoq:generic/ndfeb-magnet-tape#3X0.5X80`.
- Two sellers can sell different tapes under the same specification. The part number does not
  tell them apart. Measure a real piece before you rely on a value that the specification does
  not give, such as the holding force.
- `generic` has no brand files and no terms to review. Every model in it is our own.
