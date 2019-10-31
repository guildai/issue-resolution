# Required resource links for batch trials not readable on Windows

https://github.com/guildai/guildai/issues/86

## Problem

When Guild copies a proto directory containing links, the copied links
are readable on Windows.

## Recreating

Requirements:

- 0.6.7.dev9
- Windows OS

Change to this directory and run this command to recreate the problem:

    $ guild run op dummy=[1] -f -y

The `dummy` flag forces Guild to run the operation as a batch with a
single trial.

The error shows up as this:

```
FileNotFoundError: [Errno 2] No such file or directory: 'foo.txt'
ERROR: [guild] Run e7171a24734242c180f4bd71a27b678d failed - see logs for details
```

## Workarounds

None that are reasonable.

## Fix

Under review
