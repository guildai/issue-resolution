---
doctest-type: bash
---

# Guild not handling dict flag values in hparams TensorBoard support

https://github.com/guildai/guildai/issues/276

Original issue on my.guild.ai:

https://my.guild.ai/t/cannot-open-tensorboard-with-guild-unhashable-type-dict/563

## Problem

Maps are legal values for flags yet Guild does not support map/dict
values in TensorBoard hparam params.

## Recreating

Requirements:

- guild<=0.7.3rc1
- See [requirements.txt](requirements.txt)

The following recreates the issue in Guild versions earlier than
0.7.3rc2. This can be verified by running `guild check -nt README.md`.

    $ guild check --version '<0.7.3rc2'
    ...
    <exit 0>

Generate a run with a dict flag value.

    $ guild run test.py x='{foo: 1}' -y
    {'foo': 1}
    <exit 0>

Show the error using the `--test-logdir` option, which sets up the
hparam summaries for the runs.

    $ guild tensorboard --test-logdir
    Preparing runs for TensorBoard
    Traceback (most recent call last):
      ...
    TypeError: unhashable type: 'dict'
    <exit 1>

## Workarounds

Use `--skip-hparams` with the `tensorboard` command or upgrade to
0.7.3rc2 or later.

## Fix

See [FIX.md](FIX.md).
