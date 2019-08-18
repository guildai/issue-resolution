# Sourcecode snapshots not selecting specified files

https://github.com/guildai/guildai/issues/39

## Recreating issue

The steps below demonstrate correct functionality as of
`0.6.6.dev2`. Earlier versions may report different results.

Requirements:

- guildai>=0.6.6.dev2

Note that you'll have to install Guild with the `--pre` option
(e.g. `pip install guildai --pre`) if `0.6.6` is not yet released. You
can check the latest version of Guild by running `guild check`.

Run `./setup` in this directory. This will create a root directory
`/tmp/guild-issue-39` containing source code file candidates.

Note that the source code root in [`guild.yml`] is
`/tmp/guild-issue-39`.

To simulate the example from issue 39, run:

    $ guild run from-issue --test-sourcecode
    Copying from /tmp/guild-issue-39
    Selected for copy:
      ../../../../../tmp/guild-issue-39/domains/gym_taxi/hello.py
      ../../../../../tmp/guild-issue-39/symbolic-goal-generation/guild.yml
      ../../../../../tmp/guild-issue-39/symbolic-goal-generation/hello.py
      ../../../../../tmp/guild-issue-39/symbolic-goal-generation/planning/taxi/hello.pddl
    Skipped:
      ../../../../../tmp/guild-issue-39/DRL/hello.bin
      ../../../../../tmp/guild-issue-39/DRL/hello.py
      ../../../../../tmp/guild-issue-39/domains/gym_taxi/hello.bin

Note that the relative paths displayed depend on where you're running
this example.

The operation `relative-paths` ensures that all included paths are
relative to the root (Guild will not evaluate files that are located
outside of the root directory).

Test the source code copy:

    $ guild run relative-paths --test-sourcecode
    Copying from /tmp/guild-issue-39
    Selected for copy:
      ../../../../../tmp/guild-issue-39/DRL/hello.py
      ../../../../../tmp/guild-issue-39/domains/gym_taxi/hello.py
      ../../../../../tmp/guild-issue-39/symbolic-goal-generation/guild.yml
      ../../../../../tmp/guild-issue-39/symbolic-goal-generation/hello.py
      ../../../../../tmp/guild-issue-39/symbolic-goal-generation/planning/taxi/hello.pddl
    Skipped:
      ../../../../../tmp/guild-issue-39/DRL/hello.bin
      ../../../../../tmp/guild-issue-39/domains/gym_taxi/hello.bin

Note that in the `relative-paths` the file
`/tmp/guild-issue-39/DRL/hello.py` is copied.

To confirm that the files are copied for each run:

    $ guild run from-issue -y
    $ guild ls --sourcecode

and:

    $ guild run relative-paths -y
    $ guild ls --sourcecode

## Resolution

This example relies on a new implementation of Guild's source code
copy engine and so may not reflect the behavior described in the
issue.

Note also that the `--test-sourcecode` option is new as of
`0.6.6.dev2`.
