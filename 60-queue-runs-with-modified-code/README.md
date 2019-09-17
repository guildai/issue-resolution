# Queue runs (and with modified code)

https://github.com/guildai/guildai/issues/60

## Problem

There's currently no way to run batches that use different iterations
of source code.

Guild supports runs with different flag values. However, it is useful
to also consider different source code iterations.

For example, run a "batch" with variations of a model architecture:

- Trial 1: Use 3 hidden layers
- Trial 2: Perform an experimental data transform on inputs
- Trial 3: Use an experimental transfer function
- ...

## Notes

From the issue, the use of `--stop-after` probably wants to be
`--stage` - however, stage puts the run off into an ad hoc
directory. We'd want to stage as a run - the way remote runs work.

There some logic in batches that applies here as well.

Assuming the problem definition is on target (might not be), there are
a couple of tracks that occur to me:

1. Parameterize the various code iterations so they can be driven with
   hyperparameters.

2. If the changes are cumbersome to parameterize, create separate
   iterations in source and name them as different operations (or
   models).
