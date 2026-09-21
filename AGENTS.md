# Agent guide

Start here if you are an agent (Cursor, Claude Code, or similar) working in this repository.

## First step (required)

Before you read `.agents/` rules or skills, update the tooling submodules to the latest `main`:

- **All agents, any OS:** `bash setup-tooling.sh`. This repository has a `doqs`
  submodule, so that is the file to run. There is no `setup-agents.sh` here.
- **People on Windows** may double-click `setup-tooling.bat` (`pause` is OK there only). Agents must not run the `.bat`.

A `SessionStart` hook at [`.claude/hooks/session-start.sh`](.claude/hooks/session-start.sh) usually
fills those folders before you read this. Run the setup file anyway when you need the launchers it
installs, or when the hook said it could not reach the network. Both leave the submodule gitlinks
modified on purpose — leave them uncommitted unless you mean to set a new pin.

## Shared kit

This repo mounts [refaqt/refaqt-agents](https://github.com/refaqt/refaqt-agents) at [`.agents/`](.agents/).

1. Read [`.agents/rules/core.md`](.agents/rules/core.md), [`.agents/rules/communication.md`](.agents/rules/communication.md), [`.agents/rules/reporting.md`](.agents/rules/reporting.md), and [`.agents/rules/living-docs.md`](.agents/rules/living-docs.md).
2. Read [`docs/mistakes/`](docs/mistakes/) and say which prevention rules apply.
3. Read [`docs/architecture.md`](docs/architecture.md) before larger work.
4. Before new coding solutions, check `.agents-local/skills/patterns/SKILL.md` if it is there.

Write every reply and every file in B2 English. Follow `.agents/rules/communication.md`.
Write pull requests, commit messages, GitHub comments, issues, and log entries for a manager, not
for a developer. Follow `.agents/rules/reporting.md`.

## This repository

STOQ is a **parts library**: a record of components that other companies
design, make and sell. Nothing here is hardware we designed. Read
[`docs/architecture.md`](docs/architecture.md) first, then
[`doqs/docs/parts-library.md`](doqs/docs/parts-library.md) for the full
specification.

**Validate with `bash doqs.sh check`** from the repository root, before every
commit. It runs every gate. `bash doqs.sh generate` writes the generated
licence files after you add a content folder; read the diff before committing
it.

Four rules that are specific to this repository. Breaking any of them is worse
than a failing check, because a check cannot catch them:

1. **Nothing is ever removed.** A part you can no longer buy gets
   `status = "eol"`. Never delete the row and never delete the file: a machine
   in the field is still made of it.
2. **History is never rewritten.** No squash and no force-push on `main`.
   Build records in machine repositories point at commits here.
3. **Store the link, not the file.** A supplier's CAD file or datasheet is
   committed only where that brand's terms allow it. Otherwise record it as
   `fetch-only`: address, checksum and date committed, file not.
4. **Brand is not supplier.** The folder is the brand on the part. No price and
   no distributor belongs in this repository.

Adding a brand, a family or a part: [`CONTRIBUTING.md`](CONTRIBUTING.md).
The folder layout, file by file: [`modules/README.md`](modules/README.md).

Every task that changes this repository starts on a **new git branch** off
`main`, unless the user says otherwise.

| You are adding | It goes in |
| --- | --- |
| A day's work write-up | `docs/log/YYYY-MM-DD_topic.md` |
| Why a choice was made | `docs/decisions/YYYY-MM-DD_topic.md` |
| Something that went wrong | `docs/mistakes/YYYY-MM-DD_topic.md` |

Each of those folders has a `README.md` index. Update the index when you add a
file. Skills that belong only to this repo go in `.agents-local/skills/`, never
inside the `.agents/` submodule: anything written there is lost on the next
update.

## Licensing

[`LICENSE`](LICENSE) says which licence applies where. It is the only full
list; do not repeat it in another file. Never hand-write a `LICENSE` or
`TRADEMARKS.md`: `bash doqs.sh generate` renders them.

## Skills

| Skill | Path |
| --- | --- |
| Activity log | `.agents/skills/log/SKILL.md` |
| Mistake log | `.agents/skills/mistake-log/SKILL.md` |
| Maintain patterns | `.agents/skills/maintain-patterns/SKILL.md` |
| DOQS naming | `.agents/skills/doqs-naming/SKILL.md` |
| FreeCAD debugging | `.agents/skills/freecad/SKILL.md` |

Role skills are at `.agents/skills/{category}/{skill-name}/SKILL.md`. The two
that come up most here are `.agents/skills/business/purchasing/SKILL.md` and
`.agents/skills/supply-chain/supply-chain-management/SKILL.md`.

Using Cursor: copy [`.agents/templates/cursor-rule-doqs-naming.mdc`](.agents/templates/cursor-rule-doqs-naming.mdc)
and [`.agents/templates/cursor-rule-freecad.mdc`](.agents/templates/cursor-rule-freecad.mdc)
to `.cursor/rules/`.
