# Runs not appearing in guild view due to broken symlinks

https://github.com/guildai/guildai/issues/36

## Problem summary

- Batch runs with broken links to child trials
- Batch runs had been terminated early
- Batches weren't showing up in Guild View

## Recreating

This issue cannot be created with 0.6.6.dev4. It was not tested with
0.6.5.

The directory [`sample-guild-home`](sample-guild-home) contains a set
of runs that match the problem summary:

- One batch (terminated)
- Two trials, both completed (one sucessfully, another terminated)
- Batch includes a link to a missing child

To recreate the scenario in Guild View:

    $ cd issue-36
    $ guild -H sample-guild-home view

[`op.py`](op.py) is the original script that was run to generate the
batch and trials using:

    $ guild -H sample-guild-home run.op id=[1,2,3]

The operation was terminated after run #2 was started. This left the
runs with one batch and two trials, both of which were correctly
linked to from the batch. A third (broken) link was added to simulate
the condition described in the issue.
