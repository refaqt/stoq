# Adding a component

This is the method every person and every agent follows when adding a part
to STOQ. It makes sure of three things:

- We only publish a supplier's files when we are allowed to.
- We keep our own copy of everything, so customers can still service and
  reorder a machine after the part leaves the market.
- Anyone can check later why each decision was made.

Write in B2 English. The checks in `bash doqs.sh check` enforce part of this
method. The rest depends on you, so follow every step.

This page is a way of working, not legal advice. Ask a lawyer who knows EU
intellectual property law when a brand's terms are unclear and the part
matters.

## What you need before you start

| What | Why |
| --- | --- |
| The STEP file (or other CAD file) | The geometry |
| The datasheet, manual and technical drawings | The facts: dimensions, figures, mass |
| The terms for the CAD file | The download terms, a licence file, or the email it came with |
| The terms for the documents | Often printed in the document. If not, the website terms apply. |
| How each file reached you | A public download page, a product configurator, a quotation, an email |

If a document says nothing about its licence, look at the terms of the website
you downloaded it from. If you find nothing there either, **the answer is no**.
Silence is not permission.

A file that came with a quotation, an email or under a confidentiality
agreement (NDA) is **internal** until someone proves otherwise. Check first
whether an NDA covers it.

## The steps

### 1. Record the facts

Facts are ours, whatever the terms say. Record them first.

- One row in `bom/parts.csv`: part number, description, the figures that matter
  for choosing it, mass, revision, `status = "active"`.
- One row in `vendor-index.csv` for every file: address, checksum (sha256), size
  and date. Leave the address empty if the file has no public address.

### 2. Keep a private copy of everything

Put every original file in
[`refaqt/stoq-private`](https://github.com/refaqt/stoq-private), at **the same
path** it has, or would have, in STOQ. For example:

```
stoq-private/modules/thk/modules/shs-rail/cad/original/SHS20R300.step
stoq-private/modules/thk/modules/shs-rail/docs/datasheets/shs-series.pdf
```

Do this even when the files may be published. A brand can remove a download at
any time. Never overwrite a file in `stoq-private`: a changed file is a new row
with a new checksum.

### 3. Save the terms

Save a dated copy (PDF) of each terms page, licence file or email in
`stoq-private/evidence/<brand>/`, for example
`evidence/thk/2026-09-29_cad-download-terms.pdf`. Terms change. The copy shows
what was true on the day of the decision.

### 4. Answer four questions, for each kind of file

Do this separately for the **CAD files** and for the **documentation**. A
brand often allows one and not the other.

1. May we **publish** it, for anyone?
2. May we give copies to our **customers**?
3. May we **keep** a copy for ourselves?
4. May we make **derived files**, such as a FreeCAD document built from their STEP?

If the terms do not clearly say yes, the answer is no.

### 5. Record the decision

Add one `[[terms-review]]` entry for each kind of file to the brand's
`modules/<brand>/okh.toml`:

```toml
[[terms-review]]
kind     = "cad"            # cad | documentation
decision = "internal"       # public | customers | internal
basis    = "terms"          # terms | permission | none
source   = "https://www.thk.com/terms"
evidence = "evidence/thk/2026-09-29_cad-download-terms.pdf"
reviewer = "First Last"
reviewed = 2026-09-29
```

| `decision` | Means |
| --- | --- |
| `public` | Question 1 is yes. We may commit the files to STOQ. |
| `customers` | Question 2 is yes, question 1 is no. Files stay in `stoq-private`, and go to customers from there. |
| `internal` | Only question 3 is yes. Files stay in `stoq-private`, for our own use. |

Set `redistribute` in `[brand]` to `true` only when the newest `cad` decision is
`public`.

**A named person approves every decision.** An agent may read the terms and
propose an entry. The person named in `reviewer` approves the pull request.
Never edit or delete an entry. When terms change, add a new entry. The newest
one for each kind is the one that counts.

### 6. Choose a route

Choose one route for each kind of file.

#### Route A — Sharing is allowed

The decision is `public`, with `basis = "terms"`.

- Commit the files to STOQ. Set `terms = "redistributable"` in both tables.
- Build `cad/parts/<pn>.FCStd` from the STEP only if question 4 is also yes.

#### Route B — Ask for written permission

Use this when the terms say no or say nothing, and the part matters.

1. Send the email at the end of this page.
2. Save the reply, as a PDF, in `stoq-private/evidence/<brand>/`.
3. If the answer is yes, add a new review with `basis = "permission"` and
   `evidence` set to the path of the saved reply. Then follow Route A.
4. While you wait, keep the files out of git (step 7) and use Route C if the
   machine needs the geometry now.

#### Route C — Draw our own model from the datasheet

Use this when we may not share the brand's CAD file. Dimensions are facts, so a
model built from them is our work. It lives in `cad/own/` and carries our
licence, CC BY-SA 4.0.

Follow these rules. They keep the model clean.

1. **Build from the datasheet only.** The person or agent who builds the model
   never opens the brand's CAD file.
2. **Leave out what the datasheet does not show.** The outer shape and the
   mounting interface are what a machine design needs. Gaps are fine.
3. **No logos and no brand text.** Those are trademarks.
4. **Write the check list.** `cad/own/<pn>.checks.csv` lists every dimension,
   its value, the datasheet file and page it came from, and the result.
   The template is `doqs/templates/parts-library/cad/own/checks.csv`.
5. **Compare separately, and write only pass or fail.** A separate step compares
   each listed dimension with the brand's file. It writes `pass`, `fail` or
   `not-confirmed`, never the brand's value.
6. **On a fail, go back to the drawing.** Read the drawing again. If it is
   unclear, or the drawing and the brand's file really differ, mark the
   dimension `not-confirmed`, or ask the brand which one is right. **Never copy
   a value from the brand's file.**

In `bom/parts.csv`, the row gets `terms = "own-model"` and `cad` points to
`cad/own/<pn>.FCStd`. Run `bash doqs.sh generate` once, so `cad/own/` gets its
licence file.

### 7. Keep non-public files out of git

For every file that is not `public`:

- Set `terms = "fetch-only"` when anyone can download it from the brand, or
  `terms = "private"` when it has no public address.
- Add the exact path to `.gitignore`.

The check fails if git tracks one of these files. This matters, because history
here is never rewritten: a file that was committed once can never be taken
back.

To open models that use these files, copy them from your checkout of
`stoq-private`:

```bash
bash doqs.sh restore-private --from ../stoq-private
```

It checks each checksum before it copies anything.

### 8. Check and open a pull request

```bash
bash doqs.sh check
```

Open a pull request. Say which route you chose for each kind of file, and why.
Ask the person named in `reviewer` to approve it.

## When to check again

- When you add a new file from a brand that is already in STOQ.
- At least once a year for each brand with a `public` decision.
- When a brand, a customer or a lawyer raises a question.

If terms got stricter, add a new review, set the rows to `fetch-only` or
`private`, and stop adding files. Do not remove files that are already in the
history. See [ADR-001](decisions/2026-09-21_committing-supplier-cad.md).

## Customers

A customer may get a copy of a file from `stoq-private` only when the newest
decision for that kind of file is `public` or `customers`. The best time to get
that right is when you buy the part. Ask for this clause in the purchase terms:

> The buyer may keep the CAD files, datasheets and manuals for this product, and
> may pass them on to its customers, for the use, maintenance, repair and
> reordering of machines that contain the product, for the whole life of those
> machines.

Save the signed terms in `stoq-private/evidence/<brand>/` and record a review
with `basis = "permission"`.

## Permission request email

Copy this, fill in the parts in brackets, and send it to the brand's sales or
marketing contact.

> Subject: Permission to publish CAD files for [brand] [product series]
>
> Hello,
>
> We build open-source machines, and we use your [product series] in them. The
> designs are public, so that our customers and others can build, repair and
> maintain the machines.
>
> We would like to include your CAD files and datasheets for these parts in our
> public design files:
>
> - [part number]
> - [part number]
>
> The files would stay unchanged and would carry your name and part numbers. We
> would not claim any rights to them, and we would link to your website as the
> source.
>
> Do you allow this? If you do not allow public sharing, may we give the files
> to our own customers, for the maintenance and repair of their machines?
>
> A short written reply to this email is enough for us.
>
> Kind regards,
> [name]
> [company]

## Related

- [`CONTRIBUTING.md`](../CONTRIBUTING.md) — the other recipes
- [`doqs/docs/parts-library.md`](../doqs/docs/parts-library.md#taking-in-a-suppliers-files) — what the checks enforce
- [ADR-002](decisions/2026-09-29_component-intake.md) — why this method exists
