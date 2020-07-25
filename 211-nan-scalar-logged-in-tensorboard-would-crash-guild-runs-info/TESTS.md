# Tests

Verify we're running the expected version.

    >>> run("guild check --version '>=0.7.1.dev1' -n")
    <exit 0>

The `test.py` script logs both 'inf' and 'nan' values. This is okay
but generates a warning.

    >>> run("guild run test.py -y", ignore="Refreshing")
    WARNING: [root] NaN or Inf found in input tensor.
    WARNING: [root] NaN or Inf found in input tensor.
    <exit 0>

Guild shows the last value, which is 'inf' in `guild runs info`.

    >>> run("guild runs info")
    id: ...
    scalars:
      runs/...#loss: inf (step 2)
    <exit 0>

To show all scalars, use `--all-scalars`.

    >>> run("guild runs info --all-scalars")
    id: ...
    scalars:
      runs/...#loss:
        avg: nan (step 4)
        first: nan (step 1)
        last: inf (step 2)
        max: nan (step 1)
        min: nan (step 1)
        total: nan (step 4)
    <exit 0>
