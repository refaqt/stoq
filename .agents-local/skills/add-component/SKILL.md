---
name: add-component
description: >-
  Add a part, a family or a brand to STOQ, with its CAD files, datasheets and
  manuals. Use whenever someone uploads or links a supplier's STEP file,
  datasheet, manual, technical drawing or licence file, asks to add a component
  to the parts library, or asks whether a supplier's file may be shared.
---

# Adding a component

The full method, for people and agents, is
[`docs/adding-components.md`](../../../docs/adding-components.md). Read it
first, and follow every step in order. This file adds the rules that apply to
you as an agent. They are hard rules. Breaking one is worse than a failing
check, because some mistakes cannot be undone: history here is never
rewritten.

## Hard rules

1. **You never decide that a file may be public.** You may read the terms and
   propose a `[[terms-review]]` entry. Write the name of the person who will
   approve it in `reviewer`, and ask that person in the pull request. If you do
   not know who that is, ask the user. Never write your own name or a tool name
   as the reviewer.
2. **When the terms are unclear, the answer is no.** Choose `internal`, keep the
   files out of git, and say what is unclear. Do not guess in favour of sharing.
3. **A file that came with a quotation, an email or an NDA is `internal`**, until
   a person shows you written permission.
4. **Never commit a file whose decision is not `public`.** Put it in
   `stoq-private` at the same path, add its exact path to `.gitignore`, and run
   `bash doqs.sh check` before every commit. The check fails if git tracks it.
5. **When you build an own model (route C), never open the brand's CAD file.**
   Work from the datasheet and drawings only. Write every dimension, with its
   file and page, in `cad/own/<pn>.checks.csv`.
6. **The comparison step writes only pass, fail or not-confirmed.** If you run
   the comparison, do it as a separate step, after the model is finished. Never
   write the brand's value anywhere, and never change the model with it. On a
   fail, read the drawing again. If the drawing is unclear, mark the dimension
   `not-confirmed` and tell the user.
7. **No logos or brand text in an own model.**
8. **Never edit or delete a `[[terms-review]]` entry, a `vendor-index.csv` row
   or a file in `stoq-private`.** Add a new one instead.

## What to report

In the pull request and in your reply, say for each kind of file (CAD,
documentation):

- which terms you read, and where the saved copy is,
- your answers to the four questions in the method,
- the decision you propose and the route you chose,
- what is still open, such as a permission request not yet sent.

Follow `.agents/rules/communication.md` and `.agents/rules/reporting.md`.
