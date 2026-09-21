# Brands and families

One folder per brand, then one per family. Everything below is the shape the
checks expect. The full specification is
[`doqs/docs/parts-library.md`](../doqs/docs/parts-library.md).

## What is here today

| Brand | Families | What they are |
| --- | --- | --- |
| [`hiwin/`](hiwin/) | `hgr-rail`, `hgl-block` | Profile rail linear guideways |
| [`maxwell/`](maxwell/) | `mk2-mover`, `mk2-stator`, `wjm-forcer` | Iron core linear motors |

Both brands are marked as files we may share, so a machine that links one of
these models keeps working for anyone who clones it. A new brand starts from
`fetch-only` again. The reasoning is in
[ADR-001](../docs/decisions/2026-09-21_committing-supplier-cad.md).

## Brand is not supplier

The folder level is the **brand**: the name on the part, part of the part
number, unchanging for decades. HIWIN, Beckhoff, DIN.

It is **not** the supplier, which is where you buy the part. You often buy from
several at once, and that changes. No distributor and no price is recorded
here: a parts library is technical.

For a standard, the brand is the standards body: `modules/din/`.

## The family is the module. A part number is a row.

```
modules/hiwin/                      the brand
├── okh.toml                        [brand] with cad-terms and redistribute
└── modules/hgr-rail/               the family -- THIS is the module
    ├── okh.toml                    [brand], and [[provides-interface]] where
    │                               the family has a real mechanical interface
    ├── bom/parts.csv               ONE row per orderable part number
    ├── vendor-index.csv            provenance: address, checksum, date, per file
    ├── cad/
    │   ├── parts/HGR20R500.FCStd   the document a role links
    │   └── original/HGR20R500.step the untouched download
    └── docs/datasheets/            catalogues and datasheets
```

Where a difference is a number, it is another row. Where it is architectural --
an HGR20 rail and an HGR25 rail have different bolt patterns -- it is another
family.

There is **no `cad/vendor/`** here. That folder exists in a machine repository
only to carve one directory out of the hardware licence, because the rest of
`cad/` is ours and that one is not. In a library nothing is ours, so the
carve-out moves up to the repository and the folders go back to normal.

Where a family is genuinely parametric -- a DIN 912 screw range -- add
`cad/params/` and declare `[[model]]`, instead of downloading hundreds of files.

## Naming

Brand and family folders are kebab-case: `hiwin`, `hgr-rail`, `din-912`.

Part numbers keep the brand's own casing, **verbatim**: `HGR20R500`,
`AM8113-0F20`. This is the one documented exception to kebab-case. The part
number is the string you order by and search for, and rewriting it breaks that
link. See [`doqs/docs/naming.md`](../doqs/docs/naming.md).

## Starter files

Copy these rather than writing a manifest from memory:

| Template | Copy to |
| --- | --- |
| [`doqs/templates/parts-library/brand-okh.toml`](../doqs/templates/parts-library/brand-okh.toml) | `modules/<brand>/okh.toml` |
| [`doqs/templates/parts-library/family-okh.toml`](../doqs/templates/parts-library/family-okh.toml) | `modules/<brand>/modules/<family>/okh.toml` |
| [`doqs/templates/parts-library/bom/parts.csv`](../doqs/templates/parts-library/bom/parts.csv) | `modules/<brand>/modules/<family>/bom/parts.csv` |

Do **not** copy a `LICENSE` by hand. Run `bash doqs.sh generate` from the
repository root and the licence files follow the folders you added.

The recipes -- add a brand, add a family, add a part, retire a part -- are in
[`CONTRIBUTING.md`](../CONTRIBUTING.md).
