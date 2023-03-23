---
doctest-type: bash
---

# Confusion on multistep operations, restarting substeps, and copied files?

https://my.guild.ai/t/confusion-on-multistep-operations-restarting-substeps-and-copied-files/998

## Problem

This issue needs to clarify some of Guild's behavior:

- Links vs copies when running steps
- Links vs copies when resolving upstream run dependencies
- Parent run status updates when child step runs are subsequently
  re-run and completed

## Recreating

Requirements:

- guild<=0.9.0

    $ guild check -n --version '<=0.9.0'

## Summary

TODO: summarize above points and list any work we might want to start
on Guild.
