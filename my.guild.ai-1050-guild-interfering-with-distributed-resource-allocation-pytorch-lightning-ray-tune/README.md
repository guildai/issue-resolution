---
doctest-type: bash
---

# Guild interfering with distributed resource allocation (pytorch-lightning/ray-tune

https://my.guild.ai/t/guild-interfering-with-distributed-resource-allocation-pytorch-lightning-ray-tune/1050

## Problem

Guild appears to be impacting the system view when running a Ray tune
operation.

## Recreating

Cannot recreate this so far.

The sample operation `mwe` is defined in [`guild.yml`](guild.yml). It
runs the script [`mwe.py`](mwe.py).

`mwe.py` is a modified version of the sample script provided in the
original issue. It's been modified to expose worked counts and CPU/GPU
counts.

There are two scenarios we've seen. Each scenario is captured by a
[published run](published-runs).

1. Run with worker count and CPU/GPU resources that we know aren't
   available on the system - see run
   [`eb1d9177`](published-runs/eb1d91774b7e4ffa998306eb483e028a)

2. Run with worker count and CPU/GPU resources that are available -
   see run
   [`aca3d652`](published-runs/aca3d6526c03439d8503f4d418d8b9c0/README.md)

Case #1 failed to proceed due a lack of available resources. The run
had to be manually terminated. Refer to the run
[output](published-runs/eb1d91774b7e4ffa998306eb483e028a/README.md#output)
for details.

Case #2 shows the expected resource count in the run
[output](published-runs/aca3d6526c03439d8503f4d418d8b9c0/README.md#output)
when run under Guild, at least on that particular system.

```
2023-07-01 07:36:36.866442: I tensorflow/core/util/port.cc:110] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2023-07-01 07:36:36.890998: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 AVX_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-07-01 07:36:37.246751: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
INFO: [torch.distributed.nn.jit.instantiator] Created a temporary directory at /tmp/tmpigdbr98n
INFO: [torch.distributed.nn.jit.instantiator] Writing /tmp/tmpigdbr98n/_remote_module_non_scriptable.py
INFO: [ray.tune.impl.tuner_internal] A `RunConfig` was passed to both the `Tuner` and the `LightningTrainer`. The run config passed to the `Tuner` is the one that will be used.
2023-07-01 07:36:39,491	INFO worker.py:1625 -- Started a local Ray instance.
2023-07-01 07:36:40,087	INFO tune.py:218 -- Initializing Ray automatically. For cluster usage or custom Ray initialization, call `ray.init(...)` before `Tuner(...)`.
== Status ==
Current time: 2023-07-01 07:36:41 (running for 00:00:01.44)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 8.0/20 CPUs, 1.0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/aca3d6526c03439d8503f4d418d8b9c0/ray_results/mwe
Number of trials: 2/2 (1 PENDING, 1 RUNNING)
+------------------------------+----------+----------------------+------------------------+
| Trial name                   | status   | loc                  |   lightning_config/_mo |
|                              |          |                      |    dule_init_config/lr |
|------------------------------+----------+----------------------+------------------------|
| LightningTrainer_ed5a9_00000 | RUNNING  | 192.168.1.206:799019 |             0.00279928 |
| LightningTrainer_ed5a9_00001 | PENDING  |                      |             0.00513599 |
+------------------------------+----------+----------------------+------------------------+
```

Note *Logical resource usage: 8.0/20 CPUs* in the output above. This
shows the correct CPU (core) count for the applicable system. There is
no apparent resource limitation when run with Guild in this case.

To further dianose this issue, run `mwe` from the OP environment.

    $ guild run mwe -y

## Workarounds

Not sure

## Fix

Not sure

## Related Issues

None
