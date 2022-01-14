---
doctest-type: bash
---

# Fix

    $ guild check -n --version '>=0.7.5.dev4'

    $ guild run test.py x=loguniform[1e-2:1e-6] -y
    guild: invalid function args in 'x=loguniform[0.01:1e-06]': the lower
    bound 0.01 has to be less than the upper bound 1e-06
    <exit 1>

    $ guild run test.py --optimizer + x=loguniform[1e-2:1e-6] -y
    guild: invalid function args in 'dummy=loguniform[0.01:1e-06]': the lower
    bound 0.01 has to be less than the upper bound 1e-06
    <exit 1>
