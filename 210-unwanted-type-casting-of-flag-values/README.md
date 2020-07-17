# Unwanted type casting of FLAG values

https://github.com/guildai/guildai/issues/210

## Problem

Guild doesn't use flag type when decoding string arguments.

## Recreating

Requirements:

- guild<=0.7.0

The test operation in [guild.yml](guild.yml) defines a single flag `x`
of type `string`.

This command:

```
$ guild run test x=013
```

yields:

```
You are about to run test
  x: '13'
Continue? (Y/n)
```

Guild is decoding '013' using standard YAML decoding and then encoding
using the flag type. Guild should use the flag type to decode the flag
value.

## Workarounds

Strings that are otherwise converted to numbers must be quoted.

```
$ guild run test x="'013'"
```

## Fix

Fix will be available in 0.7.1.

Applied in https://github.com/guildai/guildai/commit/9a1ca9ec

To test, run:

```
$ guild check -nt TEST.md
```
