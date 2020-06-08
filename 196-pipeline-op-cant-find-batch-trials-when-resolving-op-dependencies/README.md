# Pipeline op can't find batch trials when resolving op dependencies

https://github.com/guildai/guildai/issues/196

## Problem

When running in a stepped op, downstream runs are only able to select
zero or one upstream runs. In a stepped op, it would make more sense
to select by default all upstream runs generated in the stepped op.

## Recreating

Requirements:

- guild<=0.7.0.rc10

There are two operations that illustrate separate problems.

`pipeline-1` breaks because Guild downstream runs can't find upstream
runs because the upstream runs are trials within batches. Guild does
not consider batch trials for candidate runs. This is a bug.

To recreate, change to this directory and run:

    $ guild run pipeline-1

Output:

```
You are about to run pipeline-1
Continue? (Y/n)
INFO: [guild] running upstream: upstream a=[1, 2]
INFO: [guild] Running trial d374baf5e8ff47afa8ab60fb496218a6: upstream (a=1)
1
INFO: [guild] Running trial 6fd02919c6064cc7a4c9d2ce7d52775a: upstream (a=2)
2
INFO: [guild] running downstream: downstream b=[3, 4]
WARNING: cannot find a suitable run for required resource 'upstream'
INFO: [guild] Running trial 2160a0f918464d78992f67ea85a411d3: downstream (b=3)
INFO: [guild] Resolving upstream dependency
ERROR: [guild] trial 2160a0f918464d78992f67ea85a411d3 exited with an error (see log for details)
INFO: [guild] Running trial ce4052f7ebec4050959522fdb33e408f: downstream (b=4)
INFO: [guild] Resolving upstream dependency
ERROR: [guild] trial ce4052f7ebec4050959522fdb33e408f exited with an error (see log for details)
```

`pipeline-2` works around this by using `isolate-runs: no` for the
downstream step. This causes Guild to look at all runs, including
batch trials.

However, Guild only ever selects the latest available run and so the
batch of two upstream trials is never fully used. The reasonable
expected behavior is that both trials are used in the downstream
batch. This would result in six trials for four trials of
downstream. But we only see two.

    $ guild run pipeline-2

Output:

```
You are about to run pipeline-2
Continue? (Y/n)
INFO: [guild] running upstream: upstream a=[1, 2]
INFO: [guild] Running trial 5a19855d880840b1ab9816a11af156c2: upstream (a=1)
1
INFO: [guild] Running trial efe01d8dfc06439eb7357074daa9106f: upstream (a=2)
2
INFO: [guild] running downstream: downstream b=[3, 4]
INFO: [guild] Running trial 5dc263b759d0456db0c09024d1050d80: downstream (b=3, upstream=efe01d8dfc06439eb7357074daa9106f)
INFO: [guild] Resolving upstream dependency
INFO: [guild] Using run efe01d8dfc06439eb7357074daa9106f for upstream resource
efe01d8dfc06439eb7357074daa9106f
3
INFO: [guild] Running trial 7af7dc3499c5469f9e7b61ce7ebaa457: downstream (b=4, upstream=efe01d8dfc06439eb7357074daa9106f)
INFO: [guild] Resolving upstream dependency
INFO: [guild] Using run efe01d8dfc06439eb7357074daa9106f for upstream resource
efe01d8dfc06439eb7357074daa9106f
4
```

## Workarounds

`pipeline-3` avoid the upstream batch by running each upstream step as
a single run and duplicating the call to the downstream batch for each
upstream run.

This approach becomes cumbersome-to-untenable when there are more
downstream steps.

`pipeline-4` uses several devious tricks to approximate the desired
behavior:

- Define pipeline level flags that are used in steps
- Define default pipeline flags with lists that describe the set of
  step flags to search (grid) over
- Use `--needed` with each step to avoid re-running steps with the
  same flag values
- Use `isolate-runs: no` to allow each step to consider all runs when
  applying the "needed" test

And somehow this achieves the desired results.

## Fix

Ultimate I think we want `pipeline-1` to work as expected.

When resolving required runs within a stepped op, the resolver should
select all available upstream runs matching the op spec, at least by
default.

Perhaps another way of approaching this, Guild should expand its op
resolution logic to select all non-error runs as alternative to
matching just the latest run.

Something perhaps like this:

    $ guild run downstream upstream=all

Alternatives:

    - `all[]`
    - `*`
    - `select[:]`

This issue could be considered indirectly related to the need to
provide a select spec for runs and support that within the op
dependency spec.
