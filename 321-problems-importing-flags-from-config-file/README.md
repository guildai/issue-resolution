---
doctest-type: bash
---

# Problems importing flags from config file

https://github.com/guildai/guildai/issues/321

## Problem

Getting the following error when trying to import flags:

```
WARNING: cannot import flags from main.py: TypeError: 'NoneType'
object is not subscriptable (run with guild --debug for details)
```

The issue is with `guild.yml` and `main.py`. See below for a resolution.

## Recreating

Requirements:

- guild<=0.7.5

    $ guild check -n --version '<=0.7.5'

The script [`main.py`](main.py) loads values from a config file and
applies them to `sys.argv` to be parsed. This is interfering with
Guild's use of `--help` when running the script to detect args.

    $ guild run main -y seed=66
    WARNING: cannot import flags from main.py: TypeError: 'NoneType'
    object is not subscriptable (run with guild --debug for details)
    guild: unsupported flag 'seed'
    Try 'guild run main --help-op' for a list of flags or use
    --force-flags to skip this check.
    <exit 1>

## Fix

The fix must be to `guild.yml` and the main script. See `main2`
operation in [`guild.yml`](guild.yml) and [`main2.py`](main2.py).

The `main2` approach differs from `main` as follows:

- Rather than use `options.yml` to generate args to `sys.argv`, use
  them to generate argparse args.

- Use Guild's flags dest support for configuration files (see
  `flags-dest` for the `main2` operations).

This approach uses `options.yml` to drive the flags
interface. `main2.py` uses the values in `option.yml` by default but
allows selective override via command line options. Guild, however,
does not use the command line args interface but rather writes an
updated version of `options.yml` with the user-defined flag
values. `main2.py` pickes these values up as the default values for
the run-specific CLI.

Run with default values (defined in `options.yml`):

    $ NO_WARN_FLAGS_IMPORT=1 guild run main2 -y
    Resolving config:options.yml dependency
    Namespace(seed=42, verbose=True)

    $ guild cat -p options.yml
    seed: 42
    verbose: true

Run with user-defined flag values:

    $ NO_WARN_FLAGS_IMPORT=1 guild run main2 -y seed=66 verbose=no
    Resolving config:options.yml dependency
    Namespace(seed=66, verbose=False)

    $ guild cat -p options.yml
    seed: 66
    verbose: false
