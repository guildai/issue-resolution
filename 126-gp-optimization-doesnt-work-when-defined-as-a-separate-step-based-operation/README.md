# GP optimization doesn't work when defined as a separate step-based operation

https://github.com/guildai/guildai/issues/126

This issue is fixed in 0.7.0.rc10.

## Problem

Guild does not see previous trials when an optimization run is started
as a step.

## Recreating

Requirements:

- guild>=0.7.0.rc4,<=0.7.0.rc9

Change to this directory and run:

    $ guild run tune -y

Every trial looks like this:

```
INFO: [guild] Random start for optimization (missing previous trials)
INFO: [guild] Running trial ...: test_model:evaluate (x=...)
loss: ...
```

## Workarounds

Upgrade to 0.7.0.r10 to resolve this.
