# Tensorboard TypeError when using flag with null and numbers

https://github.com/guildai/guildai/issues/163

## Problem

Guild automatically generates hparam data, which includes flag
values. The TensorBoard hparam plugin requires (assumes?) that the
type for flag name is the same for all runs. When a flag value types
differ, Guild is crashing because it doesn't handle the underlying
hparam plugin issue.

The underlying constraint that's being violated is
`tensorboard.plugins.hparams.summary_v2.Discrete`. Guild happily
passes a list of values of potentially different types to this
constructor, which generates the underlying error.

## Recreating

Requirements:

- guild<=0.7.0.rc9

To reproduct, run:

    $ guild run test.py x=[1,null]

Then run:

    $ guild tensorboard

You get traceback:

```
...
  File "~/guild/guild/tensorboard.py", line 188, in _refresh_run
    _refresh_tfevent_links(run, run_logdir, state)
  File "~/guild/guild/tensorboard.py", line 199, in _refresh_tfevent_links
    _init_tfevent_link(tfevent_path, link, run, state)
  File "~/guild/guild/tensorboard.py", line 213, in _init_tfevent_link
    _init_hparam_session(run, link_dir, state)
  File "~/guild/guild/tensorboard.py", line 221, in _init_hparam_session
    _add_hparam_experiment(state.hparam_experiment, writer)
  File "~/guild/guild/tensorboard.py", line 231, in _add_hparam_experiment
    writer.add_hparam_experiment(hparams, metrics)
  File "~/guild/guild/summary.py", line 126, in add_hparam_experiment
    self._add_summary(_HParamExperiment(hparams, metrics))
  File "~/guild/guild/summary.py", line 187, in _HParamExperiment
    hparams=[_HParam(key, vals) for key, vals in hparams.items()],
  File "~/guild/guild/summary.py", line 187, in <listcomp>
    hparams=[_HParam(key, vals) for key, vals in hparams.items()],
  File "~/guild/guild/summary.py", line 201, in _HParam
    return hp.HParam(name, hp.Discrete(legal_vals))
  File "~/guild-issues/163-tensorboard-typeerror-when-using-flag-with-null-and-numbers/venv/lib/python3.6/site-packages/tensorboard/plugins/hparams/summary_v2.py", line 513, in __init__
    % (value, self._dtype.__name__)
TypeError: dtype mismatch: not isinstance(5, str)
```

Note that this fails when different types are used. A combination of
similar types (e.g. `[null,null]`, `[1,2]`, etc.) does not fail.

## Workarounds

None. Upgrade to 0.7.0.rc10 to resolve the issue.

## Fix

This is fixed in 0.7.0.rc10.

When you view runs with different flag value types using `guild
tensorboard`, the values appear in the HPARAM tab but cannot be
filtered in the left pane.

## Related Issues

- https://github.com/guildai/guildai/issues/99
