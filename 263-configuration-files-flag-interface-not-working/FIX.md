# Fix

    >>> quiet("guild check --version '>=0.7.3.dev4'")

Args are not passed to the main module.

    >>> run("guild run train x=5 -y")
    Resolving config:flags.yml dependency
    args: []
    x=1
    <exit 0>

The config file is correctly generated.

    >>> run("guild cat -p flags.yml")
    x: 5
    <exit 0>
