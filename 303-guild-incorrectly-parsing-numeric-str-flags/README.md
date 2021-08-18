---
doctest-type: bash
---

# Guild incorrectly parsing numeric str flags

https://github.com/guildai/guildai/issues/303

## Problem

Guild does not correctly use the arg parsers option type to infer the
string flag type.

## Recreating

Requirements:

- guild<=0.7.4.rc1

    $ guild check -n --version '<=0.7.4.rc1'

Run `test.py` using a string value for `some_flag` that can be parsed as a number.

    $ guild run -y test.py some_flag=00500
    500

Note that the `some_flag` option is explicitly defined as a `str` type.

    $ fgrep -- --some_flag test.py
    parser.add_argument('--some_flag', type=str, default='')

## Workarounds

Explicitly quote the string value.

    $ guild run -y test.py some_flag="'00500'"
    00500

## Fix

Pending

## Related Issues

None
