---
doctest-type: bash
---

# Opening source file causes File not found exception

https://my.guild.ai/t/opening-source-file-causes-file-not-found-exception/903/123

## Problem

Guild cannot run scripts that are implemented as Python modules.

## Recreating

Requirements:

- guild<=<applicable Guild version>
- See [requirements.txt](requirements.txt)

    $ python -m pkg.test
    hello

    $ guild run pkg/test.py -y
    Traceback (most recent call last):
    ...
    ModuleNotFoundError: No module named 'pkg'
    <exit 1>

## Workarounds

Currently, use a Guild file to specify `main` as `pkg.module`.

    $ cat guild.yml
    test:
      main: pkg.test
    <exit 0>

    $ guild run test -y
    hello

## Fix

Pending

## Related Issues

None
