---
doctest-type: bash
---

# Fix

    $ guild check -n --version '>=0.7.5.dev4'

Both `x` (does not use type annotations) and `y` (does use type
annotations) are supported.

    $ guild run test.ipynb x=10 y=20 -y
    INFO: [guild] Initializing test.ipynb for run
    INFO: [guild] Executing test.ipynb
    z: 30.0
    INFO: [guild] Saving HTML

    $ guild runs info
    id: ...
    flags:
      x: 10
      y: 20.0
    scalars:
      z: 30.000000 (step 0)
