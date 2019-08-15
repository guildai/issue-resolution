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

- guildai<=0.6.5

The script [`echo.py`](echo.py) prints a flag value `x` and its
type. The script [`recreate`](recreate) runs multiple operations with
different flag arguments for `x`.

Run:

    $ ./recreate

Output:

    3e563: inf <type 'float'>
    3e10: 30000000000.0 <type 'float'>
    '3e10': 30000000000.0 <type 'float'>
    "3e10": 30000000000.0 <type 'float'>

Note even in the case where a string is explicitly used (last two
cases) Guild converts the value to a float.
