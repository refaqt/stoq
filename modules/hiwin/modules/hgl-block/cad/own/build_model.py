"""Our own HGL15CA low square block, drawn from the catalogue only.

Source: linear guideways catalogue GW-13-1-EN-2606-K, page 41 (table 3.7 and
the figure), page 43 (rail) and page 47 (E2 unit). The brand's CAD file was
not used. Values named est_* in params.csv are read from the figure, which is
drawn for size 25, and scaled to size 15: they are estimates. Rebuild headless:

    "C:\\Program Files\\FreeCAD 1.1\\bin\\freecadcmd.exe" build_model.py

Axes, the same as our rail model and the HIWIN model:
- Y runs along the rail. The end face of the grease nipple end is at Y = 0,
  the other end face at Y = L.
- Z is up. The rail bottom is at Z = 0.
- X runs across. The rail centre is at X = 0. The reference edge is on the -X
  side: seen from the nipple end, it is on the left, as in the catalogue's
  front view.

What is in the model:
- Steel body (length L1) with the reference edge band (height T) on -X, the
  side below the band set back, and top and bottom chamfers.
- End caps with end seals at both ends (together (L - L1) / 2 each), a little
  narrower and lower than the body.
- Grease nipple envelope (length G, axis H2 below the top) at the Y = 0 end.
- End seal screw heads on both end faces.
- Lubrication ports: on top of each end cap (K1 from the hole centre) and on
  both sides of each end cap (K2 from the steel body, H3 below the top).
- Four M4 holes (tap drill size, depth l). The thread is not modelled.

What is left out: the ball grooves and the lips inside the rail channel (the
channel is the rail's WR x HR envelope), the hex shape of the nipple (it is a
cylinder around the hex corners), and the inside of the ports.
"""

import sys
from pathlib import Path

try:
    _HERE = Path(__file__).resolve().parent
except NameError:  # exec()'d from the FreeCAD console
    _HERE = Path.cwd()


def _doqs_scripts(start):
    for base in [start, *start.parents]:
        candidate = base / "doqs" / "scripts"
        if (candidate / "cad_build.py").is_file():
            return candidate
    raise RuntimeError(f"doqs/scripts/cad_build.py not found above {start}")


sys.path.insert(0, str(_doqs_scripts(_HERE)))

from cad_build import body, run  # noqa: E402


def _clear(doc):
    """The .FCStd is generated output: rebuild it from nothing every time."""
    while doc.Objects:
        top = [o for o in doc.Objects if not o.InList] or doc.Objects
        for obj in top:
            if hasattr(obj, "removeObjectsFromDocument"):
                obj.removeObjectsFromDocument()
            if obj.isValid() and doc.getObject(obj.Name):
                doc.removeObject(obj.Name)


def _params_sheet(doc, params):
    sheet = doc.addObject("Spreadsheet::Sheet", "Params")
    sheet.set("A1", "alias")
    sheet.set("B1", "value")
    row = 2
    for alias, value in params.items():
        sheet.set(f"A{row}", alias)
        sheet.set(f"B{row}", str(value))
        sheet.setAlias(f"B{row}", alias)
        row += 1
    sheet.set(f"A{row + 1}", "Source: linear guideways catalogue GW-13-1-EN-2606-K, pages 41, 43 "
              "and 47. est_* values are estimates. Change values in params.csv and rebuild.")
    return sheet


def _profile_pad(shape, name, points_xz, y_start, length):
    """Pad a closed X-Z polygon along +Y, from y_start over length."""
    import FreeCAD as App
    import Part

    sketch = shape.newObject("Sketcher::SketchObject", f"{name}Profile")
    # Sketch x -> X, sketch y -> Z. The sketch normal is then -Y.
    sketch.Placement = App.Placement(
        App.Vector(0, y_start, 0), App.Rotation(App.Vector(1, 0, 0), 90))
    pts = [App.Vector(x, z, 0) for x, z in points_xz]
    for a, b in zip(pts, pts[1:] + pts[:1]):
        sketch.addGeometry(Part.LineSegment(a, b))
    sketch.Visibility = False
    pad = shape.newObject("PartDesign::Pad", name)
    pad.Profile = sketch
    pad.Length = length
    pad.Reversed = True  # along +Y
    return pad


def _cylinder(shape, name, radius, height, base, axis, subtract=False):
    """A cylinder from `base` along `axis` ("+X", "-X", "+Y", "-Y", "-Z")."""
    import FreeCAD as App

    kind = "PartDesign::SubtractiveCylinder" if subtract else "PartDesign::AdditiveCylinder"
    cyl = shape.newObject(kind, name)
    cyl.Radius = radius
    cyl.Height = height
    rotation = {
        "+X": App.Rotation(App.Vector(0, 1, 0), 90),
        "-X": App.Rotation(App.Vector(0, 1, 0), -90),
        "+Y": App.Rotation(App.Vector(1, 0, 0), -90),
        "-Y": App.Rotation(App.Vector(1, 0, 0), 90),
        "-Z": App.Rotation(App.Vector(1, 0, 0), 180),
    }[axis]
    cyl.Placement = App.Placement(App.Vector(*base), rotation)
    return cyl


def build(doc, params):
    p = params
    _clear(doc)
    _params_sheet(doc, p)
    doc.recompute()
    shape = body(doc)
    features = []

    # Across: the reference edge is at -(N + WR/2); W is measured over it.
    x_ref = -(p["N_ref"] + p["WR"] / 2)
    x_far = x_ref + p["W_blk"]
    z_bot, z_top = p["H1_gap"], p["H_inst"]
    z_band = z_top - p["T_ref"]
    relief = p["est_ref_relief"]
    cbx, cbz = p["est_chamfer_bot_x"], p["est_chamfer_bot_z"]
    ctr, ctf = p["est_chamfer_top_ref"], p["est_chamfer_top_far"]
    x_low = x_ref + relief  # reference side below the band

    # Along: end caps (with seals) at both ends, steel body in the middle.
    length = p["L_blk"]
    cap = (p["L_blk"] - p["L1_body"]) / 2

    body_profile = [
        (x_low + cbx, z_bot), (x_far - cbx, z_bot), (x_far, z_bot + cbz),
        (x_far, z_top - ctf), (x_far - ctf, z_top), (x_ref + ctr, z_top),
        (x_ref, z_top - ctr), (x_ref, z_band), (x_low, z_band),
        (x_low, z_bot + cbz),
    ]
    features.append(_profile_pad(shape, "SteelBody", body_profile, cap, p["L1_body"]))

    inset, drop, cc = p["est_cap_inset"], p["est_cap_drop"], p["est_cap_chamfer"]
    xl, xr, zt = x_low + inset, x_far - inset, z_top - drop
    cap_profile = [
        (xl + cc, z_bot), (xr - cc, z_bot), (xr, z_bot + cc), (xr, zt - cc),
        (xr - cc, zt), (xl + cc, zt), (xl, zt - cc), (xl, z_bot + cc),
    ]
    features.append(_profile_pad(shape, "EndCapNipple", cap_profile, 0, cap))
    features.append(_profile_pad(shape, "EndCapFar", cap_profile, length - cap, cap))

    if int(p.get("E2_units", 0)) >= 1:
        t_e2 = p["Lss_E2"] - p["L_blk"]
        half = p["W_E2"] / 2
        e2_profile = [(-half, z_bot), (half, z_bot), (half, z_bot + p["H_E2"]),
                      (-half, z_bot + p["H_E2"])]
        features.append(_profile_pad(shape, "E2Unit", e2_profile, -t_e2, t_e2))
        nipple_face = -t_e2
    else:
        nipple_face = 0.0

    # Rail channel: the rail envelope, through everything.
    channel = shape.newObject("PartDesign::SubtractiveBox", "RailChannel")
    channel.Length, channel.Width, channel.Height = p["WR"], length + 40, p["HR"]
    import FreeCAD as App
    channel.Placement = App.Placement(App.Vector(-p["WR"] / 2, -20, 0), App.Rotation())
    features.append(channel)

    # Grease nipple envelope at the Y = 0 end.
    z_nipple = z_top - p["H2_nipple"]
    features.append(_cylinder(shape, "GreaseNipple", p["est_nipple_dia"] / 2, p["G_nipple"],
                              (0, nipple_face, z_nipple), "-Y"))

    # End seal screw heads on both end faces.
    r_screw, proud = p["est_screw_dia"] / 2, p["est_screw_proud"]
    for i, sx in enumerate((-1, 1), start=1):
        x = sx * p["est_screw_x"]
        features.append(_cylinder(shape, f"SealScrewNipple{i}", r_screw, proud,
                                  (x, 0, p["est_screw_z"]), "-Y"))
        features.append(_cylinder(shape, f"SealScrewFar{i}", r_screw, proud,
                                  (x, length, p["est_screw_z"]), "+Y"))

    # Four M4 holes in the steel body top.
    for i, (sx, sy) in enumerate([(1, 1), (1, -1), (-1, 1), (-1, -1)], start=1):
        features.append(_cylinder(
            shape, f"Thread{i}", p["M_tap"] / 2, p["l_thread"],
            (sx * p["B_holes"] / 2, length / 2 + sy * p["C_holes"] / 2, z_top), "-Z",
            subtract=True))

    # Lubrication ports on the end caps: on top (K1 from the hole centre) and on
    # both sides (K2 from the steel body, H3 below the top).
    r_port, depth = p["est_port_dia"] / 2, p["est_port_depth"]
    y_top_ports = (length / 2 - p["C_holes"] / 2 - p["K1_port"],
                   length / 2 + p["C_holes"] / 2 + p["K1_port"])
    for i, y in enumerate(y_top_ports, start=1):
        features.append(_cylinder(shape, f"TopPort{i}", r_port, depth, (0, y, zt), "-Z",
                                  subtract=True))
    y_side_ports = (cap - p["K2_port"], length - cap + p["K2_port"])
    z_port = z_top - p["H3_port"]
    for i, y in enumerate(y_side_ports, start=1):
        features.append(_cylinder(shape, f"SidePortRef{i}", r_port, depth, (xl, y, z_port),
                                  "+X", subtract=True))
        features.append(_cylinder(shape, f"SidePortFar{i}", r_port, depth, (xr, y, z_port),
                                  "-X", subtract=True))

    shape.Tip = features[-1]
    for feature in features[:-1]:
        feature.Visibility = False
    features[-1].Visibility = True


# FreeCADCmd 1.1 runs a script under its file name, not "__main__".
if __name__ in ("__main__", "build_model"):
    run(build, cad_dir=_HERE)
