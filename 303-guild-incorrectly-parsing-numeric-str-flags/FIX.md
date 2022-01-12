---
doctest-type: bash
---

# Fix

    $ guild check -n --version '>=0.7.4'

    $ guild run -y test.py some_flag=00500
    00500

Note that the `some_flag` option is explicitly defined as a `str` type.

    $ fgrep -- --some_flag test.py
    parser.add_argument('--some_flag', type=str, default='')
