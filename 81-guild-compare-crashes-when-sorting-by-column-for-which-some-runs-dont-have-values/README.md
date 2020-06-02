# Guild compare crashes when sorting by column for which some runs don't have values

https://github.com/guildai/guildai/issues/81

## Problem

Guild naively uses table values for a common short key. When these
values cannot be compared (e.g. int vs None, float vs string) Python 3
generates an error.

## Recreating

Requirements:

- Python 3
- guild<=0.7.0.rc9

Change to this directory and run:

    $ guild run test.py x=1 -fy
    $ guild run test.py x=hello -fy

Compare the runs, ordering by `x`:

    $ guild compare --min x

Note this only occurs on Python 3.

## Workarounds

None. Upgrade to 0.7.0.rc10.

## Fix

Use a universal value comparator.
