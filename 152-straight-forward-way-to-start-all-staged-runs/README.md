# Straight forward way to start all staged runs

https://github.com/guildai/guildai/issues/152

## Problem

While it's easy to stage runs, Guild doesn't provide a straigt forward
way to restart staged runs.

Guild does now support queues, which can be used. This is arguably a
decent solution.

## Recreating

Requirements:

- guild==0.7.0.rc9

Change to this directory and stage some runs:

    $ guild run test.py x=range[1:20] --stage-trials

The issue is how to easily start the staged runs.

## Workarounds

Use a queue:

    $ guild run queue run-once=yes

## Fix

As of 0.7.0.rc10, a "start" (alias for "restart") of a batch run will
simply re-generate staged runs. This is defensible as it's literally
doing what's being asked: start a batch run responsible for staging a
bunch of runs.

One could conceve of this to mean "start the runs you staged". A
"restart" of a trial actually starts the trial run - it doesn't merely
re-stage it.

So, stage the trials:

    $ guild run test.py x=range[1:20] --stage-trials

And start them:

    $ guild run --start `guild select -o test.py+`

All said, queues do work pretty well - let's hold off until it becomes
clearer.
