# 2026-10-28 — Mounting frames are hidden in every part

**Role(s):** mechanical engineering

## What changed

Every mounting frame in the library is now saved hidden. That is 26 frames in 15
part files, both supplier parts and our own models. The shapes did not change.

## Why it matters

The aqtuator compact stage showed the frames of every linked part. They covered
the parts and made the assembly hard to read. Now the assembly shows only the
parts. Joints still use the frames.

## Next Steps

- Open the compact stage in the FreeCAD window after this change is merged, and
  check that no frame shows. This was not checked in the window here.
- A new frame still opens visible. Hide it before you commit the part. See
  [ADR-005](../decisions/2026-10-28_mounting-frames-hidden.md).

<details>
<summary>Technical notes</summary>

- In each `.FCStd`, `Visibility` of every `Part::LocalCoordinateSystem` with a
  label that starts with `IF_` is set to `false`, in `Document.xml` and in
  `GuiDocument.xml`. Only the frame object is hidden, the way the space bar
  hides it. Its axes and planes keep their own setting, so showing the frame
  again shows them too.
- Every other byte of the files is the same. The archives were rewritten with
  the same entry order and compression.
- Three files have no frames: our own HIWIN rail and block models, and the
  MAXWELL WJM050-3 forcer. They did not change.
- The four own models (ALZ00270G, RUS-ET-A-B, MB-MC15-MK-ML220,
  MB-MC15-MK-ML240) store a checksum of their file in the fingerprint. Only that
  checksum was updated. The measured shapes in the fingerprint are the same,
  because frames are not measured.
- `bash doqs.sh check` passes. FreeCAD is not installed in this environment, so
  no file was opened in the FreeCAD window.

</details>
