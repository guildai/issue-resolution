---
doctest-type: bash
---

# ValueError at the commented-out last line in Jupyter notebook

https://github.com/guildai/guildai/issues/301

## Problem

Guild does not handle comments that occur on the last line of a cell.

## Recreating

Requirements:

- guild<=0.7.5
- See [requirements.txt](requirements.txt)

Steps to recreate:

    $ guild run test.ipynb -y
    INFO: [guild] Initializing test.ipynb for run
    Traceback (most recent call last):
    ...
    ValueError: start (2,37) precedes previous end (3,0)
    <exit 1>

## Workarounds

Include the following line as the last line of the cell:

``` python
pass  # workaround for https://github.com/guildai/guildai/issues/301
```

## Fix

Pending


## Related Issues

None
