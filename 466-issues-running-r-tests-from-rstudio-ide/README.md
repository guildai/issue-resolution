---
doctest-type: bash
---

# Issues running R tests from RStudio IDE

https://github.com/guildai/guildai/issues/466

## Problem

When running a batch from an activated virtual env that does not have
Guild installed using Guild installed in a virtual environment, the
operation fails with `click` module not found.

Missing `click` indicates that Guild source code is available but
Guild's required packages are not installed.

When Guild runs a Python script/module, including its own internal
main modules, it modifies the `PYTHONPATH` used in the call to the
Python executable to include its location. With this issue, Guild may
be incorrectly inferring its install location or it may otherwise by
incorrectly constructing the `PYTHONPATH` for the batch call, which is
implemented by `guild.batch_main`.

## Recreating

Create a virtual env for Guild. This is where we run Guild from.

    $ echo "Ensuring Guild app env" && test -d guild-app-env ||
    >   ( python -m venv guild-app-env &&
    >     guild-app-env/bin/python -m pip install --upgrade pip &&
    >     guild-app-env/bin/python -m pip install --upgrade
    >        https://api.github.com/repos/guildai/guildai/tarball/HEAD
    >   )
    Ensuring Guild app env...
    <exit 0>

Use project-local `.guild` as Guild home.

    $ export GUILD_HOME=.guild

Verify that Guild is available from the environment.

    $ guild-app-env/bin/guild check --version '<=0.8.2'
    guild_version:             ...
    guild_install_location:    .../466-issues-running-r-tests-from-rstudio-ide/guild-app-env/lib/.../site-packages/guild
    guild_home:                .../466-issues-running-r-tests-from-rstudio-ide/.guild
    guild_resource_cache:      .../466-issues-running-r-tests-from-rstudio-ide/.guild/cache/resources
    ...
    <exit 0>

Delete any previous runs.

    $ guild-app-env/bin/guild runs rm -y
    ...
    <exit 0>

Create a virtual environment for a project.

    $ echo "Ensuring project env" && test -d project-env ||
    >   ( python -m venv project-env &&
    >     project-env/bin/python -m pip install --upgrade pip
    >   )
    Ensuring project env...
    <exit 0>

Run a batch of two trials of `test.sh` with the following conditions:

  - The project env is activated
  - Guild is run from the Guild app env
  - Guild is not available on the path

    $ . project-env/bin/activate &&
    > PATH="/usr/bin" &&
    > echo "VIRTUAL_ENV: ${VIRTUAL_ENV-<unset>}" &&
    > echo "PYTHONPATH: ${PYTHONPATH-<unset>}" &&
    > echo "guild on path: $(which guild || echo '<not available>')" &&
    > echo "---" &&
    > guild-app-env/bin/guild run test.sh x=[1,2] --force-flags --keep-batch -y
    VIRTUAL_ENV: .../466-issues-running-r-tests-from-rstudio-ide/project-env
    PYTHONPATH: <unset>
    guild on path: <not available>
    ---
    INFO: [guild] Running trial ...: test.sh (x=1)
    x = 1
    INFO: [guild] Running trial ...: test.sh (x=2)
    x = 2

Show the runs generated for the batch.

    $ guild-app-env/bin/guild runs -s
    [1]  test.sh   completed  x=2
    [2]  test.sh   completed  x=1
    [3]  test.sh+  completed

The batch run requires `PYTHONPATH` because it runs
`guild.batch_main`. The path only include `site-packages` from the
Guild app env.

The batch command:

    $ guild-app-env/bin/guild cat 3 -p .guild/attrs/cmd
    - .../466-issues-running-r-tests-from-rstudio-ide/project-env/bin/python
    - -um
    - guild.batch_main

Verify the start of the `PYTHONPATH` value, which should include the
current directory (i.e. the run directory). We use a helper script to
make a more precise assertion.

    $ python -m check_python_path $(guild-app-env/bin/guild select --path 3) guild-app-env
    Python path ok: ...

The two trials should not be run with `PYTHONPATH` because they're not
Python scripts.

The trial commands:

    $ guild-app-env/bin/guild cat 2 -p .guild/attrs/cmd
    - .../466-issues-running-r-tests-from-rstudio-ide/test.sh

    $ guild-app-env/bin/guild cat 1 -p .guild/attrs/cmd
    - .../466-issues-running-r-tests-from-rstudio-ide/test.sh

The `PYTHONPATH` used for each trial:

    $ guild-app-env/bin/guild cat 2 -p .guild/attrs/env | grep PYTHONPATH
    PYTHONPATH: .:.../466-issues-running-r-tests-from-rstudio-ide/guild-app-env/lib/.../site-packages

    $ guild-app-env/bin/guild cat 1 -p .guild/attrs/env | grep PYTHONPATH
    PYTHONPATH: .:.../466-issues-running-r-tests-from-rstudio-ide/guild-app-env/lib/.../site-packages

NOTE: This is incorrect behavior! The `PYTHONPATH` should NOT be set
for the trials. This appears to occur only when we run the trials as
batches. If we run a single tria directly, `PYTHONPATH` is not
set. This is the correct, expected behavior.

Run `test.sh` directly (not in a batch).

    $ . project-env/bin/activate &&
    > PATH="/usr/bin" &&
    > echo "VIRTUAL_ENV: ${VIRTUAL_ENV-<unset>}" &&
    > echo "PYTHONPATH: ${PYTHONPATH-<unset>}" &&
    > echo "guild on path: $(which guild || echo '<not available>')" &&
    > echo "---" &&
    > guild-app-env/bin/guild run test.sh x=3 --force-flags -y
    VIRTUAL_ENV: .../466-issues-running-r-tests-from-rstudio-ide/project-env
    PYTHONPATH: <unset>
    guild on path: <not available>
    ---
    x = 3

Show the runs.

    $ guild-app-env/bin/guild runs -s
    [1]  test.sh   completed  x=3
    [2]  test.sh   completed  x=2
    [3]  test.sh   completed  x=1
    [4]  test.sh+  completed

Confirm that the latest run does not use `PYTHONPATH`.

    $ guild-app-env/bin/guild cat -p .guild/attrs/cmd
    - .../466-issues-running-r-tests-from-rstudio-ide/test.sh

    $ guild-app-env/bin/guild cat -p .guild/attrs/env | grep PYTHONPATH
    <exit 1>

## Notes

The spurious `PYTHONPATH` appearing in the trials is almost certainly
due to `PYTHONPATH` to `guild.batch_main` being passed through to the
trial runs. This would be by design as Guild explicitly passes
`PYTHONPATH` provided to the run command through to the run. See the
builtin `pythonpath` test (located in the Guild source as
`guild/tests/pythonpath.md`) for detailed coverage of this topic.

In any case, this would not appear to explain why `click` cannot be
found under some circumstances. The batch run above does in fact
succeed. That `PYTHONPATH` is defined for `test.sh` should not pose a
problem - it should go as unread environment for that run.

We've observed `guild.batch_main` being run with the project
environment in `PYTHONPATH`. *This* is causing the `click` error. The
question we haven't answered is why Guild is using the the wrong
location for its packages in that case.

## Workarounds

Pending

## Fix

Pending

## Related Issues

Pending
