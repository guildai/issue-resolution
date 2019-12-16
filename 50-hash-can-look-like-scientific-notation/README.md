# Hash can look like scientific notation

https://github.com/guildai/guildai/issues/50

## Problem

Guild attempts to parse numbers for flag values. A string value '1' is
converted to an integer 1, a value of '1.1' to a float 1.1, etc.

Guild supports conversion of floating point notation as well,
e.g. '3e10' will be successfully parsed as 30000000000.0.

The problem is Guild can't tell the difference between a string that
is meant to be a float expressed using exponent notation and a string
that simply matches the pattern `[0-9]+e[0-9]+`.

Furthermore, even when an explicit string value is provided (e.g. by
enclosing a value in quotes), Guild proceeds to convert it to a float.

## Recreating

Requirements:

- guildai==0.6.6

To recreate, this example uses sample runs in
[`sample-guild-home/runs`](sample-guild-home/runs). In a terminal, set
`GUILD_HOME` to use these runs.

```
$ export GUILD_HOME=sample-guild-homes
```

Run `downstream` with an `upstream` run with a run ID that uses
scientific notation.

```
$ guild run downstream upstream=67217e15
```

Output:

```
You are about to run downstream
  x: 1.2
  upstream: 6.7217e+19
Continue? (Y/n
```

Note that Guild incorrectly represents the run ID as a float.

## Fix

As of Guild 0.7.0.rc4, Guild handles floats that look like short run
IDs as strings.

To recreate, this example uses sample runs in
[`sample-guild-home/runs`](sample-guild-home/runs). In a terminal, set
`GUILD_HOME` to use these runs.

```
$ export GUILD_HOME=sample-guild-homes
```

Run `downstream` with an `upstream` run with a run ID that uses
scientific notation.

```
$ guild run downstream upstream=67217e15
```

Expected output:

```
You are about to run downstream
  upstream: '67217e15'
  x: 1.2
```

Previous to this fix, the prompt for upstream contained `6.7217e+19`
for the run ID.

The `downstream` operation also includes a *float* flag `x`. With the
type specified in the Guild file, flag values for `x` that would
otherwise be treated as run ID strings are treated as floats.

```
$ guild run downstream x=67217e15
```

Expected output:

```
You are about to run downstream
  upstream: '67217e15'
  x: 6.7217e+19
Continue? (Y/n)
```
