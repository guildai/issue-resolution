---
doctest-type: bash
---

# Support for argument group with argparse

https://github.com/guildai/guildai/issues/200

## Problem

This issue appears to be resolved in 0.7.3.

## Recreating

Cannot recreate in 0.7.3.

## Fix

    $ guild run op.py src=foo -y
    Namespace(src='foo')
    <exit 0>
