# 0.7.3 stop not working with PyTorch data loader

https://github.com/guildai/guildai/issues/281

## Problem

Not sure.

## Recreating

Requirements:

- guild==0.7.3
- See [requirements.txt](requirements.txt)

Run `test.py`:

    $ guild run test.py sleep=99 -y

In another terminal, stop test:

    $ guild stop -Fo test.py -y

Note that the `test.py` operation does not stop.

## Workarounds

Not sure.

## Fix

Not sure.
