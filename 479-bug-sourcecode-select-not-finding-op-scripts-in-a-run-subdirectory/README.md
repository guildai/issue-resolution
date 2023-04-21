---
doctest-type: bash
---

# bug: sourcecode select not finding op scripts in a run subdirectory

https://github.com/guildai/guildai/issues/479

## Problem

Running guild for R with `--test-sourcecode` and a path containing subdirectories
(`guild run --test-sourcecode subdir-a/subdir-b/train.R`) causes guild to try to copy
from a path that does not exist (`Copying from 'subdir-a/subdir-b/subdir-a/subdir-b'`).

## Recreating

Requirements:

- guild<=0.9.0
- R

To run this file as a test, use `guild check -t README.md`

To run the fix use `guild check -t FIX.md`.

Confirm we're running the version of Guild that replicates the
reported behavior.

    $ guild check -n --version '<=0.9.0'

Create and initialize the project that surfaces the problem.

    $ mkdir -p ex-proj
    
    $ cd ex-proj

    $ mkdir -p subdir-a/subdir-b

    $ touch    subdir-a/subdir-b/train.py

    $ touch    subdir-a/subdir-b/train.R

Running `train.py` works as expected.

    $ guild run --test-sourcecode subdir-a/subdir-b/train.py
    Copying from the current directory
    Rules:
      exclude dir .guild
      exclude dir * containing .guild-nocopy
      exclude dir .git
      gitignore + guildignore patterns
      exclude .git*, .guildignore
    Selected for copy:
      subdir-a/subdir-b/train.R
      subdir-a/subdir-b/train.py
    Skipped:

Note: running `guild run subdir-a/subdir-b/train.py` (without `--test-sourcecode`)
causes the program to hang.

Run the R script, which fails to copy any files as it looks under the wrong path.

    $ guild run --test-sourcecode subdir-a/subdir-b/train.R
    Copying from 'subdir-a/subdir-b/subdir-a/subdir-b'
    Rules:
      exclude dir .guild
      exclude dir * containing .guild-nocopy
      exclude dir .git
      gitignore + guildignore patterns
      exclude .git*, .guildignore
    Selected for copy:
    Skipped:
    <exit 0>

Display the op data returned by the R plugin.

    $ Rscript -e 'guildai:::emit_r_script_guild_data("subdir-a/subdir-b/train.R")'
    name: subdir-a/subdir-b/train.R
    flags-dest: subdir-a/subdir-b/train.R
    flags: {}
    exec: '''/usr/lib/R/bin/Rscript'' -e ''guildai:::do_guild_run("subdir-a/subdir-b/train.R")'''

## Workarounds

There are no known workarounds.

## Fix

TODO: Fix, WIP

It appears the path is being calculated correctly for python scripts, but not R scripts.
The current approach for a fix is targeted at comparing these two paths to catch the
discrepancy.