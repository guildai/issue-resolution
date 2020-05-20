# Adding TensorBoard mesh breaks guild view

https://github.com/guildai/guildai/issues/178

## Problem

Guild does not handling non-scalar values.

## Recreating

Requirements:

- guild==0.7.0.rc9
- torch==1.4.0
- tensorboard==2.2.1

Change to this directory and run:

    $ guild init
    $ source guild-env
    $ guild run test.py

This generates a run that logs a mesh using [this example](test.py).

Try to view the mesh using Guild TensorBoard:

    $ guild tensorboard

This operation fails with the reported traceback.

## Workarounds

None. Upgrade to 0.7.0.rc10.

## Fix

This issue is fixed in 0.7.0.rc10.
