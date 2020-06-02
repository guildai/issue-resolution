# Staged runs to automatically use latest operation as input to next

https://github.com/guildai/guildai/issues/78

## Problem

Guild is not considering staged runs as valid runs for staged run
operation requirements.

## Recreating

Requirements:

- guildai==0.6.7.dev8

To recreate, change to this directory and run:

```
$ guild run a --stage -y
$ guild run b --stage -y
```

The second command fails with:

```
Resolving a dependency
guild: run failed because a dependency was not met: could not resolve
'operation:a' in a resource: no suitable run for a
```

## Workarounds

As described in the issue, the work around is to specify the upstream
staged run ID explicitly.

```
$ guild run b a=abcd1234 --stage -y
```

## Fix

This issue has been fixed in 0.6.7.dev9.

The following stages a and then b, using the staged a run ID:

```
$ guild run a --stage --y
$ guild run b --stage --y
```

You can run the staged runs to completion with a queue.

```
$ guild run queue run-once=yes -y
```
