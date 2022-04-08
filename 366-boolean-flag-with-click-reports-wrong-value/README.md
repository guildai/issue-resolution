---
doctest-type: bash
---

# boolean flag with click reports wrong value

https://github.com/guildai/guildai/issues/366

## Problem

Imported flag values appear to be getting inverted somehow.

## Recreating

Requirements:

- guild<=0.8.0

The issue is illustrated by the `args-click-default` operation in the
[`flags` Guild AI
example](https://github.com/guildai/guildai/tree/master/examples/flags). The
applicable code from the example is copied to this project to
reproduce the issue.

The `args-click-default` operation shows how Guild handles flag values
imported from a Click based CLI.

The `arg-click-default` operation runs the
[`args_click.py`](args_click.py) script. When we run this script
directly in Python, we see the defaults.

    $ python args_click.py
    Flags: 1 1.1 False hello red

Note that the third value (boolean) defaults to False. If we run the
script with the `--b` option, it sets this value to True.

    $ python args_click.py --b
    Flags: 1 1.1 True hello red

When we run the script with Guild, Guild mistakenly includes the `--b`
option by default.

    $ NO_IMPORT_FLAGS_CACHE=1 guild run args_click.py --print-cmd
    ??? -um guild.op_main args_click --b --c red --f 1.1 --i 1 --s hello

    $ NO_IMPORT_FLAGS_CACHE=1 guild run args_click.py -y
    Flags: 1 1.1 True hello red

Guild appears to correctly import the default value for `b`.

    $ NO_IMPORT_FLAGS_CACHE=1 guild run args_click.py --help-op
    Usage: guild run [OPTIONS] args_click.py [FLAG]...
    ...
    Flags:
      b  sample flag (default is no)
    ...

This is the same behavior of the `args-click-default` operation, which
runs `args_click.py`.

    $ NO_IMPORT_FLAGS_CACHE=1 guild run args-click-default --print-cmd
    ??? -um guild.op_main args_click -- --b --c red --f 1.1 --i 1 --s hello

    $ NO_IMPORT_FLAGS_CACHE=1 guild run args-click-default -y
    Flags: 1 1.1 True hello red

    $ NO_IMPORT_FLAGS_CACHE=1 guild run args-click-default --help-op
    Usage: guild run [OPTIONS] args-click-default [FLAG]...
    ...
    Flags:
      b  sample flag (default is no)
    ...


## Workarounds

Define the boolean flag and specify `arg-switch: yes`. See
`args-click-default-workaround` in [`guild.yml`](guild.yml).

In this case, Guild correctly omits the `--b` option by default.

    $ NO_IMPORT_FLAGS_CACHE=1 guild run args-click-default-workaround --print-cmd
    ??? -um guild.op_main args_click -- --c red --f 1.1 --i 1 --s hello

The output for the operation is as expected.

    $ NO_IMPORT_FLAGS_CACHE=1 guild run args-click-default-workaround -y
    Flags: 1 1.1 False hello red

Guild correctly determines the default value.

    $ NO_IMPORT_FLAGS_CACHE=1 guild run args-click-default-workaround --help-op
    Usage: guild run [OPTIONS] args-click-default-workaround [FLAG]...
    ...
    Flags:
      b  sample flag (default is no)
    ...

Setting b to yes works as expected.

    $ NO_IMPORT_FLAGS_CACHE=1 guild run args-click-default-workaround b=yes -y
    Flags: 1 1.1 True hello red

Setting b to no explicitly works as expected.

    $ NO_IMPORT_FLAGS_CACHE=1 guild run args-click-default-workaround b=no -y
    Flags: 1 1.1 False hello red

## Fix

Pending

## Related Issues

- https://github.com/guildai/guildai/issues/124
