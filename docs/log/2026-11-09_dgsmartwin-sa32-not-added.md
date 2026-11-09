# 2026-11-09 — The DGSMARTWIN SA32 encoder is not added to the library

**Role(s):** mechanical engineering, purchasing

## What changed

Nothing is added. DGSMARTWIN (Dongguan Smartwin) offered the SA32 absolute linear encoder for the
compact stage in aqtuator: read head SA32EY05A-MC (EnDat 2.2, 0.1 µm step) and steel tape scale
SA32-L250-MC (250 mm, for 220 mm of travel). We asked for the documents from 14 October to
9 November 2026.

| Asked for | Answer |
| --- | --- |
| Product manual | Not sent |
| Installation manual | Not sent |
| 3D CAD model of the head | Not sent |
| Drawing of the scale | Not sent. Only the head drawing in the sales catalog |
| Scale applicator and end clamps | They exist ("Renishaw type"), but no product numbers |
| Installation video | Only by WhatsApp, WeChat or DingTalk |
| Scale | Steel tape, glued to the base |
| Top speed | 10 m/s at 0.05 µm and at 0.1 µm |

## Why it matters

The library method needs a maker's model or a maker's drawing for each part. We have neither for
the SA32. aqtuator also decided not to continue with DGSMARTWIN for now. The RSF MC 15 stays the
absolute encoder in the library and in the compact stage.

## Next Steps

- None now. If aqtuator takes DGSMARTWIN up again, ask first for the head CAD model and the scale
  drawing.
- aqtuator record: `docs/log/2026-11-09_dgsmartwin-answers-and-stop.md` and
  `docs/decisions/2026-11-09_no-dgsmartwin-for-now.md`.
