# Handle parents parser correctly

https://github.com/guildai/guildai/issues/164

## Problem

Guild's method of detecting flags from argparse is overly complex and
brittle.

## Recreating

Requirements:

- guild<=0.7.0.rc9

To recreate, change to this directory and run:

    $ guild run argparse-parent-test

Incorrect output:

    You are about to run argparse-parent-test
      sub-float: 2.2
      sub-int: 2
    Continue? (Y/n) n

Running `main.py` directly:

    $ python main.py --help
    usage: main.py [-h] [--main-int MAIN_INT] [--main-float MAIN_FLOAT]
                   [--sub-int SUB_INT] [--sub-float SUB_FLOAT]

    optional arguments:
      -h, --help            show this help message and exit
      --main-int MAIN_INT
      --main-float MAIN_FLOAT
      --sub-int SUB_INT
      --sub-float SUB_FLOAT

Guild should detect `main-int` and `main-float`.

Expected Guild output:

    $ guild run argparse-parent-test
    You are about to run argparse-parent-test
      main-float: 1.2
      main-int: 1
      sub-float: 2.2
      sub-int: 2
    Continue? (Y/n)

## Workarounds

None. Please upgrade to 0.7.0.rc10 or later.

## Related Issues

- https://github.com/guildai/guildai/issues/147
