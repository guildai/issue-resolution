# Warning on the YAML flags with `type: boolean`

https://github.com/guildai/guildai/issues/56

## Problem

Guild doesn't coerce boolean types.

## Recreating

Requirements:

- guildai<=0.7.0

To recreate:

```
$ guild run
```

The preview shows:

```
WARNING: unknown flag type 'boolean' for generate_pos - cannot coerce
You are about to run train
  generate_pos: no
```

## Fix

This is fixed in 0.7.0.
