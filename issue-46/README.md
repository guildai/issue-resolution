# How to use data files from local filesystem

https://github.com/guildai/guildai/issues/46

This project contains a layout similar to that described in the issue.

Refer to [`guild.yml`](guild.yml) for project configuration.

## Running examples

Requirements:

- guildai>=0.6.5

Run the `experiment` operation, which simply lists the files in the
`DATA_DIR`:

    $ guild run experiment -y
    Resolving file:data dependency
    Contents of ~/.guild/runs/bcdce3b8901c4fcbb85d139c5c28f0a8/data
    file.csv

List the files for the run:

    $ guild ls
    ~/.guild/runs/60aaa3e9f6064fe1864a35ce6bf25a71:
      data/

Note that `data/` in this case is a symlink. By default, Guild does
not follow links when listing files. To show files under `data/`, use
the `-L, --follow-links` option:

    $ guild ls -L
    ~/.guild/runs/60aaa3e9f6064fe1864a35ce6bf25a71:
      data/
      data/file.csv

### Alternative configuration - using `path`

The operation `experiment-2` requires `data/file.csv` and links to it
under the `data` path within the run directory. This has a similar
effect to `experiment` in that the file `data/file.csv` is available
to the run. However, in this case `data/file.csv` is the link and
`data` is a new directory that Guild creates for each run.

Run the alternative operation:

    $ guild run experiment-2 -y
    Resolving file:data/file.csv dependency
    Contents of ~/.guild/runs/e1cace83ee8243ae8e5b444f64c855df/data
    file.csv

List the files for the run:

    $ guild ls
    ~/.guild/runs/e1cace83ee8243ae8e5b444f64c855df:
      data/
      data/file.csv

Note that `file.csv` is displayed because `data` is *not* a link -
it's a directory that Guild creates according to the resource `path`
attribute.

### Alternative configuration - using named resources

`experiment` and `experiment-2` both use inlined resource definitions
under `requires`. You can alternatively use a *named resource* as is
shown in `experiment-3`.

Run `experiment-3`:

    $ guild run experiment-3 -y
    Resolving data dependency
    Contents of ~/.guild/runs/3ea673ed6b454e1a8b771e6b8867ab99/data
    file.csv

List the run files:

    $ guild runs ls
    ~/.guild/runs/3ea673ed6b454e1a8b771e6b8867ab99:
      data/

Note that this configuration links to `data` and so does not show
`file.csv` by default.

List the run files following links:

    $ guild runs ls -L
    ~/.guild/runs/3ea673ed6b454e1a8b771e6b8867ab99:
      data/
      data/file.csv

### Staging runs

It's important to generate the correct run directory layout. Guild
lets you create a staged run without running the operation. This is
helpful for verifying run directory layout and debugging issues.

Use the `--stage` option with the `run` command:

    $ guild run experiment --stage /tmp/guild-issue-46-stage -y
    Resolving file:data dependency
    Operation is staged in /tmp/guild-issue-46-stage
    To run the operation, use: (cd /tmp/guild-issue-46-stage && source
    .guild/env && /usr/bin/python -um guild.op_main experiment --
    --DATA_DIR data)

You can inspect the directory `/tmp/guild-issue-46-stage` and fix any
issue before running the operation.

### List source code files

To list the source code files for any run, use the `-s, --source`
option with `ls`:

    $ guild ls -s
    .guild/sourcecode/
    .guild/sourcecode/README.md
    .guild/sourcecode/experiment.py
    .guild/sourcecode/guild.yml

The model `topic_model` excludes everything in the `data`
directory. All other text files are copied as source code. To exclude
additional files or paths, add them to the `sourcecode` list using the
same `exclude` directives. To include binaries, add the applicable
specs as `include` directives.

`sourcecode` config can be defined at the model level, operation
level, or both. If defined at both levels, the operation config
extends the model config.

Use the `--test-sourcecode` option to the `run` command to check which
files Guild will copy based on the source code configuration for the
applicable operation.

    $ guild run experiment --test-sourcecode
    Copying from the current directory
    Selected for copy:
      ./README.md
      ./experiment.py
      ./guild.yml
    Skipped:
      ./data/file.csv

## Related topics

- The [Guild copy source test
  project](https://github.com/guildai/guildai/blob/master/guild/tests/samples/projects/copy-sourcecode/guild.yml)
  contains an extensive list of configuration examples.

- The [Guild copy source test
  script](https://github.com/guildai/guildai/blob/master/guild/tests/copy-sourcecode.md)
  contains annotated tests that run the test project examples.
