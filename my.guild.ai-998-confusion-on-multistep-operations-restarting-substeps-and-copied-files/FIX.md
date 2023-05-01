---
doctest-type: bash
---

# Fix

Verify the Guild version.

    $ guild check -n --version '>=0.9.0.dev1'

Delete runs associated with this project.

    $ guild runs rm -y -Ft my.guild.ai-998
    ???
    <exit 0>

The `pipeline` operation in [`guild.yml`](guild.yml) runs two steps:
prepare and train. Each of these steps is configured to fail by
default.

Run the pipeline.

    $ guild run pipeline -y
    INFO: [guild] running prepare: prepare
    Running prepare
    Traceback (most recent call last):...
    AssertionError
    <exit 1>

The pipeline fails because the prepare step fails. The train step is
not run.

    $ guild runs -s -Ft my.guild.ai-998
    [1]  prepare   error  fail=yes
    [2]  pipeline  error

Fix the failed prepare step manually.

    $ guild run --restart `guild select -Fo prepare` fail=no -y
    Running prepare

    $ guild runs -s -Ft my.guild.ai-998
    [1]  prepare   completed  fail=no
    [2]  pipeline  error

Note that this does not affect the pipeline status. There is not way
to change a pipeline status by changing a step status manually. The
pipeline must be restarted and successfully run each step to be
completed.

Restart the pipeline with the `--needed` option. The pipeline skips
the prepare step because it is completed and its flag values are not
changed. It runs train, which fails.

    $ guild run --restart `guild select -Fo pipeline` --needed -y
    INFO: [guild] restarting prepare: ... --needed
    Skipping run because flags have not changed (--needed specified)
    INFO: [guild] running train: train
    Running train
    Traceback (most recent call last):...
    AssertionError
    <exit 1>

    $ guild runs -s -Ft my.guild.ai-998
    [1]  train     error      fail=yes
    [2]  pipeline  error
    [3]  prepare   completed  fail=no

Fix the failed train step manually.

    $ guild run --restart `guild select -Fo train` fail=no -y
    Running train

    $ guild runs -s -Ft my.guild.ai-998
    [1]  train     completed  fail=no
    [2]  pipeline  error
    [3]  prepare   completed  fail=no

Restart the pipeline with the `--needed` option.

    $ guild run --restart `guild select -Fo pipeline` --needed -y
    INFO: [guild] restarting prepare: ... --needed
    Skipping run because flags have not changed (--needed specified)
    INFO: [guild] restarting train: ... --needed
    Skipping run because flags have not changed (--needed specified)

The pipeline operation skips both steps because they're already
completed. The pipeline status is updated to `completed`.

    $ guild runs -s -Ft my.guild.ai-998
    [1]  pipeline  completed
    [2]  train     completed  fail=no
    [3]  prepare   completed  fail=no
