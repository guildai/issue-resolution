# Guild doesn't show scalars with '/' in key in compare

https://github.com/guildai/guildai/issues/125

## Problem

There are a few issues in play.

- Guild plugins can generate a lot of scalar values that we don't want
  to show up in compare by default.

- Guild doesn't support changing the default list of columns without
  having to redefine the entire list, including flags. This makes the
  `compare` operation attr less-than-useful.

## Recreating

Requirements:

- guild<=0.7.0.rc5

Run:

```
$ guild run test-summaries -y
```

List all of the scalars:

```
$ guild runs info -s
```

Note `a/b` as a scalar.

View the run in compare:

```
$ guild compare -t 1
```

Note that `a/b` is not listed.

## Workarounds

None. This is fixed in 0.7.0.rc6 and later.

## Fix

As of 0.7.0.rc6, Guild now shows scalars that contain '/' chars by
default, provided they don't start with 'sys/'.

To show all scalars, including those that start with 'sys/', compare
now supports a `--all-scalars` or `-s` option. This is consistent with
the `runs info` interface.

To verify, upgade to 0.7.0.rc6 or later.

Run:

```
$ guild run test-summaries -y
```

View the latest run in Compare:

```
$ guild compare 1 -t
```

And show the scalars in `runs info`:

```
$ guild runs info -s
```

## Related Issues

- https://github.com/guildai/guildai/issues/123
- https://github.com/codewell/ml-workflow/issues/52
