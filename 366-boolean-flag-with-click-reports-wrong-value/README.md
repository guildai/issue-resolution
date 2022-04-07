---
doctest-type: bash
---

# boolean flag with click reports wrong value 

https://github.com/guildai/guildai/issues/366

## Problem

Imported flag values appear to be getting inverted somehow.

## Recreating

Requirements:

- guild<=0.8.0
- See [requirements.txt](requirements.txt)

    
    $ guild run -y args-click-default
    Flags: 1 1.1 True hello red
    
    $ guild run -y args-click-default b=True
    Flags: 1 1.1 False hello red

    $ guild run -y args-click-default b=False
    Flags: 1 1.1 True hello red

    $ guild run -y args-click-default b=0
    Flags: 1 1.1 True hello red


    $ guild run -y args-click-default b=1
    Flags: 1 1.1 False hello red

## Workarounds

Invert logic intentionally, I guess?

## Fix

<Describe the fix and the release it's available in. If there's no
thoughts yet to a fix or a fix isn't applicable (e.g. not a bug or
otherwise decide not to fix) state that here.>

## Related Issues

<List any related issues using their full GitHub URL.>
