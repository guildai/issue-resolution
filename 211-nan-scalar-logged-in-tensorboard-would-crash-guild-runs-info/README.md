# NaN scalar logged in tensorboard would crash guild runs info

https://github.com/guildai/guildai/issues/211

## Problem

Guild is not handling None values logged in scalars when showing
scalar values in `guild runs info`.

## Recreating

Requirements:

- guild==0.7.0
- See [requirements.txt](requirements.txt)

```
guild init -y
guild run test.py -y
guild runs info
```

## Workarounds

Not sure. Avoiding NaN and Inf as scalars but that's not reasonable.

## Fix

Pending
