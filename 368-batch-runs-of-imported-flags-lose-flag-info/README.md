---
doctest-type: bash
---

# Batch runs of imported flags lose flag info

https://github.com/guildai/guildai/issues/368

## Problem

Boolean flags in particular require that the OpCmd flags are set when we emit 
the command line flag strings. Without this knowledge, we treat the boolean flag
as a normal flag (one that takes a value argument), and this is wrong. When 
running a batch that uses imported flags, we seem to not re-populate the OpCmd 
object correctly, losing the flag information that was imported from the script.
This then leads to incorrect handling of the boolean flag, generally resulting in
confusing about arguments that are not understood because they're not supposed to
be there.

## Recreating

Requirements:

- guild<=0.8.0
- See [requirements.txt](requirements.txt)

This is not reproducible without https://github.com/guildai/guildai/pull/367, which
fixes a logic inversion with argparse store_true and store_false flags. In particular,
the logic inversion at https://github.com/guildai/guildai/pull/367/files#diff-123520f84fa1e4ae36c2411e19d16258223d94a4be3f66a7220cd4d12fd5fefaR115
breaks a lot of implicit filtering that has been happening.

<Use bash commands with doctest patterns to illustrate the
behavior. If there is an issue, the steps should show the
incorrect/unexpected behavior. If the issue cannot be recreatd, the
steps should show the correct/expected behavior. Use `FIX.md` to show
the steps after a fix has been applied - don't update this section.>

    $ guild run -y say-with-label msg="[abc, 123]"
    INFO: [guild] Running trial 25d3a173912e462e9867d4b1e73190ba: say-with-label (loud=no, msg=abc)
    usage: say.py [-h] [--msg MSG] [--loud]
    say.py: error: unrecognized arguments: 
    ERROR: [guild] Trial 25d3a173912e462e9867d4b1e73190ba exited with an error (2) - see log for details
    INFO: [guild] Running trial cd3d1113739b44528194d0f62f2d58c4: say-with-label (loud=no, msg=123)
    usage: say.py [-h] [--msg MSG] [--loud]
    say.py: error: unrecognized arguments: 
    ERROR: [guild] Trial cd3d1113739b44528194d0f62f2d58c4 exited with an error (2) - see log for details
    
The unrecognized arguments are empty strings that are being passed explicitly as arguments 
to the "loud" boolean flag, because at the time of generating the CLI output strings, we don't have the
flag info: https://github.com/guildai/guildai/blob/master/guild/op_cmd.py#L111-L115

Instead, we fall through to https://github.com/guildai/guildai/blob/master/guild/op_cmd.py#L121-L123, 
which is what gives us the empty string.

## Workarounds

<Describe any way the issue can be worked-around without the
fix. State if there are no known work-arounds.>

None known.

## Fix

Proposed fix is to propagate OpCmd flag objects from the initial batch parsing pass into each run,
such that any boolean flag default values carry through correctly. Alternatively, force re-parsing
a source file if we detect that parameters are being imported.

<Describe the fix and the release it's available in. If there's no
thoughts yet to a fix or a fix isn't applicable (e.g. not a bug or
otherwise decide not to fix) state that here.>

## Related Issues

https://github.com/guildai/guildai/issues/366