# 2026-10-07 — The MK2 stators have a mounting frame

**Role(s):** mechanical engineering

## What changed

The MK2-180 and MK2-120 stators (the magnet tracks of the Maxwell linear motor) now each have a
mounting frame called `IF_mount_bottom`. A machine assembly can now fix a stator to its base with
one joint on this frame. It does not need a face or an edge of the supplier shape.

The frame sits on the bottom face of the stator, on the first mounting hole at the N end, halfway
between the two hole rows. Its Z axis points up, into the stator, towards the magnets. Its X axis
runs along the stator. This is the same layout as the frame on the HIWIN rail.

## Why it matters

AQTUATOR puts two MK2-180 stators into the compact stage. Without a frame, the stators could only
be placed by hand or on supplier faces, which break when the model changes.

## Next Steps

- Give the MK2-300 stator a FreeCAD part with the same frame when it is first used.
- The parts table says "one 120 mm hole pitch" for the MK2-120 and "two 120 mm hole pitches" for
  the MK2-180. The STEP files have 60 mm between holes. Check the table against the data sheet.

<details>
<summary>Technical notes</summary>

- The frame is a `Part::LocalCoordinateSystem` inside the `Part` container, attached `FlatFace` to
  the part's `XY_Plane`. The attachment offset turns it −90° around X, so the frame Z axis is the
  part's +Y axis (the part's bottom face is at y = 0, the magnets at y = 9.6).
- The x position is an expression: `-0.78 - (holes - 1) * 60 / 2`, with 3 holes per row for the
  MK2-180 and 2 for the MK2-120. That gives x = −60.78 mm and x = −30.78 mm, the first hole axis in
  the STEP shape. The STEP hole pattern sits 0.78 mm off the centre of the envelope, towards the N
  end. The catalogue gives 30.6 mm from the end to the first hole, which matches.
- The hole rows are at z = ±37 mm (74 mm apart in the catalogue). The frame is at z = 0.
- The frames were added with `freecadcmd`. These files have never had colour data
  (no `GuiDocument.xml`), so nothing was lost by working without the window.
- `bash doqs.sh check` passes.

</details>
