---
doctest-type: bash
---

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

Run `test.py` with Guild:

    $ guild run test.py -y  # doctest: +SKIP

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

    $ guild run test.py out=[null,default,stderr,stdout,log.txt] -y # doctest: +SKIP
    INFO: [guild] Running trial ...: test.py (steps=10, wait=0.01)
    ...
    <exit 0>

Use `guild cat --output [RUN]` to view output for a particular
run. Use `guild cat -p log.txt` to view progress output for the last
run in the batch.

Note that when Guild's run output is disabled by setting
`NO_RUN_OUTPUT` to `1`, output is synchronized.

    $ NO_RUN_OUTPUT=1 guild run test.py -y 2>&1 | tr -cd "[:print:]\n"
    0%|          | 0/10 [00:00<?, ?it/s]                                      0
      0%|          | 0/10 [00:00<?, ?it/s]                                      1
      0%|          | 0/10 [00:00<?, ?it/s]                                      2
      0%|          | 0/10 [00:00<?, ?it/s]                                      3
      0%|          | 0/10 [00:00<?, ?it/s]                                      4
      0%|          | 0/10 [00:00<?, ?it/s]                                      5
      0%|          | 0/10 [00:00<?, ?it/s]                                      6
      0%|          | 0/10 [00:00<?, ?it/s]                                      7
      0%|          | 0/10 [00:00<?, ?it/s]                                      8
      0%|          | 0/10 [00:00<?, ?it/s]                                      9
      0%|          | 0/10 [00:00<?, ?it/s]100%|| 10/10 [00:00<00:00, ...it/s]100%|| 10/10 [00:00<00:00, ...it/s]
    <exit 0>

## Workarounds

0.7.5.dev1 fixes an issue using `NO_RUN_OUTPUT` in the Guild
file. Setting this value disables run output for the applicable
operation.

Below is the operation def in `guild.yml` that runs `test.py` under
the following modified conditions:

- Run output is disabled by setting the operation env `NO_RUN_OUTPUT`
  to `1`
- Stdout and stderr are joined and written to the standard Guild
  output location (`.guild/output`) using the `tee` program

``` yaml
test-workaround:
  exec: bash -c "python -m test 2>&1 | tee .guild/output"
  env:
    NO_RUN_OUTPUT: 1
```

Run the operation (pipe to `strings` to show underlying formatting
here in output):

    $ guild run test-workaround -y | tr -cd "[:print:]\n"
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]100%|| 10/10 [00:00<00:00, ...it/s]100%|| 10/10 [00:00<00:00, ...it/s]
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    <exit 0>

The output is also written to the standard Guild output location
(`.guild/output`):

    $ guild cat --output | tr -cd "[:print:]\n"
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]100%|| 10/10 [00:00<00:00, ...it/s]100%|| 10/10 [00:00<00:00, ...it/s]
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    <exit 0>

Verify by showing `.guild/output`:

    $ guild cat -p .guild/output | tr -cd "[:print:]\n"
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]
    0%|          | 0/10 [00:00<?, ?it/s]100%|| 10/10 [00:00<00:00, ...it/s]100%|| 10/10 [00:00<00:00, ...it/s]
    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    <exit 0>

## Fix

Pending

## Related Issues

- https://github.com/guildai/guildai/issues/129
