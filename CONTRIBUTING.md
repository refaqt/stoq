# Contributing to STOQ

STOQ records parts other people design, make and sell. Adding to it means
writing down what you found out about a part, so that the next project does not
have to find it out again.

Before you start, read [`docs/architecture.md`](docs/architecture.md) and
[`modules/README.md`](modules/README.md). The full specification is
[`doqs/docs/parts-library.md`](doqs/docs/parts-library.md).

## One command

```bash
bash doqs.sh check
```

That runs every gate. Run it before every commit. `doqs.bat check` is the same
on Windows, and `python doqs/doqs.py check` works without either launcher.
`bash doqs.sh list` prints every command.

## Recipes

**Adding any supplier file — a CAD file, a datasheet, a manual — follows
[`docs/adding-components.md`](docs/adding-components.md).** That page decides
whether a file may be committed at all. The recipes below are the short form.

### Add a part to an existing family

1. A row in `bom/parts.csv`. Part number, description, the figures that matter
   for choosing it, mass, terms, revision, `status = "active"`.
2. Keep every original file in `stoq-private`, at the same path.
3. If someone needs the geometry now, and the brand's newest `cad` decision is
   `public`: put the STEP in `cad/original/<pn>.step`, build
   `cad/parts/<pn>.FCStd` from it, and fill the `cad` column. If the decision is
   not `public`, keep the files out of git, or draw our own model in `cad/own/`
   instead. If nobody needs the geometry yet, leave the column empty. The table
   is the complete catalogue; the files are a cache that fills as people use
   parts.
4. A row in `vendor-index.csv` with the address, the checksum and the date.
5. `bash doqs.sh check`.

### Add a family

1. `modules/<brand>/modules/<family>/okh.toml`, from
   [`doqs/templates/parts-library/family-okh.toml`](doqs/templates/parts-library/family-okh.toml).
   It needs `[brand]`, and `[[provides-interface]]` where the family has a real
   mechanical interface.
2. `bom/parts.csv` with the parts you know about, from
   [`doqs/templates/parts-library/bom/parts.csv`](doqs/templates/parts-library/bom/parts.csv).
3. `bash doqs.sh generate`, then `bash doqs.sh check`.

### Add a brand

1. `modules/<brand>/okh.toml`, from
   [`doqs/templates/parts-library/brand-okh.toml`](doqs/templates/parts-library/brand-okh.toml).
   It needs `[brand]`, including `cad-terms`.
2. **Read those terms**, save a dated copy in `stoq-private/evidence/<brand>/`,
   and add one `[[terms-review]]` for `cad` and one for `documentation`. Set
   `redistribute` to match the `cad` one. A named person approves both. See
   [`docs/adding-components.md`](docs/adding-components.md), steps 3 to 5.
3. Then add a family.

### Retire a part

Set `status = "eol"`. Do **not** delete the row and do **not** delete the file.
Add the replacement part number to `notes` if there is one, so a machine that
selected the old part gets a useful warning.

## The catalogue table

`bom/parts.csv` has one row per orderable part number, and this header exactly:

```
pn,description,spec,unit_mass_g,cad,datasheet,terms,revision,status,notes
```

Lines starting with `#` are comments and are skipped.

`terms` is `redistributable`, `fetch-only`, `private` or `own-model`. `status`
is `active` or `eol`.

**No price and no distributor.** A parts library is technical. What a part costs
and who sells it are answered by a different system, and both change far faster
than the part does.

## Naming

Brand and family folders are kebab-case: `hiwin`, `hgr-rail`, `din-912`.

Part numbers keep the brand's own casing, **verbatim**: `HGR20R500`. This is the
one documented exception to kebab-case, because the part number is the string
you order by and search for. See [`doqs/docs/naming.md`](doqs/docs/naming.md).

## Copyright: store the link, not the file

Commit text by default. Part numbers, dimensions, masses and the specifications
we write down are facts we gathered and organised. They are the bulk of the
value here.

- **`fetch-only`** is the default. The address, the checksum and the retrieval
  date are committed; the file is not. Each person downloads it from the brand
  under the brand's own terms. This needs no legal opinion and works in a public
  repository.
- **`redistributable`** only where the brand's newest `[[terms-review]]` for
  that kind of file says `public`.
- **`private`** like `fetch-only`, but the file has no public address. The only
  copy is in `stoq-private`.
- **`own-model`** a model we drew ourselves from the datasheet, in `cad/own/`.
  It is ours, so it is always committed.

A `fetch-only` or `private` file is listed in `.gitignore` by its exact path, so
a fresh clone stays green. Validation warns rather than fails when the file is
absent, and fails when git tracks it. `bash doqs.sh restore-private --from
../stoq-private` copies these files into place.

Two things to check with a lawyer before committing any brand's files: the
download terms of your main suppliers, and whether the EU database right affects
copying a large part of a catalogue. This page is not legal advice.

## Nothing is ever removed

This is the rule that lets a machine pin one commit of this repository and still
find every part it was built from, years later.

- A part row is never edited in place when the part itself changed. A revised
  design is a new row with a new revision and, almost always, a new part number.
- A part you can no longer buy gets `status = "eol"`. That stops new designs
  choosing it. It never deletes what an existing machine is made of.

Two consequences. The history of this repository is **never rewritten** — no
squash and no force-push on `main`, or every build record that points here
breaks. And checksums are checked, not just recorded: if a brand changes a file
under the same part number, add a new row rather than overwriting the old one.

## Branching

Every task that changes this repository starts on a **new git branch** off
`main`. Do not land task work as commits directly on `main`.

Write pull requests and commit messages for a manager, not for a developer.
The headings are in [`.github/pull_request_template.md`](.github/pull_request_template.md);
the rules behind them are in `.agents/rules/reporting.md`.

## Licence files are generated

Never hand-write a `LICENSE` or `TRADEMARKS.md`. `bash doqs.sh generate` renders
them, including a stub for every `cad/` and `docs/datasheets/` folder you add.
Read the diff before you commit it.

There is deliberately no CERN Open Hardware Licence in this repository. Writing
one over a supplier's file would claim a licence on something we do not own, and
the licence check treats it as an error.
