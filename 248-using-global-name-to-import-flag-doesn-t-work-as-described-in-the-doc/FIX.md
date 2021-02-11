# Verify Fix

Guild correctly imports all flags from the `params` global defined in
`op.py`.

    >>> run("NO_IMPORT_FLAGS_CACHE=1 guild run op --help-op")
    Usage: guild run [OPTIONS] op [FLAG]...
    <BLANKLINE>
    Use 'guild run --help' for a list of options.
    <BLANKLINE>
    Flags:
      b      (default is yes)
      f      (default is 1.123)
      i      (default is 1)
      s      (default is hello)
      sub.f  (default is 2.234)
      sub.i  (default is 2)
    <exit 0>
