---
doctest-type: bash
---

# Fix

The fix is available in 0.7.3.rc2 and later.

    $ guild check --version '>=0.7.3.rc2'
    ...
    <exit 0>

Default values:

    $ guild run test -y
    Resolving config:test.yaml dependency
    ['single value']

    $ guild cat -p test.yaml
    a_list:
    - single value

Modified values:

    $ guild run test a_list='a b 1 1.123 "d e" yes' -y
    Resolving config:test.yaml dependency
    ['a', 'b', 1, 1.123, 'd e', True]

    $ guild cat -p test.yaml
    a_list:
    - a
    - b
    - 1
    - 1.123
    - d e
    - true
