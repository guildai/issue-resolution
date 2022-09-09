---
doctest-type: bash
---

# Odd flag import behavior involving globals and namespaces

https://github.com/guildai/guildai/issues/450

## Problem

Guild is showing incorrect behavior in the test case below. It's not
clear what the underlying cause is.

## Recreating

Requirements:

- guild<=0.8.1

Guild appears to be importing flags defined in the SimpleNamespace
`test.py:cfg2` for each of the operations, even when the operation
refers to a different global variable.

OB    $ guild help
    ...
    BASE OPERATIONS
    <BLANKLINE>
        namespace
          Flags:
            flag_c  (default is 3)
            flag_d  (default is 4)
    <BLANKLINE>
        plain-class-global
          Flags:
            flag_c  (default is 3)
            flag_d  (default is 4)
    <BLANKLINE>
        plain-class-namespace
          Flags:
            flag_c  (default is 3)
            flag_d  (default is 4)
    <exit 0>

The issue appears to coincide with WARNING messages when the script is
processed.

    $ guild run namespace --test-flags
    ### Script flags for namespace
    reading flags for main spec 'test'
    test.py flags imported for dest 'namespace:cfg2':
      flag_c:
        arg-split: null
        default: 3
        type: number
      flag_d:
        arg-split: null
        default: 4
        type: number
    ### Script flags for plain-class-global
    reading flags for main spec 'test'
    WARNING: cannot import flags for param 'cfg' in 'test.py': param must be a dict or SimpleNamespace (got NoneType)
    test.py flags imported for dest 'global:cfg':
      {}
    ### Script flags for plain-class-namespace
    reading flags for main spec 'test'
    WARNING: cannot import flags for param 'cfg' in 'test.py': param must be a dict or SimpleNamespace (got NoneType)
    test.py flags imported for dest 'namespace:cfg':
      {}
    flags-dest: namespace:cfg2
    flags-import: yes
    flags:
      flag_c:
        default: 3
        type: number
        required: no
        arg-name:
        arg-skip:
        arg-switch:
        arg-split:
        env-name:
        choices: []
        allow-other: no
        distribution:
        max:
        min:
        null-label:
      flag_d:
        default: 4
        type: number
        required: no
        arg-name:
        arg-skip:
        arg-switch:
        arg-split:
        env-name:
        choices: []
        allow-other: no
        distribution:
        max:
        min:
        null-label:

## Workarounds

This is likely a problem that occurs when there's incorrect import
specs and should go away when those issues are fixed.

## Fix

Pending

Guild's designed behavior here could stand a re-think.

1. Why require `namespace:<param>` when `global:<param>` would work,
   provided Guild knew how to handle SimpleNamespace objects?

2. Why doesn't Guild simply set flags as object attributes to *param*
   for `global:<param>` when the param value is not a dict? This would
   provide generalized support for any type of object-based config,
   including SimpleNamespace and plain Python classes.

## Related Issues

This example was prompted by [this
post](https://my.guild.ai/t/python-global-variable-flag-interface/907/3),
calling attention to the common pattern of using a plain Python class
to define config.
