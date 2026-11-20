# 2026-11-20 — The Agito AGD155 and AGD156 servo drives are in the library

**Role(s):** electrical engineering, purchasing, legal

## What changed

The library now has the brand Agito, with two servo drive families: AGD155
(four part numbers) and AGD156 (one part number). Each row holds the main
figures from the product manual: current, supply, encoder types, inputs and
outputs, size and mass. The notes add the answers Akribis gave to our
technical questions, and the encoder pinout we need for our own cable.

The manuals came by email with a request for quote, and each one says "All
rights reserved". So the decision is `internal` and the rows are `private`.
The manuals are not in this repository. They are in `stoq-private`, at the
same paths, with a dated copy of the email.

## Why it matters

We are choosing a servo drive for the linear motor stage. The machine designs
can now point at these parts.

## Next Steps

- Niels Bosmans approves the `internal` decision in the pull request.
- Ask Akribis about the open points. The list is in
  `modules/agito/docs/drive-questions.md` in `stoq-private`.

## Related

- [docs/adding-components.md](../adding-components.md)
