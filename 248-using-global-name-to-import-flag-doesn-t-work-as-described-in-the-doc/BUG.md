# Incorrect Behavior

Guild does not import the default values for `params`.

Here's the script `op.py`.

    >>> cat("op.py")
    from pprint import pprint
    <BLANKLINE>
    params = {
        "i": 1,
        "f": 1.123,
        "s": "hello",
        "b": True,
        "sub": {
            "i": 2,
            "f": 2.234,
        },
    }
    <BLANKLINE>
    pprint(params)

We expect Guild to import the values defined in `params` as flags.

Here's what Guild sees:

    >>> run("NO_IMPORT_FLAGS_CACHE=1 guild run op --help-op")
    Usage: guild run [OPTIONS] op [FLAG]...
    <BLANKLINE>
    Use 'guild run --help' for a list of options.
    <exit 0>
