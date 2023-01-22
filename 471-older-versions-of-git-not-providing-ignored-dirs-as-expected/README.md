---
doctest-type: bash
---

# Older versions of Git not providing ignored dirs as expected

https://github.com/guildai/guildai/issues/471

## Problem

Guild cannot rely on a single command for listing ignores on older
versions of Git.

This project provides a test utility for examining the output of `git
ls-files` to test behavior for a specific version.

Git `2.31.0` exhibits the OLD behavior.

    $ ./test-version 2.31.0
    Testing Git version 2.31.0...
    git ls-files -ioc --exclude-standard --directory
    ------------------------------------------------
    ignored/
    <BLANKLINE>
    git ls-files -ioc --exclude-standard
    ------------------------------------
    ignored/bar.txt
    implicit/foo.txt

Git `2.32.0` exhibits the NEW behavior.

    $ ./test-version 2.32.0
    Testing Git version 2.32.0...
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

    $ ./test-version 2.39.0
    Testing Git version 2.39.0...
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
