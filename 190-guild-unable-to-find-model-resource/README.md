# Guild unable to find model resource

https://github.com/guildai/guildai/issues/190

## Problem

The test for "is scientific notation run ID" when decoding flags is
wrong.

## Recreating

Requirements:

- guild<=0.7.0.rc9

To recreate this problem, change to this directory and run:

    $ export GUILD_HOME=.
    $ guild run downstream upstream=1e0000000
    WARNING: cannot find a suitable run for required resource 'upstream'
    You are about to run downstream
      upstream: '1.0'
    Continue? (Y/n) n

If you specify the run ID with one less `0`, Guild recognizes the flag
arg as a run ID:

    $ guild run downstream upstream=1e000000
    You are about to run downstream
      upstream: '1e000000'
    Continue? (Y/n) n

## Workarounds

Specify the argument using the magic 8-char formula or specify enough
chars to break the scientific notation syntax.

## Fix

This is fixed in 0.7.0.rc10.
