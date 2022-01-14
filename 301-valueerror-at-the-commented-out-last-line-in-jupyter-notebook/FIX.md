---
doctest-type: bash
---

# Fix

    $ guild check -n --version '>=0.7.5.dev4'

    $ guild run test.ipynb -y
    INFO: [guild] Initializing test.ipynb for run
    INFO: [guild] Executing test.ipynb
    INFO: [guild] Saving HTML
    <exit 0>

    $ guild runs info
    id: ...
    flags:
      n_epoch: 0
    scalars:
    <exit 0>
