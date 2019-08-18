# Duplicated tensorboard output

https://github.com/guildai/guildai/issues/32

## Recreating

As of 0.6.5 this issue cannot be recreated.

To show the current functionality, run:

    $ cd issue-32
    $ ./recreate

Note this generates runs in /tmp/guild-issue-32. You must delete this
directory manually.

The `recreate` script runs `guild tensorboard` without options. This
excludes batch runs in the list - only trial runs should be visible in
TensorBoard.

To include batch runs, use the `--include-batch` option. E.g.

    $ guild -H /tmp/guild-issue-32 tensorboard --include-batch
