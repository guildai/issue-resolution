# guild tensorboard with true/false flags

https://github.com/guildai/guildai/issues/99

## Problem

It looks like Guild boolean values are presented to TB as "False" and
"True" literal strings.

## Recreating

Cannot recreate this issue with the steps below.

Requirements:

- guild==0.7.0.rc3
- tensorboard==1.14.0

Generate a run:

```
$ guild run test.py -y
```

View in TensorBoard:

```
$ guild tensorboard
```

Not seeing any errors in the console and the HParams plugin/tab is
correct.

## Workarounds

Use integer values `1` and `0` for `True` and `False` respectively.

## Fix

Not sure at this point - unable to recreate.

## Related Issues

- https://github.com/guildai/guildai/issues/163
