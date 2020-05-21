# Error when running `guild run --stop-after N`

https://github.com/guildai/guildai/issues/155

## Problem

Guild's 'stop after' support in 0.7.0.rc9 is broken.

## Recreating

Requirements:

- guild<=0.7.0.rc9

Change to this directory and run:

    $ guild run sleep.py --stop-after 0

Guild no only fails to stop the process immediately, it terminates as
described in the issue.

## Workarounds

Upgade to 0.7.0.rc10 or later.

## Fix

This issue is resolved in 0.7.0.rc10.

To verify, run:

    $ guild run sleep.py --stop-after 0.01

Note that `--stop-after` accepts floats, which can be used to specify
finer grained minute intervals.

Guild should stop the run shortly after starting it.

    Sleeping for 5 seconds
    Stopping process early (pid 10173) - 0.1 minute(s) elapsed
