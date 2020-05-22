# Logging with tqdm results in jumbled output

https://github.com/guildai/guildai/issues/54

## Problem

Guild's interaction with tqdm is not synchronized when the output
stream is `stderr`.

The issue reports the state when output is `None` - but this is
equivalent to `sys.stderr` or not specifying a value for the `file`
argument. See *Recreating* below for more information.

Note also that the progress bar width for `tqdm` is different when run
with Guild. When run without Guild, the progress bar takes up the full
console width. When run with Guild, the progress bar is the default of
10.

## Recreating

Requirements:

- guild<=0.7.0.rc9
- tqdm

Change to this directory and create and activate a new environment:

    $ guild init
    $ source guild-env

Run `test.py` with Guild:

    $ guild run test.py

With the default flags, the output may be jumped like this:

```
0
1
2
                                      3
  0%|          | 0/10 [00:00<?, ?it/s]4
5
6
7
8
9
100%|██████████| 10/10 [00:00<00:00, 93.81it/s]
```

If the output is not jumbed, try running again or try different values
for `wait` or increase `steps`.

This behavior occurs when the `out` flag is any of these values:

- `null`
- `stderr`
- `default`

Each of these flag values has the equivalent effect of using
`sys.stderr` for output.

To observer synchronized output, use one of the following values for
the `out` flag:

- `stdout`
- a filename (view the file after the operation finished)

To run all scenarios:

    $ guild run test.py out=[null,default,stderr,stdout,log.txt]

Use `guild cat --output [RUN]` to view output for a particular
run. Use `guild cat -p log.txt` to view progress output for the last
run in the batch.

Note that when Guild's run output is disabled by setting
`NO_RUN_OUTPUT` to `1`, output is synchronized.

    $ NO_RUN_OUTPUT=1 guild run test.py -y

## Workarounds

Unfortunately, None if the target stream cannot be `sys.stdout` (as is
the case with canonical progress logging, which should go to stderr).

## Fix

Pending.

## Related Issues

- https://github.com/guildai/guildai/issues/129
