---
doctest-type: bash
---

# Some flags with argparse actions don't get detected

https://github.com/guildai/guildai/issues/378

## Problem

Guild is not support argparse types of `BooleanOptionalAction` (new in
Python 3.9)

## Recreating

Requirements:

- guild<=<applicable Guild version>
- See [requirements.txt](requirements.txt)

Create a new virtual environment using Python 3.9 or later. You can
use Guild for this.

    $ test -d venv || guild init -g 0.8.0 -y
    ???

    $ venv/bin/guild check -n --version '0.8.0'

Run [`test.py`](test.py) as a baseline.

    $ venv/bin/python test.py --help
    usage: test.py [-h] [--foo | --no-foo] [--bar | --no-bar]
    <BLANKLINE>
    optional arguments:
      -h, --help       show this help message and exit
      --foo, --no-foo
      --bar, --no-bar

    $ venv/bin/python test.py
    bar=False foo=True

    $ venv/bin/python test.py --bar --foo
    bar=True foo=True

    $ venv/bin/python test.py --no-bar --no-foo
    bar=False foo=False

Show script help using Guild - flags are not imported.

    $ NO_IMPORT_FLAGS_CACHE=1 venv/bin/guild run test.py --help-op
    Usage: guild run [OPTIONS] test.py [FLAG]...
    Use 'guild run --help' for a list of options.

## Workarounds

Use `action='store_true'` and `action='store_false'` to use old-style
boolean switched (pre Python 3.9).

## Fix

Guild needs support for `BooleanOptionalAction`. Guild should map the
boolean values `yes` and `no` to the command line arg `--<name>` and
`--no-<name>` respectively.

## Related Issues

None
