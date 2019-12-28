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

## Workarounds

Use `tensorboard --logdir RUN_DIR` as a temporary workaround.

## Fix

Pending
