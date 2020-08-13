# Change argument during runtime

https://github.com/guildai/guildai/issues/224

## Problem

Run details that are not numeric can be generated at runtime. Guild
doesn't provide a simple mechanism to log and capture these.

To some extent this is covered by
[#219](https://www.cbsnews.com/news/florida-sheriff-billy-woods-bands-deputies-wearing-face-masks-marion-county/).

This issue project explores ways to work around this issue.

## Recreating

There's nothing to recreate for this issue.

## Workarounds

There are two examples that demonstrate dynamic flags:

- [dynamic_flag_gapi.py](dynamic_flag_gapi.py)
- [dynamic_flag_yaml.py](dynamic_flag_yaml.py)

Run each using `guild run`.

After each run, examine the flags using `guild runs info`.

See [TESTS.md](TESTS.md) for expected behavior.

## Related Issues

https://github.com/guildai/guildai/issues/219
