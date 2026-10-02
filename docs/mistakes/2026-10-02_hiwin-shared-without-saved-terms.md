# 2026-10-02 — HIWIN files were shared without reading and saving the terms

## What happened

On 2026-09-21 the HIWIN catalogue and CAD files were committed to this public
library as files we may share. On 2026-10-02 the terms were read properly.
They do not allow sharing. The files had been public for eleven days, and they
stay in the history, because history here is never rewritten.

## Why it went wrong

The decision rested on a link to the terms, not on a quoted clause. Nobody
saved a copy of the terms, so nobody checked what they said. The wish to keep
a machine assembly working pushed the decision towards sharing.

## Prevention rule

Never record a `public` decision without a saved, dated copy of the terms in
`stoq-private/evidence/`, and without quoting the clause that allows sharing.
If no clause says yes, the answer is no.

## Related

- [ADR-003](../decisions/2026-10-02_hiwin-stop-sharing.md)
- [ADR-001](../decisions/2026-09-21_committing-supplier-cad.md)
- [`docs/adding-components.md`](../adding-components.md)
