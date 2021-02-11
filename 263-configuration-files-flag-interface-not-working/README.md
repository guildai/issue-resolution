# Configuration files flag interface not working

https://github.com/guildai/guildai/issues/263

## Problem

It appears that Guild is sending command line arguments when the flags
interface is a config file.

## Recreating

Requirements:

- guild<=0.7.3.dev3

See [BUG.md](BUG.md) for steps to recreate or run `make recreate`.

## Workarounds

Strip the leading `--` arg from `sys.argv` before parsing the
arguments.

## Fix

Upgade to 0.7.3.dev4 or later.

To verify, see [FIX.md](FIX.md) or run `make verify-fix`.
