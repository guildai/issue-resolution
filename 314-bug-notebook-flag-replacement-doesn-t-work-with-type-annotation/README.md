---
doctest-type: bash
---

# [Bug] notebook flag replacement doesn't work with type annotation

https://github.com/guildai/guildai/issues/314

## Problem

Guild does not detect or set/modify values that use Python type
annotations.

## Recreating

Requirements:

- guild<=0.7.5
- See [requirements.txt](requirements.txt)

To recreate, run `test.ipynb`. This notebook defines variables `x` and
`y`.

    $ guild run test.ipynb x=10 y=20 -y
    guild: unsupported flag 'y'
    Try 'guild run test.ipynb --help-op' for a list of flags or
    use --force-flags to skip this check.
    <exit 1>

`y` is not detected because it uses type annotations.

## Workarounds

Upgrade to 0.7.5.

## Fix

This is fixed in 0.7.5.
