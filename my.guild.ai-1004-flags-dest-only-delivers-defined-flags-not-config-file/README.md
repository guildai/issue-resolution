---
doctest-type: bash
---

# Flags-dest only delivers defined flags, not config file

https://my.guild.ai/t/flags-dest-only-delivers-defined-flags-not-config-file/1004

## Problem

<Outline the problem as you see it. This should not be a copy-paste of
the issue as we already have that info.>


## Recreating

Requirements:

- guild<=0.9.0

<Use bash commands with doctest patterns to illustrate the
behavior. If there is an issue, the steps should show the
incorrect/unexpected behavior. If the issue cannot be recreatd, the
steps should show the correct/expected behavior. Use `FIX.md` to show
the steps after a fix has been applied - don't update this section.

To run this file as a test, use `guild check -t README.md`

To run the fix use `guild check -t FIX.md`.

Confirm we're running the version of Guild that replicates the
reported behavior.

    $ guild check -n --version '<=0.9.0'
    <exit 0>

We run `train` with using this command.

    $ guild run train data=test -y

## Workarounds

<Describe any way the issue can be worked-around without the
fix. State if there are no known work-arounds.>

## Fix

<Describe the fix and the release it's available in. If there's no
thoughts yet to a fix or a fix isn't applicable (e.g. not a bug or
otherwise decide not to fix) state that here.>

## Related Issues

<List any related issues using their full GitHub URL.>
