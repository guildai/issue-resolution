---
doctest-type: bash
---

# Fix

Requirements:

- guild>0.9.0
- R

To run this file as a test, use `guild check -t README.md`

To run the fix use `guild check -t FIX.md`.

Confirm we're running the version of Guild that replicates the
reported behavior.

    $ guild check -n --version '>0.9.0'

Test sourcecode copy for `subdir/train.R`.

    Copying from the current directory
    Rules:
      exclude dir .guild
      exclude dir * containing .guild-nocopy
      exclude dir .git
      gitignore + guildignore patterns
      exclude .git*, .guildignore
    Selected for copy:
      FIX.md
      README.md
      train.R
      subdir/train.R
      subdir/train.py
    Skipped:

Run `subdir/train.R`.

    $ guild run subdir/train.R -y
    ??? cat("hi\n")
    hi
