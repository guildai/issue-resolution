---
doctest-type: bash
---

# ImportError when running Python op with submodule containing guild.yml

https://github.com/guildai/guildai/issues/477

## Problem

Guild custom module finder, which is registered when `guild.model` is
loaded, is foiling Python's default module loading scheme.

## Recreating

Verify the version of Guild.

    $ guild check --version 0.9.0rc1

Run `a.py` directly.

    $ guild run a.py -y
    Traceback (most recent call last):
    ...
    ImportError: cannot import name 'b' from 'submodule' (.../submodule/__init__.py)
    <exit 1>

## Fix

The issue is fixed in 0.9.0rc2 and later.
