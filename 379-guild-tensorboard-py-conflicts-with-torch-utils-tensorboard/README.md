---
doctest-type: bash
---

# guild/tensorboard.py conflicts with torch.utils.tensorboard

https://github.com/guildai/guildai/issues/379

## Problem

The issue describes a case where `torch.utils.tensorboard` module
imports `guild.tensorboard` from the statement `import tensorboard`,
rather than the `tensorboard` module.

Renaming the Guild module may work around the problem, but it doesn't
address the real problem as describes in the issue.

It's not clear what the root problem is. A possible cause is that the
path to Guild's `guild` package directory is in the Python system
path. The solution in that case is to remove that path entry (or find
out how it's being added) - it should not be in the path.

## Recreating

Issue cannot be recreated below.

Requirements:

- guild<=0.8.0
- See [requirements.txt](requirements.txt)

Setup a virtual environment, activate it, and install the requirements
from `requirements.txt`.

When running this README as a test, first activate the environment,
then run `guild check -nt README.md`.

The test is shown in [`test.py`](test.py).

Run `test.py` with Python directly (baseline behavior):

    $ python test.py
    Imported torch.utils.tensorboard
    tensorboard module is from .../site-packages/tensorboard/__init__.py
    guild.tensorboard modile is from .../site-packages/guild/tensorboard.py

Run `test.py` with Guild:

    $ guild run test.py -y
    Imported torch.utils.tensorboard
    tensorboard module is from .../site-packages/tensorboard/__init__.py
    guild.tensorboard modile is from .../site-packages/guild/tensorboard.py

## Workarounds

Not sure

## Fix

Not sure

## Related Issues

None
