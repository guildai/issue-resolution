---
doctest-type: bash
---

# Fix

As of 0.8.2 Guild supports user-defined filter expressions that
support boolean operators 'and' and 'or.

    $ guild check -n --version '>0.8.1'
    <exit 0>

Generate runs of our sample. We generate two runs where a=1 and b=4 so
we can assert below using `-n2`.

    $ guild run filter_test.py a=1 b=4 -y
    a=1 b=4

    $ guild run filter_test.py a=1 b=4 -y
    a=1 b=4

    $ guild run filter_test.py a=2 b=4 -y
    a=2 b=4

The old behavior is still supported.

    $ guild runs -Fl a=1 -Fl b=4 -n2
    [1:...]  filter_test.py  ...  completed  a=2 b=4
    [2:...]  filter_test.py  ...  completed  a=1 b=4

Use `-F` to select runs with labels matching our targets.

    $ guild runs -F "label contains 'a=1' and label contains 'b=4'" -n2
    [1:...]  filter_test.py  ...  completed  a=1 b=4
    [2:...]  filter_test.py  ...  completed  a=1 b=4

Filter expressions may refer to flag values as well. This command
reflects the user intent and does not rely on run labels, which may
not accurately reflect the flag values.

    $ guild runs -F "a=1 and b=4" -n2
    [1:...]  filter_test.py  ...  completed  a=1 b=4
    [2:...]  filter_test.py  ...  completed  a=1 b=4

An expression may further clarify that a value reference applies to a
flag (as opposed to a different run attribute or scalar, which may
have the same name).

    $ guild runs -F "flag:a=1 and flag:b=4" -n2
    [1:...]  filter_test.py  ...  completed  a=1 b=4
    [2:...]  filter_test.py  ...  completed  a=1 b=4

Filters support complex expressions.

    $ guild runs -F "(a = 1 and b = 4) or (a in [0, 2] and b in [4, 5])" -n3
    [1:...]  filter_test.py  ...  completed  a=2 b=4
    [2:...]  filter_test.py  ...  completed  a=1 b=4
    [3:...]  filter_test.py  ...  completed  a=1 b=4

    $ guild runs -F "op = filter_test.py and b = 4" -n3
    [1:...]  filter_test.py  ...  completed  a=2 b=4
    [2:...]  filter_test.py  ...  completed  a=1 b=4
    [3:...]  filter_test.py  ...  completed  a=1 b=4

A filter expression may be combined with other filters.

    $ guild runs -Fo filter_test.py -Fl a=1 -F b=4 -n2
    [1:...]  filter_test.py  ...  completed  a=1 b=4
    [2:...]  filter_test.py  ...  completed  a=1 b=4
