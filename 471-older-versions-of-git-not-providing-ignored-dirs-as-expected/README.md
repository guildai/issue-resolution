---
doctest-type: bash
---

# Older versions of Git not providing ignored dirs as expected

https://github.com/guildai/guildai/issues/471

## Problem

Guild cannot rely on a single command for listing ignores on older
versions of Git.

This project provides a [test utility](test-version) for examining the
output of `git ls-files` to test behavior for a specific version.

The *NEW* (desired) behavior is available in Git 2.32 and later. The
tests below show this.

Clear the test projects.

    $ rm -rf test-repo*

### `2.31.0` - OLD behavior

    $ ./test-version 2.31.0  # doctest: +REPORT_UDIFF
    Testing Git version 2.31.0...
    Project layout
    --------------
    .
    ./.git
    ./.gitignore
    ./implicit
    ./implicit/foo.txt
    ./ignored
    ./ignored/bar.txt
    <BLANKLINE>
    .gitignore
    ----------
    *.txt
    ignored
    <BLANKLINE>
    git ls-files -ioc --exclude-standard --directory
    ------------------------------------------------
    ignored/
    <BLANKLINE>
    git ls-files -ioc --exclude-standard
    ------------------------------------
    ignored/bar.txt
    implicit/foo.txt

    $ PATH=$(realpath git-2.31.0):$PATH guild check --external git-ls-files
    warning: templates not found in ...
    guild: git-ls-files NOT OK (git version 2.31.0; .../git-2.31.0/git)
    unexpected output for ls-files:
    <exit 1>

### `2.32.0` NEW behavior

    $ ./test-version 2.32.0  # doctest: +REPORT_UDIFF
    Testing Git version 2.32.0...
    Project layout
    --------------
    .
    ./.git
    ./.gitignore
    ./implicit
    ./implicit/foo.txt
    ./ignored
    ./ignored/bar.txt
    <BLANKLINE>
    .gitignore
    ----------
    *.txt
    ignored
    <BLANKLINE>
    git ls-files -ioc --exclude-standard --directory
    ------------------------------------------------
    ignored/
    implicit/
    implicit/foo.txt
    <BLANKLINE>
    git ls-files -ioc --exclude-standard
    ------------------------------------
    ignored/bar.txt
    implicit/foo.txt

    $ PATH=$(realpath git-2.32.0):$PATH guild check --external git-ls-files
    warning: templates not found in ...
    git-ls-files is ok (git version 2.32.0; .../git-2.32.0/git)

Git `2.39.0` exhibits the NEW behavior.

    $ ./test-version 2.39.0  # doctest: +REPORT_UDIFF
    Testing Git version 2.39.0...
    Project layout
    --------------
    .
    ./.git
    ./.gitignore
    ./implicit
    ./implicit/foo.txt
    ./ignored
    ./ignored/bar.txt
    <BLANKLINE>
    .gitignore
    ----------
    *.txt
    ignored
    <BLANKLINE>
    git ls-files -ioc --exclude-standard --directory
    ------------------------------------------------
    ignored/
    implicit/
    implicit/foo.txt
    <BLANKLINE>
    git ls-files -ioc --exclude-standard
    ------------------------------------
    ignored/bar.txt
    implicit/foo.txt

    $ PATH=$(realpath git-2.39.0):$PATH guild check --external git-ls-files
    warning: templates not found in ...
    git-ls-files is ok (git version 2.39.0; .../git-2.39.0/git)
