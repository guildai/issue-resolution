---
doctest-type: bash
---

# How to filter runs using multiple flag values

https://my.guild.ai/t/how-to-filter-runs-using-multiple-flag-values/760

## Problem

Guild does not support user-defined filter expressions.

## Recreating

Requirements:

- guild<=0.8.1

Generate a couple runs of our sample.

    $ guild run filter_test.py a=1 b=4 -y
    a=1 b=4

    $ guild run filter_test.py a=2 b=4 -y
    a=2 b=4

We'd like to show runs where a is 1 and b is 4. We can query the
label, however, we can't apply the AND operator --- Guild's
application of multiple label filters uses OR.

    $ guild runs -Fl a=1 -Fl b=4 -n2
    [1:...]  filter_test.py  ...  completed  a=2 b=4
    [2:...]  filter_test.py  ...  completed  a=1 b=4

## Workarounds

Upgrade to 0.8.2.

## Fix

This has been addressed in 0.8.2. See [FIX.md](FIX.md) for details.

## Related Issues

None
