---
doctest-type: bash
---

# Torch.multiprocessing.spawn fails

https://my.guild.ai/t/torch-multiprocessing-spawn-fails/929

## Problem

A Python script that uses `torch.multiprocessing` cannot be run with
Guild.

The issues appears to be related to Guild's loading of main modules
from `op_main`. See **Workarounds** below for a way around this.

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

The code runs successfully using Guild's `exec` spec. See
the `test-exec` operation in [`guild.yml`](guild.yml).

    $ cat guild.yml | grep test-exec -A1
    test-exec:
      exec: python .guild/sourcecode/test.py

    $ guild run test-exec -y
    Hello (0, 1, ['foo', 'bar'])

    $ guild runs info
    id: ...
    operation: test-exec
    from: ...
    status: completed
    ...

## Fix

Pending

## Related Issues

Pending
