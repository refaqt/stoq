# Onboarding

How to set up, run, and find your way around this repository.
Write this file in B2 English. Follow `.agents/rules/communication.md`.

## Prerequisites

- Git, with access to [refaqt/doqs](https://github.com/refaqt/doqs) and
  [refaqt/refaqt-agents](https://github.com/refaqt/refaqt-agents). Both are public.
- Python 3.12 or newer. The checks use the standard library only, so there is
  nothing to install.
- FreeCAD, only if you will build a `.FCStd` document from a supplier's model.

## Setup

1. Clone the repository with its submodules:

   ```bash
   git clone --recurse-submodules https://github.com/refaqt/stoq
   ```

2. From the repository root, run the helper:

   ```bash
   bash setup-tooling.sh
   ```

   It fills `doqs/` and `.agents/` and installs the launchers. People on
   Windows may double-click `setup-tooling.bat`. Agents must not: it waits for
   a key press.

3. Check that everything is in place:

   ```bash
   bash doqs.sh check
   ```

`git status` showing `doqs` and `.agents` as modified after the helper is
normal. Leave them uncommitted unless you mean to set a new pin.

## Everyday commands

| Command | When |
| --- | --- |
| `bash doqs.sh check` | Before every commit. Runs every gate. |
| `bash doqs.sh generate` | After adding a content folder, so the licence files follow. |
| `bash doqs.sh list` | When you forget a command. |

## Where to read next

| Doc | Use |
| --- | --- |
| [`CONTRIBUTING.md`](../CONTRIBUTING.md) | Adding a brand, a family, a part; retiring a part |
| [`docs/architecture.md`](architecture.md) | Repository map and the brand/family/part grammar |
| [`modules/README.md`](../modules/README.md) | The folder layout of a family, file by file |
| [`doqs/docs/parts-library.md`](../doqs/docs/parts-library.md) | The full specification |
| [`doqs/docs/naming.md`](../doqs/docs/naming.md) | Naming rules |
| [`doqs/docs/roles.md`](../doqs/docs/roles.md) | Buying a part into a machine |
| `docs/decisions/` | Why past choices were made |
| `docs/mistakes/` | What went wrong and how to avoid it |
| `docs/log/` | Date-ordered activity log |
| `.agents/` | Shared agent rules and skills |

## Cursor / Agent

Root [`AGENTS.md`](../AGENTS.md) is the start file. Shared rules and skills
live in `.agents/`. Skills that belong only to this repository go in
`.agents-local/skills/`, never inside the submodule.
