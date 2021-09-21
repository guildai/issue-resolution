---
doctest-type: bash
---

# Flags not being imported from config files

https://github.com/guildai/guildai/issues/308

## Problem

Cannot recreate. The OP may not be running the current version of Guild.

## Recreating

Requirements:

- guild<=0.7.4

    $ guild run train --help-op
    Usage: guild run [OPTIONS] train [FLAG]...
    <BLANKLINE>
    Use 'guild run --help' for a list of options.
    <BLANKLINE>
    Flags:
      x  (default is 1.0)
      y  (default is 123)
      z  (default is hello)

    $ guild run train x=2.0 y=345 z=bye -y
    Resolving config:prepare-config-output.json dependency

    $ guild ls -n
    prepare-config-output.json

    $ guild cat -p prepare-config-output.json
    {"x": 2.0, "y": 345, "z": "bye"}
