# Bug: stopping a run that's being run by a queue freezes the queue

https://github.com/guildai/guildai/issues/245

## Problem

Guild asserts that its output reader threads have exited when they may
not have. Guild uses a timeout of 10 seconds when waiting on readers
to exit. This is misplaced as it should wait forever and rely on the
underlying process to close.

## Recreating

Requirements:

- guild<=0.7.2
- See [requirements.txt](requirements.txt)

Steps:

```
$ guild run test.py --stage -y
$ guild run queue -y
```

The queue starts the staged run.

In another terminal, run:

```
$ guild stop -Fo test.py -y
```

Depending on timing, the OP assertion will occur.

## Workarounds

This assertion can be ignored as it's benign.

## Fix

This is addressed in 0.7.3. Upgrade to that version or later.

## Related Issues

None
