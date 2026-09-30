# ADR-002 — One method for every supplier file

- **Date:** 2026-09-29
- **Status:** Accepted
- **Builds on:** [ADR-001](2026-09-21_committing-supplier-cad.md), and doqs
  [ADR-009](../../doqs/docs/decisions/2026-09-29_component-intake.md), which works
  with doqs [ADR-008, a private parts library](../../doqs/docs/decisions/2026-09-29_private-parts-library.md)

## Context

ADR-001 decided, once and for the whole brand, that the HIWIN and MAXWELL files
may be shared. There was no fixed way to make that decision for the next brand,
and no copy of the terms that were read.

Three needs were not met:

- Some files may not be published, but we still need to keep them. Customers
  need them for service and reorders after a part leaves the market.
- A brand may allow its datasheet to be shared, but not its CAD files.
- When we may not share a CAD file, a machine design still needs the geometry.

## Decision

Every supplier file follows [`docs/adding-components.md`](../adding-components.md):

1. Record the facts in STOQ, and keep every original in the private parts
   library `refaqt/stoq-private`, at the same path, with `terms = "internal"`.
2. Save a dated copy of the terms.
3. Decide for the CAD files and for the documentation separately: `public`,
   `customers` or `internal`. An agent may propose. A named person approves.
4. Then choose a route: sharing is allowed, ask for written permission, or draw
   our own model from the datasheet.

`stoq-private` is never a submodule of STOQ or of a machine repository, because a
public clone could not fetch it.

The HIWIN and MAXWELL decisions from ADR-001 are recorded in the new form, as
they were made. For MAXWELL nothing written allows the sharing, because the
files came with a quotation. That is now visible as a warning in every check.
This change does not change what is shared. That remains Niels Bosmans's call.

## Consequences

A new brand cannot be shared without a recorded decision and a named reviewer.
The check enforces this.

Files that may not be shared can no longer be committed by mistake. The check
fails if git tracks one.

Our own models are CC BY-SA 4.0, so a public machine design always has usable
geometry, even when the brand's file stays private.

Open for MAXWELL: ask for written permission, or add a new decision that stops
sharing its files. The permission email is in the method.
