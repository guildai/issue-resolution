# Tensorboard PermissionError due to trailing space in label

https://my.guild.ai/t/tensorboard-permissionerror-due-to-trailing-space-in-label/1005

## Problem

Trailing space in label causes problems for TensorBoard. This might be
Windows specific.

## Recreating

NOTE: This test deviates from the typical test format and uses Python
doctest, rather than bash. We need to parse output from a command
below and so use `run_capture`, which is not possible using the bash
doctest type.

Requirements:

- guild<=0.9.0

Check expected Guild version.

    >>> run("guild check -n --version '<=0.9.0'")
    <exit 0>

Configure a new Guild environment.

    >>> use_project(mkdtemp())

Create a simple operation to run.

    >>> write("guild.yml", """
    ... test:
    ...   main: guild.pass
    ... """)

Generate a run with an empty space at the end of the label.

    >>> run("guild run test --label 'hello ' -y")
    <exit 0>

Run TensorBoard using `--test-logdir` (note this is a developer only
option and not included in the Guild docs) to process the runs and
exit.

    >>> out = run_capture(f"guild tensorboard --no-open --test-logdir")

Get the log dir from output.

    >>> logdir = re.search("Initialized log dir (.*)", out).group(1)

Show files under log dir. Note the space at the end of the label.

    >>> dir(logdir)
    ['... test ... hello ']

## Workarounds

Don't include a blank space at the end of the label :)

## Fix

Pending
