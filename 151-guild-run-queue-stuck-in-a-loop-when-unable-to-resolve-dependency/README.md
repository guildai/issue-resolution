# Guild run queue stuck in a loop when unable to resolve dependency

https://github.com/guildai/guildai/issues/151

This issue is fixed in 0.7.0.rc10.

## Problem

Queues attempt to re-run staged runs that fail during dependency
resolution phase. Moreover, Guild doesn't change a run status from
`staged` to `error` when it fails due to dependency errors.

## Recreating

Requirements:

- guild<=0.7.0.rc9

To recreate, change to this directory and run:

    $ guild run downstream --stage -y
    $ guild run queue -y

The queue starts the staged run, which fails because a required run
for `upstream` doesn't exist. The queue rapidly attempts to restart
the staged run.

E.g.

```
INFO: [queue] 2020-05-26 16:55:01 Starting staged run bb7753a642894c8ea0ec1c49091c93b9
Resolving upstream dependency
guild: run failed because a dependency was not met: could not resolve 'operation:upstream' in upstream resource: no suitable run for upstream
ERROR: [queue] 2020-05-26 16:55:01 bb7753a642894c8ea0ec1c49091c93b9 failed with exit code 1
INFO: [queue] 2020-05-26 16:55:01 Starting staged run bb7753a642894c8ea0ec1c49091c93b9
Resolving upstream dependency
guild: run failed because a dependency was not met: could not resolve 'operation:upstream' in upstream resource: no suitable run for upstream
ERROR: [queue] 2020-05-26 16:55:02 bb7753a642894c8ea0ec1c49091c93b9 failed with exit code 1
```

## Workarounds

Upgrade to 0.7.0.rc10 or later.

## Fix

Guild clears the STAGED marker before resolving dependencies. This
ensures that any errors that occur during dependency resolution leave
the run in an `error` state.
