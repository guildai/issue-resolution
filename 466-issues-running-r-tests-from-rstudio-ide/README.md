---
doctest-type: bash
---

# Issues running R tests from RStudio IDE

https://github.com/guildai/guildai/issues/466

## Problem

Not sure - the steps below don't show an issue.

## Recreating

Create a virtual env for the R package Guild installation.

    $ echo "Ensuring Guild install env" && test -d r-guildai ||
    >   ( python -m venv r-guildai &&
    >     r-guildai/bin/python -m pip install --upgrade pip &&
    >     r-guildai/bin/python -m pip install --upgrade
    >        https://api.github.com/repos/guildai/guildai/tarball/HEAD
    >   )
    Ensuring Guild install env...
    <exit 0>

Verify the expected Guild version is running from that env.

    $ r-guildai/bin/guild check -n --version '<=0.8.2'

Run `test.R` directly.

    $ Rscript test.R
    x = 1

Ensure the latest R package for Guild.

    $ mkdir -p r-guildai/R

    $ R_LIBS=r-guildai/R Rscript
    >   -e 'install.packages("remotes")'
    >   -e 'remotes::install_github("t-kalinowski/guildai-r")'
    Installing package into...
    <exit 0>

Run `test.R` with Guild.

    $ R_LIBS=$(realpath r-guildai/R) r-guildai/bin/guild run test.R -y
    ???> x = 1
    > cat("x =", x, "\n")
    x = 1
    >
    >

Note that the plugin runs the script using R's `echo` feature. This
might be surprising for users if we claim that Guild is essentially a
drop-in replacement for `Rscript`. This might be something we enable
with an option but otherwise leave off by default.

For example:

``` command
guild run test.R --echo -y  # and equivalent --no-echo to disable
```

Note also that `R_LIBS` is resolved as an absolute path in the command
above. This is required as Guild changes the current working directory
to the run directory. The R plugin might rewrite `R_LIBS` (and any
other path-related environment variables used by R) with an absolute
path for the run.

When we run the script using a relative path for `R_LIBS` the
operation fails.

    $ R_LIBS=r-guildai/R r-guildai/bin/guild run test.R -y
    Error in loadNamespace(x) : there is no package called ...guildai...
    Calls: loadNamespace -> withRestarts -> withOneRestart -> doWithOneRestart
    Execution halted
    <exit 1>

Run with a different flag value.

    $ R_LIBS=$(realpath r-guildai/R) r-guildai/bin/guild run test.R x=111 -y
    ???> x = 111L
    > cat("x =", x, "\n")
    x = 111
    >
    >

Run a batch.

    $ R_LIBS=$(realpath r-guildai/R) r-guildai/bin/guild run test.R x=[222,333] -y
    INFO: [guild] Running trial ...: test.R (x=222)
    > x = 222L
    > cat("x =", x, "\n")
    x = 222
    >
    >
    INFO: [guild] Running trial ...: test.R (x=333)
    > x = 333L
    > cat("x =", x, "\n")
    x = 333
    >
    >

The last 5 runs:

    $ r-guildai/bin/guild runs -s -n 5
    [1]  test.R  completed  x=333
    [2]  test.R  completed  x=222
    [3]  test.R  completed  x=111
    [4]  test.R  error      x=1.0
    [5]  test.R  completed  x=1.0

## Workarounds

Pending

## Fix

Pending

## Related Issues

Pending
