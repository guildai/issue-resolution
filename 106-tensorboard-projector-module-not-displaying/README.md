# Tensorboard projector module not displaying

https://github.com/guildai/guildai/issues/106

## Problem

Guild is not copying additional files needed by the projector plugin.

## Recreating

Requirements:

- guildai<=0.7.0.rc4

Create a virtual environment to ensure we're using a controlled set of
TF packages.

    $ virtualenv venv -p python3
    $ source venv/bin/activate
    $ pip install -r requirements.txt

To see the expected behavior, run `test.py` without Guild:

    $ python test.py

This generates several files in `logs`.

Use TensorBoard to view the logs:

    $ tensorboard --logdir logs

Open [http://localhost:6006](http://localhost:6006) and select the
PROJECTOR tab. If the tab isn't visible, select it under the INACTIVE
dropdown at top right. You should see the projected embeddings - ten
randomly generated points.



## Workarounds

Use `tensorboard --logdir RUN_DIR` as a temporary workaround.

## Fix

This is fixed in 0.7.0.rc10. To confirm, run:

    $ guild run test

This runs `test.py` to generate the same set of files when running
directly with Python.

View the generated files:

    $ guild ls

View the run in TensorBoard with Guild:

    $ guild tensorboard

Click the PROJECTOR tab. If the tab doesn't exist, select it from
INACTIVE in the top right.
