# STOQ

Components bought from third-party suppliers, recorded once and read by every
project.

STOQ is a **parts library**. It holds parts that other companies design, make
and sell. We design nothing here. What is ours is the record we compile: the
part numbers, the dimensions, the specifications, and where each file came
from.

A HIWIN rail belongs to no single machine. Without this repository, every
project that buys the same rail repeats the same work: find the part, download
the file, record where it came from, write the table row. Here that work is
done once.

## Use it in a machine

```bash
git submodule add https://github.com/refaqt/stoq modules/stoq
```

Your own checks skip this whole checkout. It is validated in its own
repository, and a machine should not re-run hundreds of supplier checks on
every commit.

**An ordinary part is one extra cell** on a row you already write. No folder,
no generated file:

```csv
id,name,spec,category,qty,unit,unit_mass_g,equiv_class,brand,brand_pn,part,notes
STD-004,Cap Screw,DIN912 M4x10 A2-70,fastener,8,pc,2,M4X10-SHCS,DIN,M4X10,stoq:din/din-912#M4X10,
```

The reference is `<library>:<brand>/<family>#<part number>`. Validation checks
that it resolves, that the part is still sold, and that it agrees with the
brand and part number you wrote beside it.

**A part with requirements gets a role module** instead: a folder named after
the job, holding the requirements and one line saying what fills that job
today. Changing brand is then one line of text. See
[`doqs/docs/roles.md`](doqs/docs/roles.md).

## How it is organised

| Level | Where | What it is |
| --- | --- | --- |
| Brand | `modules/hiwin/` | The name on the part. Stable for decades. |
| Family | `modules/hiwin/modules/hgr-rail/` | One product range. **This is the module.** |
| Part | a row in `bom/parts.csv` | One orderable part number. Not a folder. |

Brand is not supplier. HIWIN is the brand: on the part, in the part number,
unchanging. Where you buy it is commercial, changes often, and is not recorded
here. [`modules/README.md`](modules/README.md) has the full layout.

## Two rules

**Nothing is ever removed.** A machine built years ago still points at the row
it was built from. A part you can no longer buy gets `status = "eol"`, which
stops new designs choosing it; the row stays. History is never rewritten --
a squash or a force-push on `main` breaks every build record that points here.

**Store the link, not the file.** Facts we compiled are committed. A supplier's
own CAD file or datasheet is committed only where that brand's terms allow it.
Everything else is `fetch-only`: the address, the checksum and the date are
committed, and each person downloads the file from the brand under the brand's
terms.

## Working here

```bash
git clone --recurse-submodules https://github.com/refaqt/stoq
bash setup-tooling.sh     # fills doqs/ and .agents/, installs the launchers
bash doqs.sh check        # every gate
```

[`docs/onboarding.md`](docs/onboarding.md) is the longer version, and
[`CONTRIBUTING.md`](CONTRIBUTING.md) has the recipes for adding a brand, a
family or a part.

## Licence

The record we compile is **CC BY-SA 4.0**. Supplier files under any `cad/` or
`docs/datasheets/` directory keep their own terms and are **not** covered by
it. There is deliberately no CERN Open Hardware Licence here: nothing in this
repository is hardware we designed.

[`LICENSE`](LICENSE) is the only full list; it says which licence applies
where. Reserved marks are in [`TRADEMARKS.md`](TRADEMARKS.md).
