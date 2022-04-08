---
doctest-type: bash
---

# Fix

The fix for [this issue](https://github.com/guildai/guildai/issues/366) is pending.

# Correct output

As a baseline, here's the expected behavior when running
`args_click.py` with Python.

    $ python args_click.py
    Flags: 1 1.1 False hello red

    $ python args_click.py --b
    Flags: 1 1.1 True hello red

Here's the behavior when running the script with Guild.

    $ NO_IMPORT_FLAGS_CACHE=1 guild run args_click.py -y
    Flags: 1 1.1 False hello red

    $ NO_IMPORT_FLAGS_CACHE=1 guild run args_click.py b=yes -y
    Flags: 1 1.1 True hello red

    $ NO_IMPORT_FLAGS_CACHE=1 guild run args_click.py b=no -y
    Flags: 1 1.1 False hello red

Guild correctly imports the flags.

    $ NO_IMPORT_FLAGS_CACHE=1 guild run args_click.py --help-op
    Usage: guild run [OPTIONS] args_click.py [FLAG]...
    ...
    Flags:
      b  sample flag (default is no)
    ...
