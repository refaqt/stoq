# stoq: rules for this repository

STOQ is a **parts library**: a record of components that other companies
design, make and sell. Nothing here is hardware we designed. Read
[`docs/architecture.md`](../../docs/architecture.md) first, then
[`doqs/docs/parts-library.md`](../../doqs/docs/parts-library.md) for the full
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
   committed only where the brand's newest `[[terms-review]]` says `public`, and
   a named person approved it. Otherwise record it as `fetch-only` or `private`:
   address, checksum and date committed, file not. Follow
   [`docs/adding-components.md`](../../docs/adding-components.md) and the
   `add-component` skill for every supplier file.
4. **Brand is not supplier.** The folder is the brand on the part. No price and
   no distributor belongs in this repository.

Adding a brand, a family or a part: [`CONTRIBUTING.md`](../../CONTRIBUTING.md).
The folder layout, file by file: [`modules/README.md`](../../modules/README.md).

## Licensing

[`LICENSE`](../../LICENSE) says which licence applies where. It is the only full
list; do not repeat it in another file. Never hand-write a `LICENSE` or
`TRADEMARKS.md`: `bash doqs.sh generate` renders them.

Add a component with the skill `add-component` (`.agents-local/skills/add-component/SKILL.md`).
