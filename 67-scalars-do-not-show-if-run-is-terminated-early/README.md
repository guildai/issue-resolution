# Scalars do not show if run is terminated early

https://github.com/guildai/guildai/issues/67

## Problem

Output scalars aren't being logged under certain cases.

For example:

```
hello: 1.123
... more output
```

When `Ctrl-c` is used to terminate the run, `hello` is not logged.

If the script runs to completion, `hello` is logged.

This is not easily recreated.

## Recreating

Requirements:

- guild<=0.6.6

### Terminate run early

Run:

```
$ guild run fashion.py -y
```

Type `Ctrl-c` before the operation finished.

View the scalars for the run:

```
$ guild runs info
```

Note that `hello` is NOT present.

### Let run finish

Run the operation again:

```
$ guild run fashion.py
```

This time let it finish.

View scalars:

```
$ guild runs info
```

Note that `hello` IS present.

## Workarounds

When this problem occurs, the only known workaround is to explicitly
log the scalars using a summary writer.

See [explicit_logging.py](explicit_logging.py) for details.

## Fix

Fixed in 0.6.7.dev5.

## Related Issues

[Logging with tqdm results in jumbled
output](https://github.com/guildai/guildai/issues/54) *may* be
related, though it's not clear if it is.
