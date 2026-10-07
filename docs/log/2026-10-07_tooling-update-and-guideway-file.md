# 2026-10-07 — Shared tooling updated, guideway file out of git

**Role(s):** mechanical engineering

## What changed

The shared agent rules and the doqs tools now point at their newest
versions. The session start check now also works when a session opens a
parent folder.

The HIWIN file for the assembled HGL15 guideway (two 760 mm rails, two blocks
each) is no longer in git. Nothing in the library uses it. Its row in the
block's vendor index stays, marked `private`, so the record of that
configuration is kept. A copy of the file is in `stoq-private` at the same
path.

The newer doqs checks our own models more strictly. To pass, the build
script and parameter file of our own rail and block models now carry the
model's name, for example `HGR15R418H.build.py`. Each script states its axes.
Both models were rebuilt headless. Their shapes did not change.

## Why it matters

Without these changes the project check failed, so no pull request could
pass.

## Next Steps

- The check still warns about 43 sizes in our own models that are typed in,
  not linked to the parameter sheet. Link them when the models are next
  changed.
