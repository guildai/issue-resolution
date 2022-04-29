---
doctest-type: bash
---

# Cannot define a dependency on a batch

https://github.com/guildai/guildai/issues/394

## Problem

OP title has evolved a bit - this topic involves using batches to run
work and then define a dependency on that batch.

The goal is to require a batch run as a dependency. There's an issue
with Guild, as of 0.8.0, that makes this a bit challenging. See
*Recreating* below for details.

## Recreating

Requirements:

- guild<=0.8.0

    $ guild check -n --version '<=0.8.1rc1'

Batch runs for an operation are named '<op-name>+' (operation name
followed by a plus sign). It should be possible to define an upstream
dependency for a batch running 'op' by specifying the operation name
'op+':

``` yaml
downstream:
  requires:
    - operation: op+
```

However, this isn't working in 0.8.0.

To illustrate, let's run `op` defined in [`guild.yml`](guild.yml) as a
batch. We need to specify `--keep-batch` to preserve the parent batch
run, which Guild otherwise deletes.

    $ guild run op name=[a,b,c] --keep-batch -y
    INFO: [guild] Running trial ...: op (name=a)
    INFO: [guild] Running trial ...: op (name=b)
    INFO: [guild] Running trial ...: op (name=c)

Next, we'll run `summary`, which requires a run matching `op+`.

    $ grep summary: guild.yml -A3
    summary:
      exec: ls
      requires:
        operation: op+

    $ guild run summary -y
    Resolving batch dependency
    Using run ... for batch resource
    c

Note in this case that Guild resolves a single `op` run where
`name=c`. This is not what we want - we want Guild to resolve the
batch run, which contains links to the three `op` runs.

There is an issue with Guild's run resolution that does not correctly
detect/use the '+' in the operation spec.

Note that Guild uses regular expressions when resolving operation
names. However, when escaped using `op\+`, Guild does not find an
upstream run at all. This is illustrated by the `summary2` operation.

    $ grep summary2: guild.yml -A3
    summary2:
      exec: ls
      requires:
        operation: op\+

    $ guild run summary2 -y
    WARNING: cannot find a suitable run for required resource 'batch'
    Resolving batch dependency
    guild: run failed because a dependency was not met: could not resolve
    'operation:op\+' in batch resource: no suitable run for op\+
    <exit 1>

## Workarounds

The [`guild select`](https://my.guild.ai/commands/select) command can
be used to get the full run ID of a batch. This can be used with
command substitution in the applicable shell to select the latest
batch run.

    $ guild run summary batch=`guild select -Fo op+` -y
    Resolving batch dependency
    Using run ... for batch resource
    ...
    <exit 0>

We can't verify in these tests that the runs for `a`, `b`, and `c` are
available in the latest run (`summary`op) but we can list all of the
files and show that there are three available in three distinct
directories.

    $ guild ls -Ln
    .../
    .../...
    .../
    .../...
    .../
    .../...

## Fix

Fix Guild's run resolution logic to work with batch runs. The behavior
of run selection should be kept in sync with the behavior implemented
in `guild select.
