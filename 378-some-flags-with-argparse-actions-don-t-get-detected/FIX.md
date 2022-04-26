---
doctest-type: bash
---

# Fix

    $ NO_IMPORT_FLAGS_CACHE=1 guild check -n --version '>0.8.0'

Guild imports the two flags foo and bar:

    $ NO_IMPORT_FLAGS_CACHE=1 guild run test.py --help-op
    Usage: guild run [OPTIONS] test.py [FLAG]...
    Use 'guild run --help' for a list of options.
    Flags:
      bar  (default is no)
           Choices:  yes, no
      foo  (default is yes)
           Choices:  yes, no

Default behavior:

    $ NO_IMPORT_FLAGS_CACHE=1 guild run test.py --print-cmd
    ??? -um guild.op_main test

    $ python test.py
    Namespace(foo=True, bar=False)

    $ NO_IMPORT_FLAGS_CACHE=1 guild run test.py -y
    Namespace(foo=True, bar=False)

Set both flags to true:

    $ NO_IMPORT_FLAGS_CACHE=1 guild run test.py bar=yes foo=yes --print-cmd
    ??? -um guild.op_main test --bar

    $ python test.py --foo --bar
    Namespace(foo=True, bar=True)

    $ NO_IMPORT_FLAGS_CACHE=1 guild run test.py bar=yes foo=yes -y
    Namespace(foo=True, bar=True)

Set both flags to false:

    $ NO_IMPORT_FLAGS_CACHE=1 guild run test.py bar=no foo=no --print-cmd
    ??? -um guild.op_main test --no-foo

    $ python test.py --no-foo --no-bar
    Namespace(foo=False, bar=False)

    $ NO_IMPORT_FLAGS_CACHE=1 guild run test.py bar=no foo=no -y
    Namespace(foo=False, bar=False)
