---
doctest-type: bash
---

# How to require multiple files from the same directory in guild.yml?

https://my.guild.ai/t/how-to-require-multiple-files-from-the-same-directory-in-guild-yml/991

This document outlines various approaches to providing datasets to
training runs.

Requirements:

- guild<=<applicable Guild version>
- See [requirements.txt](requirements.txt)

Check Guild version.

    $ guild check -n --version '>0.9.0'

## Copy data set files from project

While copying files does take up disk space and takes time, it avoids
making a run dependent on a project. The train record is more
reliable.

Use explicitly listed files (only configured files are available to
train with):

    $ guild run train-project-files -y
    Resolving file:data/01.npy
    Resolving file:data/02.npy
    .:
    total 8
    ... 01.npy
    ... 02.npy
    ... guild.yml
    ... README.md

Copy an entire directory (all data files are available to train with):

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

The project illustrates two different patterns:

- Prepare a dataset from scratch
- Copy a dataset from a project file

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

`train-repared` lists this operation as a dependency. Guild resolves
this dependency by creating a link to the upstream data set file.

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

What if a data set already exists in a project? It can still be used
with this pattern by copying it in a Guild operation. `copy-dataset`
illustrates this.

`copy-dataset` used a flag to select the applicable data set
file. This flag value is used in the requirement spec.

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
