# Guild incorrectly importing flags from other modules

https://github.com/guildai/guildai/issues/119

## Problem

Guild blindly responds to all mods to an argparse parser, even when
the mods are coming from other libraries.

## Recreating

Requirements:

- <=0.7.0.rc4

To recreate, run:

```
$ guild run test.py
```

Guild prompts with flags defined in [`submod`](submod.py) that have
nothing to do with [`test`](test.py) flags.

## Workarounds

This is fixed in 0.7.0.rc5.

To work around earlier versions, either define the list of flags to
import using `flags-import` or skip the unwanted flags using
`flags-import-skip`.
