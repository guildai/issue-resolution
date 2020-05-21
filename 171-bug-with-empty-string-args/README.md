# Bug with empty string args

https://github.com/guildai/guildai/issues/171

## Problem

Guild is applying incorrect argument encoding when passing an empty
string as a command line argument.

## Recreating

Requirements:

- guild<=0.7.0.rc9

Change to this directory and run:

    $ python test_arg.py --load-model ''
    Namespace(load_model='')

This shows the correct behavior.

With Guild:

    $ guild run test_arg.py load-model=''
    Namespace(load_model="''")

Note that flag decoding and assignment for global variables is
correct:

    $ guild run test_global.py load_model=''
    ''

## Workarounds

None. Please upgrade to 0.7.0.rc10 or later.

## Fix

This is issue is fixed in 0.7.0.rc10.
