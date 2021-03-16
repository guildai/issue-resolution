---
doctest-type: bash
---

# Range interpreted as string if min>max

https://github.com/guildai/guildai/issues/274

## Problem

Not sure.

## Recreating

Requirements:

- guild<=0.7.3rc1
- See [requirements.txt](requirements.txt)

The following runs the issue example but it's unclear how Guild is
interpreting the flag as a string. You can execute the example by
running `guild check -nt README.md` from this directory.

    $ guild run test.py lr=[0.003:0.00004] -y
    ERROR: [guild] flags for batch (lr='[0.003:0.00004]') do not contain any search dimensions
    Try specifying a range for one or more flags as NAME=[MIN:MAX].
    <exit 1>

## Workarounds

Pending

## Fix

Pending
