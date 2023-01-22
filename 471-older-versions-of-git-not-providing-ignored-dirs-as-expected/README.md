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

Clear the test projects.

    $ rm -rf test-repo*

Git `2.31.0` exhibits the OLD behavior.

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

Git `2.32.0` exhibits the NEW behavior.

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
