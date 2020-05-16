# Guild makes user classes not serializable

https://github.com/guildai/guildai/issues/175

## Problem

Guild's loading/executing of main modules is breaking pickling when
classes are defined in the main module.

## Recreating

- guild<=0.7.0.rc
- Python 3.x (cannot recreate issue on Python 2.7)

## Workarounds

As @CarloLucibello points out in the issue, move class definitions for
pickled objects outside of the main module.

See also the `test-alt` operation in [guild.yml](guild.yml) for an
alternative way to run a module, which bypasses `guild.op_main` to use
Python directly. This approach loses any Guild plugins (e.g. sys
summary stats).

## Fix

Unsure - this is likely related to Guild's method of module loading
and naming that's causing issues for Python's pickling mechanism.
