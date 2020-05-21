# Continue batch run after error

https://github.com/guildai/guildai/issues/158

## Problem

Guild stops a batch after one of its trials fail.

## Recreating

Requirements:

- guild<=0.7.0.rc9

Change to this directory and run:

    $ guild run test.py fail=[yes,no]

Guild runs a batch of two trials. The first trial fails and the batch
stops. The second trial not run.

## Workarounds

Upgrade to 0.7.0.rc10 or later.

## Fix

This issue is fixed in 0.7.0.rc10.

To confirm, run the following:

    $ guild run test.py fail=[yes,no]

Guild runs two trials and continues to the second run even when the
first run fails.

As of 0.7.0.rc10, the `run` command supports a `--fail-on-trial-error`
option, which causes the batch to stop with an error as soon as a
trial exits with an error.
