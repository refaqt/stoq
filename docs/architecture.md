# Architecture

Short map of this repository. Update when the layout, start points, or main parts change.
Write this file in B2 English. Follow `.agents/rules/communication.md`.

## Purpose

STOQ is a **parts library**: a record of components that other companies
design, make and sell. We design nothing here. We write down what we found out
about a part, so that no two Refaqt projects research the same rail twice.

A machine repository mounts this repository under `modules/` and refers to a
part by name. The full specification is
[`doqs/docs/parts-library.md`](../doqs/docs/parts-library.md); the reasoning is
in [ADR-004](../doqs/docs/decisions/2026-09-18_parts-library.md).

## Repository layout

| Path | Role |
| ---- | ---- |
| `library.toml` | The marker. It is what makes this repository a parts library. |
| `okh.toml` | The root manifest. Its licence must be `CC-BY-SA-4.0`. |
| `modules/` | One folder per brand, then one per family. See [`modules/README.md`](../modules/README.md). |
| `docs/` | This map, onboarding, and the living docs below. |
| `docs/decisions/` | Why a choice was made. |
| `docs/log/` | A day's work write-up. |
| `docs/mistakes/` | Something that went wrong. Read before starting work. |
| `LICENSE`, `LICENSES/`, `TRADEMARKS.md` | Who may use what. `LICENSE` is the only full list. |
| `doqs/` | Submodule: the validators, schemas and templates. |
| `.agents/` | Submodule: shared agent rules and skills. |
| `doqs.sh`, `doqs.bat`, `syson.sh`, `syson.bat` | Launchers doqs installs. Never edit them here. |

## Three levels, two of them folders

| Level | Where | What it is |
| --- | --- | --- |
| Brand | `modules/hiwin/` | The name on the part. Stable for decades. |
| Family | `modules/hiwin/modules/hgr-rail/` | One product range. **This is the module.** |
| Part | a row in `bom/parts.csv` | One orderable part number. Not a folder. |

A machine buys hundreds of part numbers. A folder each does not scale.

## How a machine uses this repository

```bash
git submodule add https://github.com/refaqt/stoq modules/stoq
```

A machine then names a part in one cell of a bill of materials
(`stoq:din/din-912#M4X10`), or through a role module when the part has
requirements. The machine's own checks skip this whole checkout: it is
validated here, and a machine should not re-run hundreds of supplier checks on
every commit.

## Two rules that shape everything else

**Nothing is ever removed.** A machine built in 2026 still points at the part
row it was built from. A part you can no longer buy gets `status = "eol"`; the
row stays. History is never rewritten: no squash and no force-push on `main`,
or every build record that points here breaks.

**Store the link, not the file.** Part numbers, dimensions and specifications
are facts we compile, and they are the bulk of the value. A supplier's own CAD
file or datasheet is committed only where that brand's terms allow it.
Everything else is recorded as `fetch-only`: the address, the checksum and the
date are committed, and each person downloads the file from the brand.
