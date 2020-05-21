# Using an exponent as label raises error when filtering runs

https://github.com/guildai/guildai/issues/183

## Problem

Guild does not explicitly save label attrs a strings. If a number is
provided as a label, Guild saves the attribute without quoting the
value.

## Recreating

Requirements:

- guild<=0.7.0.rc9

Change to this directory and run:

    $ guild run test -l 1e6
    $ guild runs -l foo

## Workarounds

<Describe any way the issue can be worked-around without the
fix. State if there are no known work-arounds.>

## Fix

<Describe the fix and the release it's available in. If there's no
thoughts yet to a fix or a fix isn't applicable (e.g. not a bug or
otherwise decide not to fix) state that here.>

## Related Issues

<List any related issues using their full GitHub URL.>
