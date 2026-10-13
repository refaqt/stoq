# 2026-10-13 — A HIWIN EG rail and QE block, with assembly frames

**Role(s):** mechanical engineering, purchasing

## What changed

Two new HIWIN parts are in the library, each in a new family:

- `egr-rail`: the EGR15R418H rail, 418 mm long. The EG rail carries both the EG and the QE blocks.
- `qeh-block`: the QEH15CAZAP+E2 block, a quiet square block with the E2 lubrication unit.

Both have the HIWIN STEP file and a FreeCAD part with mounting frames:

| Part | Frame | Where | For |
| --- | --- | --- | --- |
| Rail | `IF_mount_bottom` | Bottom face, on the first hole | Fixing the rail to the base |
| Rail | `IF_block` | Bottom centre line, at the rail start | The block |
| Block | `IF_rail` | Bottom of the rail, centre line, under the block start | Joins `IF_block` |
| Block | `IF_mount_top` | Top face, centre of the hole pattern | Fixing the carriage to the block |

On every frame the X axis runs along the rail. Z points up, except on `IF_mount_top`, where Z points
down into the block, as on the MK21 forcer.

## Why it matters

A machine assembly can put the block on the rail, the rail on a base and a carriage on the block,
with joints on frames only. A Fixed joint between `IF_block` and `IF_rail` puts the block at the
start of the rail, at the right height. To let the block move along the rail, use a Slider joint and
turn its slide axis: see the technical notes.

## Next Steps

- The block has 2 mounting holes, not the 4 in the catalogue. The E2 lifetime lubrication unit
  takes the place of one hole row, and the block has less load capacity (Niels confirmed this).
  Ask HIWIN for the load ratings of this block before a design is sized on them.
- The frames of the older HGR15 rail and HGL15 block have X across the rail, and the rail has no
  frame for the block. Give them the same frames as the new parts, if a machine needs both series.

<details>
<summary>Technical notes</summary>

- Files: `modules/hiwin/modules/egr-rail/cad/parts/EGR15R418H.FCStd` and
  `modules/hiwin/modules/qeh-block/cad/parts/QEH15CAZAP+E2.FCStd`. Each holds an `App::Part`
  labelled with the part number, the imported shape `HIWIN_<pn>` (one solid, HIWIN colours) and
  the frames as `Part::LocalCoordinateSystem`.
- The shapes keep the HIWIN axes: width along X, length along Y, height along Z, rail bottom at
  z = 0. The rail is 0…418 mm in Y, holes at y = 29 + 60·k. The block is 0…56 mm in Y and
  4…24 mm in Z (installation height 24 mm). The E2 unit is on the y = 0 end, so the body centre
  and the hole row are at y = 34.55 mm. Holes: 3.3 mm, 6 mm deep, at x = ±13 mm.
- Each frame is attached `FlatFace` to the part's `XY_Plane`. Offsets: rotation 90° around Z
  (frame X = part +Y); `IF_mount_top` also turns 180° around its X axis.
- Slider joint: FreeCAD 1.1 slides along the Z axis of the joint. Set `Offset1` and `Offset2` of the
  joint to a rotation of 90° around Y. The joint then slides along the frame X axis, along the rail.
  Tested in a scratch assembly: the block stayed on the rail at y = 100 and y = 250 mm.
- The files were built by a script in the FreeCAD 1.1 window and saved there, so they have view
  data. `doqs wrap` was tried first; its job stopped in the FreeCAD window, so the same steps were
  run directly.
- `doqs add-part` took the files into both libraries. Three of its results were corrected by hand:
  the date is now the STEP header time (it wrote the copy time); the private library keeps its own
  brand decision (the tool added a `public` review and set `redistribute = true` there); and the
  private rows are `internal`, like the other HIWIN rows there.
- Terms: the newest HIWIN decision (2026-10-06, `public`, basis `none`, Niels Bosmans) covers these
  files. No new decision was made.
- Mass: rail 1.25 kg/m × 0.418 m = 523 g; block 0.15 kg, from catalogue tables 3.45 and 3.47.
- `bash doqs.sh check` passes.

</details>
