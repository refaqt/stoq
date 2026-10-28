# ADR-005 — Mounting frames are saved hidden in this library

- **Date:** 2026-10-28
- **Status:** Accepted. Niels Bosmans asked for it.
- **Differs from:** doqs [ADR-014](../../doqs/docs/decisions/2026-10-07_imported-solids-and-frames-visible.md),
  which opens a new mounting frame visible

Write this file in B2 English. Follow `.agents/rules/communication.md`.

## Context

Every part in this library has mounting frames: the named points, with their own
axes, where an assembly joint attaches (`IF_...`). They were saved visible. A
machine assembly links many parts, so it showed every frame of every part. In
the aqtuator compact stage, the frames covered the parts.

## Decision

Every mounting frame in a part file of this library is saved hidden. A designer
who needs one shows it in the FreeCAD window (select it and press the space
bar). Joints still attach to hidden frames.

## Consequences

- An assembly that links our parts shows only the parts.
- A rebuild keeps a frame hidden, because a build does not change the visibility
  of an object that already exists.
- A new frame, made by a build script or by `doqs add-interface`, still opens
  visible. Hide it before you commit the part.
