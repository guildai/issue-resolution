---
doctest-type: bash
---

# How to require multiple files from the same directory in guild.yml?

https://my.guild.ai/t/how-to-require-multiple-files-from-the-same-directory-in-guild-yml/991

This document outlines various approaches to providing datasets to
training runs.

See [`guild.yml`](guild.yml) for project operations.

The examples below can be run using `guild` as follows:

```
$ guild check -t README.md
```

Requirements:

- guild>0.9.0

Check Guild version.

    $ guild check -n --version '>0.9.0'

## Copy data set files from project

While copying files does take up disk space and takes time, it avoids
making a run dependent on a project. The record is more reliable.

The `train-project-files` operation uses explicitly listed files (only
configured files are available to train with):

    $ guild run train-project-files -y
    Resolving file:data/01.npy
    Resolving file:data/02.npy
    .:
    total 8
    ... 01.npy
    ... 02.npy
    ... guild.yml
    ... README.md

`train-project-dir` copies an entire directory (all data files are
available to train with):

    $ guild run train-project-dir -y
    Resolving file:data
    .:
    total 12
    ... data
    ... guild.yml
    ... README.md
    <BLANKLINE>
    ./data:
    total 0
    ... 01.npy
    ... 02.npy

## Use Guild runs to make data set files available

Guild runs can be used to make data sets available. By storing data
set files in a run, those files are independent of the project.

The project illustrates two different patterns:

- Generate a dataset from scratch
- Copy a dataset from a project file to a run for later reuse

### Generate data set from scratch

`prepare-dataset` generates a `data.npy` file. In a real world
example, this operation could be parameterized using flags or
generated using different scripts. Once a dataset is generated in a
run, it can be used by multiple training runs.

    $ guild run prepare-dataset -y
    .:
    total 8
    ... data.npy
    ... guild.yml
    ... README.md

`train-prepared` lists `prepare-dataset` as a dependency. Guild
resolves this dependency by creating a link to the upstream data set
file.

    $ guild run train-prepared -y
    Resolving dataset
    Using run ... for dataset
    .:
    total 8
    ... data.npy -> ../.../data.npy
    ... guild.yml
    ... README.md

The train operation can be run multiple times, using links to the same
data set file.

    $ guild run train-prepared -y
    Resolving dataset
    Using run ... for dataset
    .:
    total 8
    ... data.npy -> ../.../data.npy
    ... guild.yml
    ... README.md

### Copy project data files to a run for later reuse

If a data set already exists in a project, it can be used with this
pattern by copying it to a run using a file dependency. `copy-dataset`
illustrates this.

`copy-dataset` uses a flag to select the applicable data set file.

    $ guild run copy-dataset name=01.npy -y
    Resolving dataset
    .:
    total 8
    ... data.npy
    ... guild.yml
    ... README.md

The `train-copied` operation requires `copy-dataset`.

    $ guild run train-copied -y
    Resolving dataset
    Using run ... for dataset
    .:
    total 8
    ... data.npy -> ../.../data.npy
    ... guild.yml
    ... README.md

Generate a copied data set using `02.npy`.

    $ guild run copy-dataset name=02.npy -y
    Resolving dataset
    .:
    total 8
    ... data.npy
    ... guild.yml
    ... README.md

`train-copied` automatcally used the latest run for `copy-dataset`.

    $ guild run train-copied -y
    Resolving dataset
    Using run ... for dataset
    .:
    total 8
    ... data.npy -> ../.../data.npy
    ... guild.yml
    ... README.md
