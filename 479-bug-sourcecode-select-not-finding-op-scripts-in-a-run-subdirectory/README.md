---
doctest-type: bash
---

# bug: sourcecode select not finding op scripts in a run subdirectory

https://github.com/guildai/guildai/issues/479

## Problem

Running guild for R with `--test-sourcecode` and a path containing subdirectories
(`guild run --test-sourcecode subdir/train.R`) causes guild to try to copy
from a path that does not exist (`Copying from 'subdir/subdir'`).

## Recreating

Requirements:

- guild<=0.9.0
- R

To run this file as a test, use `guild check -t README.md`

To run the fix use `guild check -t FIX.md`.

Confirm we're running the version of Guild that replicates the
reported behavior.

    $ guild check -n --version '<=0.9.0'

Test sourcecode copy for `subdir/train.R`.

    $ guild run --test-sourcecode subdir/train.R
    Copying from 'subdir/subdir'
    Rules:
      exclude dir .guild
      exclude dir * containing .guild-nocopy
      exclude dir .git
      gitignore + guildignore patterns
      exclude .git*, .guildignore
    Selected for copy:
    Skipped:
    <exit 0>

Note:

- copying from `subdir/subdir` which does not exist
- nothing is selected for copy

However, when we test sourcecode copy for `subdir/train.R` from the current directory,
guild selects the expected files for copy.

    $ guild run --test-sourcecode train.R
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
    Skipped:

Display the op data returned by the R plugin.

    $ Rscript -e 'guildai:::emit_r_script_guild_data("subdir/train.R")'
    name: subdir/train.R
    flags-dest: subdir/train.R
    flags: {}
    exec: '''/usr/lib/R/bin/Rscript'' -e ''guildai:::do_guild_run("subdir/train.R")'''

## Workarounds

There are no known workarounds.

## Fix

Fix is [here](https://github.com/guildai/guildai/commit/0f91e1e0).