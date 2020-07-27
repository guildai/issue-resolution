# Queues compete with batch operations to start staged runs

https://github.com/guildai/guildai/issues/215

## Problem

Queues should skip over staged trials with an active batch operation.

When a queue is running, it enters a race condition with any in-process
batch operations to start queues. The batch operation is unaware of
queues and will start a staged run even when it's already running.

## Recreating

Requirements:

- guild==0.7.0

Start a queue:

```
guild run queue -y
```

In a separate terminal, start a batch of sleep operations:

```
guild run sleep.py seconds=[2]*5 -y
```

Note in the queue terminal that the queue starts many of the staged
runs. The batch starts all of the staged runs.q

## Workarounds

Either:

- When a queue is running, start batches with the `--stage-trials` option.
- Stop queues before running batches.

## Fix

Two changes are needed here:

- Queues must not start staged trials when the trial batch run is running.

- Batch operations must not start trials unless they're in a staged state.
