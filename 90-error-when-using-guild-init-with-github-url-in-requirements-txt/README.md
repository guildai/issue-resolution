# Error when using guild init with github url in requirements.txt

https://github.com/guildai/guildai/issues/90

This issue is resolved as of 0.7.0rc3.

## Problem

Guild init is not behaving the same as pip install when setting up env
vars. Possibly a PATH issue.

## Recreating

Requirements:

- guildai<=0.7.0rc2
- `git` available on PATH

To recreate, change to this directory and run:

    $ guild init -y

## Workarounds

Setup the virtual environment manually. If the env is under `venv`
then `source guild-env` will pick it up. Otherwise just activate the
environment normally using `source ENV/bin/activate`.

Guild environments are standard Python virtual envs. The `init`
command is a convenience that works with some additional Guild file
configurable settings (e.g. Python version used for the env).

## Fix

Fixed in 0.7.0rc3
