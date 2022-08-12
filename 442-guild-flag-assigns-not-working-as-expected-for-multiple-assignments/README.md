---
doctest-type: bash
---

# Guild flag assigns not working as expected for multiple assignments

https://github.com/guildai/guildai/issues/442

## Problem

<Outline the problem as you see it. This should not be a copy-paste of
the issue as we already have that info.>

## Recreating

Requirements:

- guild<=0.8.1

    $ guild check -n --version '<=0.8.1'

Guild correctly infers the flag `x` and default value `2`.

    $ guild run test.py --help-op
    Usage: guild run [OPTIONS] test.py [FLAG]...
    <BLANKLINE>
    Use 'guild run --help' for a list of options.
    <BLANKLINE>
    Flags:
      x  (default is 2)

This value is provided by default in the underlying Python command.

    $ guild run test.py --print-cmd
    ??? -um guild.op_main test --x 2

    $ guild run test.py x=3 --print-cmd
    ??? -um guild.op_main test --x 3

However, Guild modifies the first assignment

    $ guild run test.py x=3 -y
    x=3
    x=2

Guild should either use the value `1` as the default, or modify the
second assignment, having used `2` as the default. Guild should be
consistent in where it reads and writes flag values.

## Workarounds

Remove (e.g. comment out) subsequent assignments of any scalar,
string, or boolean values.

## Fix

Pending.

Guild must formalize which assignment is both read from and modified,
ensuring that it is the same assignment in both cases.

It is arguably least surprising to use the first assignment and ignore
subsequent assignments. It makes little sense to ignore initial
assignments and modify the last assignment.
