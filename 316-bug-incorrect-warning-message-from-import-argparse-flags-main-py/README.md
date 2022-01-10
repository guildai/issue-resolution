---
doctest-type: bash
---

# [Bug] Incorrect warning message from import_argparse_flags_main.py

https://github.com/guildai/guildai/issues/316

## Problem

The import main module isn't handling its arguments correctly.

## Recreating

Requirements:

- guild<=0.75

    $ guild run test --help-op
    WARNING: cannot import flags from .../test.py:
    usage: import_argparse_flags_main.py [-h] mod_path package base_args output_path
    import_argparse_flags_main.py: error: the following arguments are required: output_path
    Usage: guild run [OPTIONS] test [FLAG]...
    <BLANKLINE>
    Use 'guild run --help' for a list of options.

## Workarounds

None. Upgrade to >=0.7.5.dev4

## Fix

Don't use argparse to parse the four required args to the import main
module - just grab the vals from sys.argv.

## Related Issues

None
