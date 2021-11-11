---
doctest-type: bash
---

# Flag not recognized: No module named --batch_size

https://github.com/guildai/guildai/issues/310

## Problem

Not clear but we'd like to more seamlessly support Pytorch
Lightning. User struggled with config to support a Lightning example.

## Recreating

Requirements:

- guild<=0.7.4
- See [requirements.txt](requirements.txt)

Steps to setup env (`-f` not supported in requirements.txt):

```
$ pip install torch==1.9.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html
$ pip install pytorch-lightning lightning-bolts guildai
```

## Workarounds

TDB

## Fix

TDB
