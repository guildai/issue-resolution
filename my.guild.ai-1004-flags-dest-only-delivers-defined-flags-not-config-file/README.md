---
doctest-type: bash
---

# Flags-dest only delivers defined flags, not config file

https://my.guild.ai/t/flags-dest-only-delivers-defined-flags-not-config-file/1004

## Problem

<Outline the problem as you see it. This should not be a copy-paste of
the issue as we already have that info.>


## Recreating

Requirements:

- guild<=0.9.0

Confirm we're running the version of Guild that replicates the
reported behavior.

    $ guild check -n --version '<=0.9.0'
    <exit 0>

`train` is configured to use
`embeddings_and_difficulty/configs_hydra/config.yaml` for the flags
dest. Flags are imported from that configuration file.

    $ guild run train --help-op
    Usage: guild run [OPTIONS] train [FLAG]...
    <BLANKLINE>
    Use 'guild run --help' for a list of options.
    <BLANKLINE>
    Flags:
      data  (default is test)

Run with the default value for `data`.

    $ guild run train -y
    Resolving config:embeddings_and_difficulty/configs_hydra/config.yaml
    data: test

Run with a different value for `data`.

    $ guild run train data=xxx -y
    Resolving config:embeddings_and_difficulty/configs_hydra/config.yaml
    data: xxx

Note that the Hydra enabled application loads the new value for `data`.

The generated config file contains the new flags value.

    $ guild cat -p embeddings_and_difficulty/configs_hydra/config.yaml
    data: xxx
