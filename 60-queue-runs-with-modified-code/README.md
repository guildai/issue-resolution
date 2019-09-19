# Queue runs (and with modified code)

https://github.com/guildai/guildai/issues/60

## Problem

As of 0.6.6, Guild does not support scheduling. Users must start runs
and wait for them to finish before starting others.

For short-lived runs, this is less problematic. For long runs, it
forces the user to monitor each run and manually intervene to start
subsquent runs.

## Approach

Guild can be enhanced to support a simple scheduling scheme that uses
a polling operation to start staged runs.

Guild would be changed as follows:

1. Refactor `--stage` as a flag that tells Guild to stage a new run in
   the runs directory. The staged run will appear with a `staged`
   status in the runs list. The previous stage functionality would be
   implemented by a new option `--stage-dir`.

2. Add a `--start` option to the `run` command, which can be used to
   start staged runs.

3. Introduce a new built-in operation `queue` that polls continuously
   for staged runs. When is sees a staged run, it starts that run,
   provided there aren't other runs in progress.

4. Add a `--restage` flag that can be used to update a run with new
   flag values, as well as reset its start time and run
   status. Restaging a run has the side-effect of setting making it
   next-to-be-run by a queue.

With this facility, a use can run a `queue` operation in one console
session and either run or stage runs in another console.

In console #1 - start a `queue` run:

    $ guild run queue

This is a run like any other. When running, it checks for staged
operations and runs them in FIFO order. It continues running until
stopped.

In console #2 - stage runs:

    $ guild run train x=1 --stage

    $ guild run train x=2 --stage

The `queue` running in console 1 polls for pending runs. When it sees
a pending run, it starts it, provided there are no other runs in
progress.

Staged runs can be deleted or restaged using `--restage` as needed.

As a queue is a normal run, it can be stopped, either by typing
`Ctrl-c` in the console or using `guild stop`.

Future possible enhancements:

1. The `queue` operation could be enhanced to start only runs matching
   specified criteria (e.g. label contents, operation names, etc.)

2. Queues could be enhanced to have binning knowledge - i.e. be
   aware of available resources and use that when determining whether
   or not staged runs should be started.

4. Queues could run staged operation in the background in support of
   parallel runs.

## Status

The functionality outlined above is available for experimentation in
Guild 0.6.7.dev4.
