---
doctest-type: bash
---

# Nb-replace with boolean value

https://my.guild.ai/t/nb-replace-with-boolean-value/830

## Problem

Guild appears to be working as designed -- see below.

## Recreating

Requirements:

- guild<=<applicable Guild version>
- See [requirements.txt](requirements.txt)

See [test.ipynb](test.ipynb) for a notebook that requires `nb-replace`
for flag support.

See [guild.yml](guild.yml) for configuration that uses a boolean
search/replace within a notebook.

True value (default):

    $ guild run test -y
    INFO: [guild] Initializing test.ipynb for run
    INFO: [guild] Executing test.ipynb
    It is alive!
    INFO: [guild] Saving HTML

    $ guild runs info
    id: ...
    flags:
      x: yes
    ...

True value (explicit):

    $ guild run test x=yes -y
    INFO: [guild] Initializing test.ipynb for run
    INFO: [guild] Executing test.ipynb
    It is alive!
    INFO: [guild] Saving HTML

    $ guild runs info
    id: ...
    flags:
      x: yes
    ...

False value:

    $ guild run test x=no -y
    INFO: [guild] Initializing test.ipynb for run
    INFO: [guild] Executing test.ipynb
    Sad :(
    INFO: [guild] Saving HTML

    $ guild runs info
    id: ...
    flags:
      x: no
    ...
