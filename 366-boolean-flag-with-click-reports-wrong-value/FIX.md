---
doctest-type: bash
---

# Fix

The fix for [this issue](https://github.com/guildai/guildai/issues/366) is pending.

# Correct output

    $ guild run -y args-click-default
    Flags: 1 1.1 False hello red
    
    $ guild run -y args-click-default b=True
    Flags: 1 1.1 True hello red

    $ guild run -y args-click-default b=False
    Flags: 1 1.1 False hello red

    $ guild run -y args-click-default b=0
    Flags: 1 1.1 False hello red

    $ guild run -y args-click-default b=1
    Flags: 1 1.1 True hello red