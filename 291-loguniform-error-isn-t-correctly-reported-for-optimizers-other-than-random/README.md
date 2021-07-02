---
doctest-type: bash
---

# `loguniform` error isn't correctly reported for optimizers other than random

https://github.com/guildai/guildai/issues/291

## Problem

Guild is not handling misspecified flag functions sensibly.

## Recreating

Requirements:

- guild==0.7.4

When the order of the flag function args is MAX:MIN (incorrect order),
Guild shows a misleading message:

    $ guild run test.py --optimizer gbrt
    >   x=loguniform[1e-2:1e-6]
    >   -m 1 -Fo random-starts=0 -y
    ERROR: [guild] flags for batch (x=loguniform[1e-2:1e-6]) do not contain any search dimensions
    Try specifying a range for one or more flags as NAME=[MIN:MAX].
    <exit 1>

When the order of the flag function args is correct, Guild runs as expected:

    $ guild run test.py --optimizer gbrt
    >   x=loguniform[1e-6:1e-2]
    >   -m1 -Fo random-starts=0 -y
    INFO: [guild] Random start for optimization (missing previous trials)
    INFO: [guild] Running trial ...: test.py (x=...)
    loss: ...
    <exit 0>

This is the same behavior when `random` is used.

    $ guild run test.py x=loguniform[1e-2:1e-6] -m1 -y
    ERROR: [guild] flags for batch (x=loguniform[1e-2:1e-6]) do not contain any search dimensions
    Try specifying a range for one or more flags as NAME=[MIN:MAX].
    <exit 1>

    $ guild run test.py x=loguniform[1e-6:1e-2] -m1 -y
    INFO: [guild] Running trial ...: test.py (x=...)
    loss: ...
    <exit 0>

When run as a batch, Guild reports a more meaningful message, but with a traceback.

    $ guild run test.py --optimizer + x=loguniform[1e-2:1e-6] -y
    Traceback (most recent call last):
    ...
    ValueError: the lower bound 0.01 has to be less than the upper bound 1e-06
    <exit 1>

    $ guild run test.py --optimizer + x=loguniform[1e-6:1e-2] -y
    INFO: [guild] Running trial ...: test.py (x=...)
    loss: ...
    <exit 0>

## Workarounds

This bug is an error message problem. Ensure that the lower and upper
limits of the function are specified in MIN:MAX format.

## Fix

Pending
