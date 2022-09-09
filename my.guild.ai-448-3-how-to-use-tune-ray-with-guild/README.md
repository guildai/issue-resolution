---
doctest-type: bash
---

# How to use Tune (ray) with Guild

https://my.guild.ai/t/how-to-use-tune-ray-with-guild/448/3

## Problem

How can a user ignore certain output scalars? By default, Guild looks
for a single pattern `(\key): (\value)` in standard output, which will
read all parsable floats in that format?

Is it possible to ignore certain values?

This is not an issue per say, but rather a configure question. This
document provides runnable examples of some approaches.

## Recreating

The sample [Guild file](guild.yml) defined four operations:

    $ guild ops
    default                    Default behavior for output scalars
    exclude-names              Exclude scalars with specified names
    exclude-names-and-pattern  Exclude scalars with specified names and a general pattern
    exclude-pattern            Exclude scalars using a general pattern

Each operation runs [test.py](test.py), which prints scalar values
using various patterns.

    $ python test.py
    foo: 1.123
    bar: 2.234
    baz: 0.012
    [foo]: 3.345
    [bar]: 4.456

The `default` operation captures everything.

    $ guild run default -y
    ...
    <exit 0>

    $ guild runs info
    ...
    scalars:
      [bar]: 4.456000 (step 0)
      [foo]: 3.345000 (step 0)
      bar: 2.234000 (step 0)
      baz: 0.012000 (step 0)
      foo: 1.123000 (step 0)

`exclude-pattern` only captures scalars that aren't formatted inside
square brackets. If the scalars-to-be-excluded happen to be formatted
a specific way, this approach can filter them out.

    $ guild run exclude-pattern -y
    ...
    <exit 0>

    $ guild runs info
    ...
    scalars:
      bar: 2.234000 (step 0)
      baz: 0.012000 (step 0)
      foo: 1.123000 (step 0)

`exclude-names` lists explicit scalar keys that should not be
captured. The general pattern in this case is the default, which
includes square-bracket formatted scalars.

    $ guild run exclude-names -y
    ...
    <exit 0>

    $ guild runs info
    ...
    scalars:
      [bar]: 4.456000 (step 0)
      [foo]: 3.345000 (step 0)
      baz: 0.012000 (step 0)

Finally, `exclude-names-and-pattern` excludes names and also scalars
that are formatted with square brackets.

    $ guild run exclude-names-and-pattern -y
    ...
    <exit 0>

    $ guild runs info
    ...
    scalars:
      baz: 0.012000 (step 0)
    <exit 0>
