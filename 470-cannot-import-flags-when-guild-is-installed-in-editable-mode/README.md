---
doctest-type: bash
---

# Cannot import flags when Guild is installed in editable mode

https://github.com/guildai/guildai/issues/470

## Problem

The root cause is related to [PEP
517](https://peps.python.org/pep-0517/). When Guild is installed using
`--no-use-pep517` flag, the issue is resolved.

[This issue](https://github.com/pypa/pip/issues/6434) addresses the
root cause.

## Recreating

Requirements:

    $ guild check -n --version '<=0.8.2'

Create a virtual env using to test.

    $ python -m venv venv

Install Guild using the `--editable` option. We assume that Guild is
installed in the env var `GUILD_PROJECT` or is otherwise in
`../../guild`.

    $ venv/bin/pip install --editable ${GUILD_PROJECT:-../../guild}
    ???
    <exit 0>

Verify the Guild install.

    $ venv/bin/guild check
    guild_version:             ...
    python_exe:                .../470-cannot-import-flags-when-guild-is-installed-in-editable-mode/venv/bin/python
    ...
    <exit 0>

Use the installed (editable) Guild package to list ops for this project.

    $ venv/bin/guild ops
    WARNING: cannot import flags from guild.pass: No module named guild.pass
    test
    test2

Note the warning - Guild can't find `guild.pass` when importing flags.

This is because Guild is not accessible on the Python system path when
importing flags for `guild.pass`. This does not occur for this
project's `test.py` module.

We're able to run the operations, despite the warning messages.

    $ venv/bin/guild run test -y
    WARNING: cannot import flags from guild.pass: No module named guild.pass
    --msg 'guild.pass runs fine'

    $ venv/bin/guild run test2 -y
    WARNING: cannot import flags from guild.pass: No module named guild.pass
    Local test.py runs fine

## Workarounds

Install Guild as editable using `--no-use-pep517` option.

    $ venv/bin/pip install --editable ${GUILD_PROJECT:-../../guild} --no-use-pep517
    ???
    <exit 0>

    $ venv/bin/guild ops
    test
    test2

    $ venv/bin/guild run test -y
    --msg 'guild.pass runs fine'

    $ venv/bin/guild run test2 -y
    Local test.py runs fine

## Fix

We will not provide a fix for this. See **Workarounds** for a solution.
