---
doctest-type: bash
---

# PyYAML encoding of single char booleans breaks interoperability

https://github.com/guildai/guildai/issues/472

## Problem

PyYAML saves single string boolean chars without quotes.

## Recreating

Default YAML encoding of the chars `n`, `y`, `N`, and `Y` (strings):

    $ python yaml_default.py
    n
    y
    N
    Y

These are all technically boolean encodings, as per the [YAML
spec](https://yaml.org/type/bool.html). Parsers that comply with the
YAML spec would decode these as booleans, which is not what Guild
intends when saving these values.

Each character must be quoted to encode it as a string value.

This behavior manifests in Guild's saved attributes. The `op.py`
module defines two flags: `x` and `y`.

    $ guild run op.py -y
    1 + 2 = 3

    $ guild cat -p .guild/attrs/flags
    x: 1
    y: 2

## Workarounds

This problem impacts applications that need to read Guild-saved
YAML-encoded values (e.g. Guild attributes).

There is no good workaround, short of modifying the YAML decoding
behavior in the application.

## Fix

Options:

**1. Patch PyYAML to quote these single char values when encoding values**

Pros:

 - Guild-generated YAML-encoded values are correctly encoded (supports
   interoperability)

Cons:

 - Ambiguity

**2. When writing YAML-encoded files, write a JSON sidecar**

Pros:

- Other applications can read Guild-generated values using JSON

Cons:

- Duplication of serialization cost
- Possibility of drift between YAML and JSON values

**3. Switch to using JSON for saving files**

Pros:

- Efficient cross-language interoperability

Cons:

- Lose the ability to diff changes by line
- Maintenance of two schemes (backward compatibility)

**4. Provide an efficient Python-based decoding utility (e.g. to
     return run attributes as JSON)**

Pros:

- Guild as black-box function to read values (insulates external
  applications from future changes)

- Supports applications that don't have YAML support

Cons:

- Likely less efficient than reading the YAML directly

- Runs are no longer independent of a Guild specific library (fatal
  flaw)

### Analysis

Option 4 is out -- we cannot build dependency on a Guild specific
library.

Option 3 is appealing -- it addresses the serialization problems that
come up with the complex and over wrought YAML standard. As Guild run
attributes are not user facing (i.e. users are not expected to view or
edit them) a JSON format is probably acceptable.

Option 2 could be a stop-gap measure if Option 1 wasn't straight
forward or presented downsides.

Option 1 would appear to solve the underlying problem without
downsides.
