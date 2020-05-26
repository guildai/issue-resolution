# Environment variables not correctly set during optimisation runs

https://github.com/guildai/guildai/issues/187

This issue if fixed in 0.7.0.rc10.

## Problem

Guild is letting the environment overwrite Guild-specific env
associated with the current op. This is resulting in bogus env from
the batch run leaking into the env of the trials. In particular,
`GUILD_OP` and `PROJECT_DIR`.

## Recreating

Requirements:

- guild<=0.7.0.rc9

As a baseline, change to this directory and run [`test.py`](test.py)
to see what it normally prints.

    $ guild run test.py -y
    PROJECT_DIR .
    GUILD_OP test.py

This shows the project dir and op name.

Next, run `test.py` in a batch:

    $ guild run test.py -o + -y

This generates a batch of a single trial. The trial prints the wrong
info:

    INFO: [guild] Running trial ...: test.py ()
    PROJECT_DIR
    GUILD_OP +

The correct output should be the values printed when run outside the
batch.

## Workarounds

None. Upgrade to 0.7.0.r10 for a fix.

## Fix

The fix is to apply op env after system env to ensure that Guild and
op controlled env are not overridden by acceident or otherwise.

## Related Issues

None
