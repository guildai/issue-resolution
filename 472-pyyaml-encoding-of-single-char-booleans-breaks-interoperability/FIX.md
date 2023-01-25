---
doctest-type: bash
---

# Fix

The required patch for serialization is illustrated in
`yaml_patched.py`.

    $ python yaml_patched.py
    'n'
    'y'
    'N'
    'Y'

When this behavior is applied in Guild, flags for `op.py` are saved
with the correct quoting of single-char booleans.

    $ guild run op.py -y
    1 + 2 = 3

    $ guild cat -p .guild/attrs/flags
    x: 1
    'y': 2
