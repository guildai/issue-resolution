---
doctest-type: bash
---

# Fix

    //$ guild check --version '>=0.7.4'
    ...
    <exit 0>

    $ guild run train-thing-1 --help-op
    ...
    Flags:
      sub_thing-var    Default: 8
      width            Default: 10.5

    $ guild run train-thing-2 --help-op
    ...
    Flags:
      sub_thing-iable    Default: 5
      width              Default: 10.5
