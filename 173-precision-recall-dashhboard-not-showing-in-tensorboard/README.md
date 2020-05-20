# recision-recall dashhboard not showing in tensorboard

https://github.com/guildai/guildai/issues/173

## Problem

Guild doesn't support the full list of TensorBoard plugins.

## Recreating

Requirements:

- guild<-0.7.0.rc9
- tensorflow

Change to this directory and run the following:

    $ guild init
    $ source guild-env
    $ guild run test

This generates a run using [pr_curve_demo.py](pr_curve_demo.py).

View the generated files:

    $ guild ls

View the run using Guild TensorBoard:

    $ guild tensorboard

Note that the PR Curve tab is not available.

It is available if you run `tensorboard` directly using the run
directory with the `--logdir` option.

## Workarounds

None. This is fixed in 0.7.0.rc10.

## Fix

Guild supports the full set of TensorBoard plugins when starting
TensorBoard. This is fixed in:

https://github.com/guildai/guildai/commit/27585fc35d248cc03273fb073d1c5b0f14a53831
