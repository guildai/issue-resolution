# Remote run cannot resolve dependencies

https://github.com/guildai/guildai/issues/101

This issue is resolved in 0.7.0.rc10.

## Problem

Guild resolves required runs for remote ops using local runs rather
than remote runs.

## Recreating

Requirements:

- 0.7.0.rc2
- ssh + remote ssh configuration (see below)

Using the following remote config:

``` yaml
remotes:
  debug-101:
    type: ssh
    host: localhost
    guild-home: /tmp/guild-env-debug-101
```

Confirm that you can ssh to `localhost`:

```
$ ssh localhost true
```

The command should run without an messages or errors. Resolve any
errors before continuing.

Confirm that remote is available:

```
$ guild remote status debug-101
```

Expected output:

```
debug-101 (localhost) is available
```

Change to this project directory and run:

```
$ guild run upstream -r debug-101 -y
```

The run should succeed with the message:

```
Starting upstream on localhost as <upstream run ID>
I am upstream <upstream run ID>
Run <upstream run ID> stopped with a status of 'completed'
```

Confirm that the `upstream` run appears in the runs list for the
remote:

```
$ guild runs -r debug-101
```

Next run `downstream`:

```
$ guild run downstream -r debug-101
```

Guild shows this preview:

```
WARNING: cannot find a suitable run for required resource 'upstream'
You are about to run downstream on debug-101
  upstream: unspecified
Continue? (Y/n)
```

This recreates the error - Guild does not resolve the `upstream`
operation despite a run being available.

## Workarounds

For versions prior to 0.7.0.rc10, specify the run ID explicitly as a
flag value as a work around. Otherwise this is resolved in 0.7.0.rc10.

## Fix

Upgrade to 0.7.0.rc10 and re-run the steps above to confirm the fix.

When you run `downstream` you should be prompted with the run ID for
the latest remote `upstream` run.

The downstream operation should complete successfully with output like
this:

```
Starting downstream on debug-101 as ...
Resolving upstream dependency
Using output from run ... for upstream resource
I am downstream ...
I am using upstream <run ID of specified upstream>
Run ... stopped with a status of 'completed'
```

If there are more than one upstream runs, you can specify the run to
use with the `upstream` flag. You can specify a partial run ID.

If you specify an invalid run ID for `upstream` (i.e. a run matching
the value doesn't exist), Guild warns you but runs the operation
anyway, which fails.
