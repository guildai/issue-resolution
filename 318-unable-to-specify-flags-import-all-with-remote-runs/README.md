---
doctest-type: bash
---

# Unable to specify flags-import: all with remote runs

https://github.com/guildai/guildai/issues/318

## Problem

Not sure at this point - cannot recreate an error.

## Recreating

Requirements:

- guild<=0.7.4

Run test op on localhost (required ssh access to localhost):

    $ guild run test -r ssh:localhost x=11 y=22 -y
    Building package
    ...
    Starting test on localhost as ...
    z: 33
    Run ... stopped with a status of 'completed'

## Workarounds

N/A

## Fix

N/A

## Related Issues

None
