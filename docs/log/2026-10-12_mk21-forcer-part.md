# 2026-10-12 — The MK21 forcer has a FreeCAD part

**Role(s):** mechanical engineering

## What changed

The MK21 forcer (the moving coil part of the Maxwell MK2 linear motor) now has a FreeCAD part. It
is built from the STEP file that Maxwell sent. It has one mounting frame called `IF_mount_top`.
A machine assembly can fix the forcer to its carriage with one joint on this frame.

The frame sits on the mounting face, the flat face with the six screw holes. It is on the
middle hole, halfway between the two hole rows. Its Z axis points into the forcer, towards the
coils. Its X axis runs along the forcer, the same way as on the MK2 stators.

## Why it matters

The MK2 stators already had parts with a mounting frame. With this part, both halves of the motor
can go into a machine assembly without placing anything by hand.

## Next Steps

- The six holes in the STEP file are 3 mm off the centre of the width, and 4 mm off the centre of
  the length. The data sheet drawing could not be read during this work. Check the hole pattern
  against the drawing, or ask Maxwell, before a carriage is drilled to it.
- The MK22, MK23 and MK24 forcers have no STEP file yet. Ask Maxwell for them when one is used.

<details>
<summary>Technical notes</summary>

- File: `modules/maxwell/modules/mk2-mover/cad/parts/MK21.FCStd`. It holds an `App::Part` labelled
  `MK21`, the imported shape `MK21_body` (one solid) and a `Part::LocalCoordinateSystem` labelled
  `IF_mount_top`.
- The shape keeps the STEP axes: length along X from −109 mm (cable end) to 59 mm, height along Y
  from 0 (mounting face) to 23.7 mm (coil face), width along Z from −43 to 43 mm. Stator 9.6 mm +
  forcer 23.7 mm + 0.7 mm air gap = the 34 mm installation height in the catalogue.
- Holes: 3.3 mm diameter, 6 mm deep, at x = −31, 4 and 39 mm and z = −28 and 22 mm.
- The frame is attached `FlatFace` to the part's `XY_Plane`, with offset (4, 0, −3) mm and −90°
  around X. So the frame Z axis is the part's +Y axis.
- The file was built and saved from the FreeCAD 1.1 window by a script, so it has view data
  (`GuiDocument.xml`) and opens with the part visible. The result was checked in a picture.
- This is the brand's own model, shared under the existing Maxwell decision of 2026-09-21
  (`public`, no written basis). No new terms were needed.
- `bash doqs.sh check` passes.

</details>
