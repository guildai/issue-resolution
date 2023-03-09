---
doctest-type: bash
---

# Fix

This may not technically be a fix for the user issue but it does
demonstrate an improvement to Guild based on the issue.

`train-2` omits the otherwise required dependency config
`target-path`.

    $ guild run train-2 data=yyy -y
    Resolving config:embeddings_and_difficulty/configs_hydra/config.yaml
    data: test
