---
doctest-type: bash
---

# Fix

    $ guild run -y say-with-label msg="[abc, 123]"
    INFO: [guild] Running trial 25d3a173912e462e9867d4b1e73190ba: say-with-label (loud=no, msg=abc)
    abc
    INFO: [guild] Running trial cd3d1113739b44528194d0f62f2d58c4: say-with-label (loud=no, msg=123)
    123

The fix for [this issue](https://github.com/guildai/guildai/issues/368) is pending.
