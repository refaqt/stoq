# 2026-10-02 — Our own HIWIN models were wrong, and the checks said they passed

## What happened

The first own models of the HGR15 rail and the HGL15 block were built from the
catalogue, but they did not match the real part:

- The block had the E2 lubrication unit on one end, so it was 14 mm too long
  and not symmetric. The HIWIN file for this part number has no such unit.
- Both models ran along a different axis than the HIWIN models, and the block
  was centred on its length instead of starting at 0. Put in the same place as
  the old models, they looked wrong.
- The models were made by hand in the FreeCAD window. There was no build
  script to review.
- The first comparison left out the end seals and still called the block
  length a pass. Its measuring scripts were saved in the builder's own work
  folder, where the builder could read the HIWIN values.
- The HIWIN files were taken out of git but left in the person's folder, and
  the report did not say so.

## Why it went wrong

- The builder treated "the values are from the catalogue" as "the model is
  right", and nobody looked at the result next to the real part.
- A catalogue drawing of an option (E2) was read as the standard shape.
- Placement and axes were chosen freely. Nothing says an own model must sit
  where the brand model sits.
- A "pass" was accepted without asking how it was measured.
- The doqs build-script method was not used, and the doqs CAD check skips a
  parts library completely, so nothing asked for it. The doqs template's
  headless rebuild also does nothing in FreeCAD 1.1, because FreeCAD does not
  run the script as `__main__`.

## Prevention rule

- Build every own model from a committed `cad/own/build_model.py` and
  `params.csv`, rebuilt headless, with its fingerprint committed.
- Use the brand model's axes and origin, so our model can replace it in an
  assembly. Say in the build script which axes are used.
- Before a model is called done, check it in a picture or with a slice, and
  check symmetry where the part is symmetric.
- An option (such as E2) is a parameter, not part of the base shape, until the
  brand confirms it.
- The comparison works in its own folder, measures exactly what the catalogue
  defines, and says how it measured each "pass". Read that before you accept it.
- When files leave git, say whether they are still on disk.

## Related

- [2026-10-02_hiwin-shared-without-saved-terms.md](2026-10-02_hiwin-shared-without-saved-terms.md)
- [ADR-003](../decisions/2026-10-02_hiwin-stop-sharing.md)
