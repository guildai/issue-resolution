# Guild creates new line when tqdm has long text

https://github.com/guildai/guildai/issues/129

## Problem

Not sure.

## Recreating

Requirements:

- guild<=0.7.0.rc9
- tqdm>=0.41.1

Running `guild run test.py` and `python run test.py` seem to behave
the same.

The new lines appear when the tty display does not accommodate the
line length - but this seems to happen with or without Guild in the
mix.

## Workarounds

Not sure.

## Fix

Pending

## Related Issues

- https://app.zenhub.com/workspace/o/codewell/ml-workflow/issues/68
