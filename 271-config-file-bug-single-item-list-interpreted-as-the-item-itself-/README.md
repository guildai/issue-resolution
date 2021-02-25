---
doctest-type: bash
---

# Config file bug. Single item list interpreted as the item itself.

https://github.com/guildai/guildai/issues/271

## Problem

Unclear at this time. See *Recreating* below for details.

## Recreating

Requirements:

- guild<=0.7.2

Here's the config file:

    $ cat test.yaml
    a_list:
    - single value

Here's the Python script that loads the config and prints a list value:

    $ cat test.py
    import yaml
    <BLANKLINE>
    with open("test.yaml") as f:
        params = yaml.full_load(f)
    <BLANKLINE>
    print(repr(params["a_list"]))
    <exit 0>

The baseline functionality from Python:

    $ python test.py
    ['single value']

Guild correctly detects the flag:

    $ guild run test --help-op
    Usage: guild run [OPTIONS] test [FLAG]...
    <BLANKLINE>
    Use 'guild run --help' for a list of options.
    <BLANKLINE>
    Flags:
      a_list  (default is '''single value''')

Notably, Guild does detect the list type and sets `arg-split` to true:

    $ guild run test --test-flags 2>/dev/null
    flags-dest: config:test.yaml
    flags-import: yes
    flags:
      a_list:
        default: '''single value'''
        type:
        required: no
        arg-name:
        arg-skip:
        arg-switch:
        arg-split: yes
        env-name:
        choices: []
        allow-other: no
        distribution:
        max:
        min:
        null-label:
    <exit 0>

Here's the result when running the script through Guild:

    $ guild run test -y
    Resolving config:test.yaml dependency
    "'single value'"

The resolved YAML file contains a string value for the list.

    $ guild cat -p test.yaml
    a_list: '''single value'''

Similarly, when we assign a splittable string, Guild fails to split to
a list and instead uses the specified string directly.

    $ guild run test -y a_list="a b c"  # should decode to list [a, b, c]
    Resolving config:test.yaml dependency
    'a b c'

    $ guild cat -p test.yaml
    a_list: a b c

## Workarounds

Guild does not correctly support list types for config files. The
workaround is to use another interface type or use a string value to
encode and decode a list.

The `workaround` operation illustrates how a list can be
encoded/decoded using shell lexcial syntax.

    $ guild run workaround -y
    Resolving config:test2.yaml dependency
    ['single value']

    $ guild run workaround -y encoded_list="a b 'c d'"
    Resolving config:test2.yaml dependency
    ['a', 'b', 'c d']

## Fix

Under development.
