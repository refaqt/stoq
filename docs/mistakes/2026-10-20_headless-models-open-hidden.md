# 2026-10-20 — Own models built without the FreeCAD window open hidden

## What happened

The aqtuator compact stage links the LAMOTION ALZ scale and the RUS-ET end
clamps from this library. In the assembly, both parts were invisible, and the
shape of each link was empty. The read head, saved from the FreeCAD window,
showed normally.

Both models were built headless, without the FreeCAD window. The build marks
every Part, Body and frame as visible, and the file stores that. But a headless
save writes no screen settings (the `GuiDocument.xml` part of the `.FCStd`).
When the FreeCAD window opens a file without screen settings, it hides every
object. So the file is right without the window and wrong with it.

The two HIWIN own models, `HGR15R418H` and `HGL15CAZBC+E2`, have the same
problem. They were not changed here.

## Why it went wrong

- The doqs rule says that visibility is stored in the document itself, so a
  headless build gets it right. That is true only without the window.
- The checks read the file without the window, so they saw "visible" and
  passed.
- Nobody opened the rebuilt file in the FreeCAD window before it was merged.

## Prevention rule

- Until the doqs build helper writes screen settings itself, rebuild an own
  model inside the FreeCAD window: start `freecad.exe` with no document open,
  run the build script in it, and let it save. The build helper then saves the
  file with screen settings.
- Before you call an own model done, open it in the FreeCAD window and look at
  it.
- A check that a model is visible must read the screen settings, not only the
  document.

## Related

- [doqs CAD guide, visibility](../../doqs/docs/agent-cad.md)
