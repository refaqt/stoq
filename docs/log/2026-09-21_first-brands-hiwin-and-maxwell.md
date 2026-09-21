# 2026-09-21 — The first two brands: HIWIN and MAXWELL

**Role(s):** Mechanical engineering, documentation

## What changed

This library now holds parts. Two brands moved in from the AQTUATOR machine
repository, where supplier files were sitting in the machine's own CAD folder.

HIWIN covers the X-axis linear guide: one profile rail and one block.
MAXWELL covers the linear motor: the magnet track in three lengths, the mover
in four lengths, and one older forcer that was selected before the MK2 range.

Nine parts are now in the catalogue. Seven have a file. The other two are
recorded because the table is meant to be the whole catalogue, and geometry
only gets downloaded when somebody needs it.

## Why it matters

The AQTUATOR machine no longer stores the rail, the block and the magnet track
itself. It points at them. The next machine that buys a HIWIN HGR15 rail finds
the part number, the mass, the accuracy class and the model already written
down.

## What was decided along the way

Both brands are marked as files we may share, so the machine's X-axis assembly
keeps working for anyone who clones it. The reasoning and the limits of that
call are in
[the decision record](../decisions/2026-09-21_committing-supplier-cad.md).

The motor parts are filed under MAXWELL, not Saho. Saho sells them; MAXWELL
makes them and puts its name on the catalogue and the part. This library
records the brand, never the supplier.

## What is still weak

Three things are worth knowing before anyone orders from these rows.

The MK24 mover mass is printed as 1.9 kg in the brand's catalogue. The three
shorter movers weigh 1.1, 2.2 and 3.3 kg. The figure looks like a misprint for
about 4.4 kg. It is recorded as printed, with a warning on the row.

The WJM050-3 forcer has almost nothing behind it. There is one FreeCAD
document, no catalogue, no datasheet, no supplier file and no download address.
Even the brand is a guess, taken from the name the download left inside the
document. Confirm who makes it before ordering one.

The MAXWELL files carry no source address, because they came with a quotation
rather than from a public page. The checksum is the only guard they have.

<details>
<summary>Notes for reviewers</summary>

Layout follows `doqs/docs/parts-library.md`. Brands are `modules/hiwin/` and
`modules/maxwell/`. Families are `hgr-rail`, `hgl-block`, `mk2-mover`,
`mk2-stator` and `wjm-forcer`.

Each brand's catalogue PDF sits at brand level in `docs/datasheets/`, not inside
a family, because one catalogue covers several families. Family rows reach it
with a relative path. `apply_licenses.py` writes the supplier carve-out stub at
that level without complaint.

Supplier downloads keep their bytes but are renamed to `<part number>.step`, as
the specification prescribes. The original file names are kept in the `notes`
column where they differ.

The FreeCAD documents came from AQTUATOR. Only their document label and their
`App::Part` label changed, from the machine role name to the part number.
Object names are untouched, so the external links in the machine's assemblies
still resolve.

`HGL15CA2R760ZBC2-ZZ+E2` is an assembled guideway of two 760 mm rails with two
blocks each. It has a row in `vendor-index.csv` but none in any `parts.csv`,
because an assembled guideway is neither a block nor a rail.

Git LFS is now switched on for `.FCStd`, `.step`, `.stp`, `.stl` and `.3mf`.
Datasheet PDFs stay ordinary git objects, which matches AQTUATOR.

`bash doqs.sh check` passes every gate.
</details>
