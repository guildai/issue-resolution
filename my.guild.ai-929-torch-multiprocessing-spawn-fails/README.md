---
doctest-type: bash
---

# Torch.multiprocessing.spawn fails

https://my.guild.ai/t/torch-multiprocessing-spawn-fails/929

## Problem

A Python script that uses `torch.multiprocessing` cannot be run with
Guild.

We're researching the underlying cause/issue.

## Recreating

Ensure that the packages defined in `requirements.txt` are installed.

When run with Python directly:

    $ python test.py
    Hello (0, 1, ['foo', 'bar'])

When run with Guild:

    $ guild run test.py -y
    Traceback (most recent call last):
    ...
    AttributeError: 'dict' object has no attribute '__spec__'
    <exit 1>

## Workarounds

Pending

## Fix

Pending

## Related Issues

Pending
