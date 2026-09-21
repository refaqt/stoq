# ADR-001 — Commit the HIWIN and MAXWELL files instead of only linking to them

- **Date:** 2026-09-21
- **Status:** Accepted

## Context

This library normally stores the link, not the file. It records the address, the
checksum and the date, and each person downloads the file from the brand. That
default needs no legal opinion and works in a public repository.

The first two brands here do not fit that default well.

The AQTUATOR machine repository already held these files. They sat in its CAD
folder and were published with it. Its X-axis assembly links three of the
FreeCAD documents by path. If we had recorded only the addresses, the assembly
would open with broken links for everyone who clones the machine, until each
person downloaded the parts again by hand.

Two of the files also have no address to record. The MAXWELL parts arrived with
a quotation, not from a public download page.

## Decision

Both brands are marked `redistribute = true`, and every file is committed.

The address of the terms we read is written in each brand's manifest:
the HIWIN general terms and conditions, and the MAXWELL company site, which
publishes no separate download terms.

Niels Bosmans made this call on 2026-09-21. It is a reading of those terms. It
is not legal advice, and no lawyer has checked it.

## Consequences

The X-axis assembly keeps working for anyone who clones the machine. Nobody has
to repeat a download to open a model.

The library carries about 16 MB of supplier files. That is small today. If it
grows, the ways to keep a checkout small are described in the parts library
specification.

This decision is reversible for new files but not for old ones. History here is
never rewritten, so a file committed today stays in the history even if a brand
later objects. If a brand does object, the next step is to set that brand to
`redistribute = false`, move its rows to `fetch-only`, and stop adding files —
not to rewrite the past.

Anyone adding a third brand should start from `fetch-only` again. This decision
covers HIWIN and MAXWELL only.
