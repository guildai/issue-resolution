# Guild treating string as list sometimes

https://github.com/guildai/guildai/issues/193

## Problem

Guild makes it very hard to pass a string value in the format `[...]`
as a flag value.

## Recreating

Requirements:

- guild<=<0.7.0.rc10

Change to this directory and run `test`, which attempts to define a
string value for flag `list_as_string`.

    $ guild run test -y
    ERROR: [guild] uniform requires 2 or 3 args, got ('1,2,3',) for flag list_as_str

This is Guild trying to parse `list_as_str` as a flag function.

## Workarounds

Either avoid using square brackets for lists or upgrade to 0.7.0.rc10.

## Fix

This is fixed in 0.7.0.rc10. In that version it's possible to quote a
list this way:

    $ guild run test list_as_str="'[1,2,3]'"

Or alternatively:

    $ guild run test list_as_str='"[1,2,3]"'

The fix for this issue also applies to [boolean ArgumentParser
arguments with default value reports wrong
value](https://github.com/guildai/guildai/issues/124).

Verify by running:

    $ guild run bool_arg.py foo=False

You should see the correct type printed.

    You are about to run bool_arg.py
      b: no
    Continue? (Y/n)
    Namespace(b=False)

## Related Issues

https://github.com/guildai/guildai/issues/124
