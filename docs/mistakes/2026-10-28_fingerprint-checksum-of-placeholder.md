# 2026-10-28 — Fingerprints recorded the checksum of a placeholder, not of the part file

## What happened

The mounting frames in every part file were hidden. Four of our own models
keep a checksum of their part file in the fingerprint, so the checksums had
to be updated. Before that, a `git stash` and `git stash pop` replaced the
part files on disk with Git LFS placeholders: small text files that only
point to the real file. The new checksums were taken from those placeholders.
The online check compared them with the real files and failed.

The real part files on GitHub were right the whole time. Only the four
checksums were wrong, and they were fixed in the same pull request.

## Why it went wrong

- In cloud sessions, Git LFS downloads large files only on request
  (`git lfs smudge --skip`). Any git command that writes files again, such as
  `stash pop` or `checkout`, leaves placeholders.
- The local check skips placeholders with only a warning, so it said "all
  gates passed".

## Prevention rule

- Do not run `git stash`, `git checkout` or `git reset` on part files in a
  session where Git LFS skips downloads. If you must, run
  `git lfs pull --include="*.FCStd"` straight after.
- Before you write a checksum of a `.FCStd`, check that the file starts with
  `PK` (a real archive), not with `version https://git-lfs`.
- Read a "Git LFS placeholders" warning from the check as a reason to stop
  when you changed part files.

## Related

- [Log 2026-10-28: mounting frames hidden](../log/2026-10-28_mounting-frames-hidden.md)
