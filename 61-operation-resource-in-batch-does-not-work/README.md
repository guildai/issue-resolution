# Specifying operation resource in batch run does not work

https://github.com/guildai/guildai/issues/61

## Problem

Batch runs aren't passing resource config along to their trials.

## Recreating

Requirements:

- guild<=0.6.7.dev3

Run:

    ./recreate

Note that the batch run uses the latest model even though an earlier
model is explicitly set in the batch command.

## Workarounds

As a workaround, Guild will use the latest marked run to satisfy an
operation requirement. This does work for batch trials.

## Fix

A fix for this issue is available in 0.6.7.dev4 and later.

## Other Notes

### Unclear or unsupported default names for resources

A requirement like this:

``` yaml
retrain:
  requires:
    - operation: train
```

should use `train` as the resource name.

That would let a user run:

    $ guild run retrain train=abcdef

As it is, the user needs to define `name` explicitly. This isn't
aweful - and it encourages better naming (e.g. `model`) but it's
non-obvious and frustrating if you miss that.

UPDATE: This is *not* included in the fix available in 0.6.7.dev4.

### Default labels missing resource args

Guild should include the resource value in its default label. E.g.

    $ guild run retrain x=1 model=abcdef

should generate a run with the label `x=1 model=abcdef`.

In fact, one could argue that this tag should be applied in all cases!
It's completely non-obvious what run is being resolved and you need to
use `runs info` to devine that. That's the purpose of default labels!

Note that Guild already has this info handy - as the `label` config in
`guild.yml` lets the user define this explicitly:

```
retrain:
  label: x=${x} model=${model}
```

^ works!

UPDATE: This is fixed in 0.6.7.dev4. Default labels now include
resource references.
