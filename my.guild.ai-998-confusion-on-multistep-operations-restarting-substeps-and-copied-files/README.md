---
doctest-type: bash
---

# Confusion on multistep operations, restarting substeps, and copied files?

https://my.guild.ai/t/confusion-on-multistep-operations-restarting-substeps-and-copied-files/998

## Problem

This issue needs to clarify some of Guild's behavior:

- Links vs copies when running steps
- Links vs copies when resolving upstream run dependencies
- Parent run status updates when child step runs are subsequently
  re-run and completed

## Recreating

Requirements:

- guild<=0.9.0

    $ guild check -n --version '<=0.9.0'

Delete runs associated with this project.

    $ guild runs rm -y -Ft my.guild.ai-998
    ???
    <exit 0>

The `pipeline` operation in [`guild.yml`](guild.yml) runs two steps:
prepare and train. Each of these steps is configured to fail by
default.

Run the pipeline.

    $ guild run pipeline -y
    INFO: [guild] running prepare: prepare
    Running prepare
    Traceback (most recent call last):...
    AssertionError
    <exit 1>

The pipeline fails because the prepare step fails. The train step is
not run.

    $ guild runs -s -Ft my.guild.ai-998
    [1]  prepare   error  fail=yes
    [2]  pipeline  error

Fix the failed prepare step manually.

    $ guild run --restart `guild select -Fo prepare` fail=no -y
    Running prepare

    $ guild runs -s -Ft my.guild.ai-998
    [1]  prepare   completed  fail=no
    [2]  pipeline  error

Restart the pipeline with the `--needed` option.

    $ guild run --restart `guild select -Fo pipeline` --needed -y
    INFO: [guild] running prepare: prepare
    Running prepare
    Traceback (most recent call last):...
    AssertionError
    <exit 1>

This behavior is incorrect - Guild should skip the prepare step
because it's completed and its flag have not changed.

## Fix

This issue is resolved in `0.9.0.dev1` - see [`FIX.md`](FIX.md).
