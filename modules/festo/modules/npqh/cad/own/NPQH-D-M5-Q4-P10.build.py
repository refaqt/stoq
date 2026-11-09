"""Our own model of the Festo push-in fitting NPQH-D-M5-Q4-P10 (578334).

Sizes from the Festo NPQH catalogue, page 5, "male thread, with external hex",
and the data sheet 578334. The lengths of the hex and the release ring are not
in the catalogue: they are estimates, marked as such in the params file. All
values are in `NPQH-D-M5-Q4-P10.params.csv`. Rebuild headless from the
library root with

    FreeCADCmd modules/festo/modules/npqh/cad/own/NPQH-D-M5-Q4-P10.build.py

Axes: Z along the fitting, from the sealing face under the hex (Z = 0) towards
the tubing end. The thread points to -Z. The origin is on the axis, on the
sealing face.
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

from cad_build import bind, body, frame, main  # noqa: E402

#: The axes and origin of this model.
AXES = "Z along the fitting from the sealing face under the hex (Z = 0) towards the tubing end; the thread points to -Z; origin on the axis on the sealing face."

DERIVED = [('r_thread', '=fit_d1 / 2', 'Radius of the M5 thread (major diameter)'),
    ('r_hex', '=fit_hex_af / sqrt(3)', 'Corner radius of the hex'),
    ('r_d6', '=fit_d6 / 2', 'Radius of the body'),
    ('r_d5', '=fit_d5 / 2', 'Radius of the release ring'),
    ('r_bore', '=fit_bore / 2', 'Radius of the bore'),
    ('r_tube', '=fit_tube_od / 2', 'Radius of the tubing seat'),
    ('body_h', '=fit_l1 - fit_l2 - fit_hex_h - fit_ring_h', 'Length of the body between hex and release ring')]


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
    sheet.set("C1", "note")
    row = 2
    for alias, value in params.items():
        sheet.set(f"A{row}", alias)
        sheet.set(f"B{row}", str(value))
        sheet.setAlias(f"B{row}", alias)
        row += 1
    for alias, expr, note in DERIVED:
        sheet.set(f"A{row}", alias)
        sheet.set(f"B{row}", expr)
        sheet.set(f"C{row}", note)
        sheet.setAlias(f"B{row}", alias)
        row += 1
    sheet.set(f"A{row + 1}", "Change values in NPQH-D-M5-Q4-P10.params.csv and rebuild.")
    return sheet


def build(doc, params):
    _clear(doc)
    _params_sheet(doc, params)
    doc.recompute()

    fitting = body(doc, "Fitting")
    thread = fitting.newObject("PartDesign::AdditiveCylinder", "Thread")
    bind(thread, "Radius", "Params.r_thread")
    bind(thread, "Height", "Params.fit_l2")
    bind(thread, "Placement.Base.z", "-Params.fit_l2")
    hexagon = fitting.newObject("PartDesign::AdditivePrism", "Hex")
    hexagon.Polygon = 6
    bind(hexagon, "Circumradius", "Params.r_hex")
    bind(hexagon, "Height", "Params.fit_hex_h")
    sleeve = fitting.newObject("PartDesign::AdditiveCylinder", "Sleeve")
    bind(sleeve, "Radius", "Params.r_d6")
    bind(sleeve, "Height", "Params.body_h")
    bind(sleeve, "Placement.Base.z", "Params.fit_hex_h")
    release = fitting.newObject("PartDesign::AdditiveCylinder", "ReleaseRing")
    bind(release, "Radius", "Params.r_d5")
    bind(release, "Height", "Params.fit_ring_h")
    bind(release, "Placement.Base.z", "Params.fit_l1 - Params.fit_l2 - Params.fit_ring_h")
    bore = fitting.newObject("PartDesign::SubtractiveCylinder", "Bore")
    bind(bore, "Radius", "Params.r_bore")
    bind(bore, "Height", "Params.fit_l1")
    bind(bore, "Placement.Base.z", "-Params.fit_l2")
    tube = fitting.newObject("PartDesign::SubtractiveCylinder", "TubeSeat")
    bind(tube, "Radius", "Params.r_tube")
    bind(tube, "Height", "Params.fit_insert")
    bind(tube, "Placement.Base.z", "Params.fit_l1 - Params.fit_l2 - Params.fit_insert")

    # Joints attach to this frame: the axis on the sealing face under the
    # hex. Z points out of the thread hole, along the fitting.
    frame(doc, "IF_port", x="0", y="0", z="0")
    # The hose end sits here, at the open end of the fitting.
    frame(doc, "IF_hose", x="0", y="0", z="Params.fit_l1 - Params.fit_l2 - Params.fit_insert")


# Keep this line as it is. FreeCADCmd 1.1 sets __name__ to the file name,
# so a test on "__main__" would skip the build without a word.
main(build, globals(), cad_dir=_HERE)
