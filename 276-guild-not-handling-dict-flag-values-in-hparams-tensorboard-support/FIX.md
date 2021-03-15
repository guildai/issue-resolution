---
doctest-type: bash
---

# Fix

The steps below can be verified by running `guild check -nt FIX.md`
from this directory.

In 0.7.3rc2 and later, Guild handles dict values by converting them to
strings.

    $ guild check --version '>=0.7.3rc2'
    ...
    <exit 0>

Generate a run with a dict flag val.

    $ guild run test.py x='{foo: 1}' -y
    {'foo': 1}
    <exit 0>

Run the `tensorboard` command. Note succeeds. We don't confirm the
rendered values in TensorBoard this test.

    $ guild tensorboard --test-logdir
    Preparing runs for TensorBoard
    Initialized log dir ...
    <exit 0>
