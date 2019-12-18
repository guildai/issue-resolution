# Remote run cannot resolve dependencies

https://github.com/guildai/guildai/issues/101

## Problem

There's an issue resolving runs on remotes under some
condition. Cannot recreate in the simple case of running over ssh on
localhost.

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

None known at this time.

## Fix

Pending
