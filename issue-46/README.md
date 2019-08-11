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

### Alternative configuration

The operation `experiment-2` requires `data/file.csv` and links to it
under the `data` path within the run directory. This has a similar
effect to `experiment` in that the file `data/file.csv` is available
to the run. However, in this case `data/file.csv` is the link and
`data` is a new directory that Guild creates for each run.

Run the alternative operation:

    $ guild run experiment-2 -y
    Resolving file:data/file.csv dependency
    Contents of /home/garrett/.guild/runs/e1cace83ee8243ae8e5b444f64c855df/data
    file.csv

List the files for the run:

    $ guild ls
    ~/.guild/runs/e1cace83ee8243ae8e5b444f64c855df:
      data/
      data/file.csv

Note that `file.csv` is displayed because `data` is *not* a link -
it's a directory that Guild creates according to the resource `path`
attribute.

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

## Related topics

- The [Guild copy source test
  project](https://github.com/guildai/guildai/blob/master/guild/tests/samples/projects/copy-sourcecode/guild.yml)
  contains an extensive list of configuration examples.
