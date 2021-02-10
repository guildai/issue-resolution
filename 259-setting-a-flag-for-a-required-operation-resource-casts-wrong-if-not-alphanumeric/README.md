# Setting a flag for a required operation resource casts wrong if not alphanumeric

https://github.com/guildai/guildai/issues/259

## Problem

Guild doesn't coerce upstream run IDs correctly when the start with
`0`.

## Recreating

Requirements:

- guild<=0.7.3.dev3

Run `BROKEN.md` to recreate the problem with the applicable version of
Guild.

    $ guild check -nt BROKEN.md

## Workarounds

Provide enough of the run ID to convince Guild that it's a string and
not an integer.

## Fix

Pending

## Related Issues

- https://github.com/guildai/guildai/issues/73
