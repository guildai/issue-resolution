---
doctest-type: bash
---

# Staged pipeline steps not given labels

https://github.com/guildai/guildai/issues/317

## Problem

Gguild applies labels given to pipelines to each pipeline step when
the pipeline stage is run directly. However, the pipeline is staged
and then run this doesn't happen. Instead only the pipeline operation
receives label, not the steps of the pipeline.

## Recreating

Requirements:

- guild<=0.7.4


## Workarounds

<Describe any way the issue can be worked-around without the
fix. State if there are no known work-arounds.>

## Fix

<Describe the fix and the release it's available in. If there's no
thoughts yet to a fix or a fix isn't applicable (e.g. not a bug or
otherwise decide not to fix) state that here.>

## Related Issues

<List any related issues using their full GitHub URL.>
