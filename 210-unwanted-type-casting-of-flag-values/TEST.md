# Tests

## Running test.py directly

Given that `x` in [test.py](test.py) is defined using a string type,
Guild should use that when detecting the flag.

    >>> run("guild run test.py --test-flags", ignore="Refreshing")  # doctest: +REPORT_UDIFF
    ### Script flags for test
    reading flags for main spec 'test'
    test.py does not import argparse - assuming globals
    test.py flags imported for dest 'globals':
      x:
        default: '012'
        type: string
    ### Script flags for test.py
    test.py does not import argparse - assuming globals
    test.py flags imported for dest 'globals':
      x:
        default: '012'
        type: string
    flags-dest: globals
    flags-import:
    flags:
      x:
        default: '012'
        type: string
        required: no
        arg-name:
        arg-skip:
        arg-switch:
        env-name:
        choices: []
        allow-other: no
        distribution:
        max:
        min:
        null-label:
    <exit 0>

With type 'string', values for `x` are always decoded as strings:

    >>> run("guild run test.py x=013 -y")
    013 (str)
    <exit 0>

    >>> run("guild run test.py x=001.123 -y")
    001.123 (str)
    <exit 0>

    >>> run("guild run test.py x=no -y")
    no (str)
    <exit 0>

## Running test operation

The `test` operation defined in [guild.yml](guild.yml) redefines the
detected type for `x` as 'auto'. This relaxes the string decoding to
auto-detect using YAML decoding rules.

    >>> run("guild run test --test-flags")  # _doctest: +REPORT_UDIFF
    ### Script flags for test
    reading flags for main spec 'test'
    test.py does not import argparse - assuming globals
    test.py flags imported for dest 'globals':
      x:
        default: '012'
        type: string
    flags-dest: globals
    flags-import:
    flags:
      x:
        default: 13
        type: auto
        required: no
        arg-name:
        arg-skip:
        arg-switch:
        env-name:
        choices: []
        allow-other: no
        distribution:
        max:
        min:
        null-label:
    <exit 0>

With the same flag values as before, the `test` operation converts to
types using YAML rules.

    >>> run("guild run test x=013 -y")
    13 (int)
    <exit 0>

    >>> run("guild run test x=001.123 -y")
    1.123 (float)
    <exit 0>

    >>> run("guild run test x=no -y")
    False (bool)
    <exit 0>
