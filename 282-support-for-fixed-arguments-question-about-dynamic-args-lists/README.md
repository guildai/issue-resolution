---
doctest-type: bash
---

# Support for fixed arguments / question about dynamic args lists?

https://github.com/guildai/guildai/issues/282

## Problem

Guild does not use the op spec args when importing flags from
argparse/click. This makes it impossible to use sub-command based
opspecs.

## Recreating

Requirements:

- guild<=0.7.3
- See [requirements.txt](requirements.txt)

    $ guild check --version '<0.7.4'
    ...
    <exit 0>

`test.py` dynamically generates options based on previous
options. This is similar to Python's sub-commands in argparse.

Here's the script for `thing1`:

    $ python test.py --sub_thing thing1 --help
    usage: test.py [-h] [--width WIDTH] [--sub_thing SUB_THING] [--sub_thing-var SUB_THING-VAR]
    <BLANKLINE>
    optional arguments:
      -h, --help            show this help message and exit
      --width WIDTH         Default: 10.5
      --sub_thing SUB_THING
                            Inferred 'thing1'; help shown corresponds to that option. Switch accepting: ['thing1', 'thing2']...
      --sub_thing-var SUB_THING-VAR
                            Default: 8

Here's the script for `thing2`:

    $ python test.py --sub_thing thing2 --help
    usage: test.py [-h] [--width WIDTH] [--sub_thing SUB_THING] [--sub_thing-iable SUB_THING-IABLE]
    <BLANKLINE>
    optional arguments:
      -h, --help            show this help message and exit
      --width WIDTH         Default: 10.5
      --sub_thing SUB_THING
                            Inferred 'thing2'; help shown corresponds to that option...
      --sub_thing-iable SUB_THING-IABLE
                            Default: 5

Even when a `main` spec is `test --sub_thing thing1`, Guild reads only
the top-level options.

    $ guild run train-thing-1 --help-op
    ...
    Flags:
      width    Default: 10.5

    $ guild run train-thing-2 --help-op
    ...
    Flags:
      width    Default: 10.5

## Workarounds

Upgrade to 0.7.4. Otherwise wrap the scripts with another script that
Guild can inspect.

## Fix

See [FIX.md](FIX.md) for steps to verify.

Use base args in the main spec when getting importing flags via `args`
and `args:click`.

## Related Issues

- https://github.com/guildai/guildai/issues/89
