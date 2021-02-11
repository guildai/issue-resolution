# Using global:<name> to import flag doesn't work as described in the doc

https://github.com/guildai/guildai/issues/248

## Problem

Guild does not import flag values when `global:<param>` is specified.

## Recreating

Requirements:

- guild<=0.7.4.dev4

See [BUG.md](BUG.md) for steps to recreate or run `make recreate`.

## Workarounds

Manually specify default values in the Guild file.

``` yaml
op:

  # params is defined as a global dict in `op.py` - the bug is
  # that Guild doesn't inspect this value to import flags. As
  # a workaround, define the flag values using `flags` attr here.
  flags-dest: global:params
  flags:
    x: 1
    y: 2
```

## Fix

This issue is resolved in 0.7.3.dev4. For expected behavior, see
[FIX.md](FIX.md) or run `make verify-fix` to check.
