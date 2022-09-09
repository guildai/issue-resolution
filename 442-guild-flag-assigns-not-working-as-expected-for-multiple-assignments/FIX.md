---
doctest-type: bash
---

# Fix

Fix is available in 0.8.2.

    #$ guild check -n --version '>=0.8.2'

Guild uses the first assignment for `x` default value.

    $ NO_IMPORT_FLAGS_CACHE=1 guild run test.py --help-op  # doctest: +REPORT_UDIFF
    Usage: guild run [OPTIONS] test.py [FLAG]...
    <BLANKLINE>
    Use 'guild run --help' for a list of options.
    <BLANKLINE>
    Flags:
      x  (default is 1)

This value is provided by default in the underlying Python command.

    $ NO_IMPORT_FLAGS_CACHE=1 guild run test.py --print-cmd
    ??? -um guild.op_main test --x 1

    $ NO_IMPORT_FLAGS_CACHE=1 guild run test.py x=3 --print-cmd
    ??? -um guild.op_main test --x 3

Guild modifies the first assignment.

    $ NO_IMPORT_FLAGS_CACHE=1 guild run test.py x=3 -y
    x=3
    x=2
