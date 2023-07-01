[Published runs](../README.md)

# mwe

| ID                   | Operation           | Started                  | Time                | Status           | Label                |
| --                   | ---------           | ---------                | ----                | ------           | -----                |
| eb1d9177 | mwe | 2023&#8209;07&#8209;01 12:31:49 UTC | 0:03:27 | completed | baseline (too high resources) |

[run.yml](run.yml)

## Contents

- [Flags](#flags)
- [Scalars](#scalars)
- [Run Files](#run-files)
- [Source Code](#source-code)
- [Output](#output)

## Flags

| Name | Value |
| ---- | ----- |
| NUM_DATALOADER_WORKERS | 7 |
| NUM_IN_FEATURES | 10 |
| NUM_TRAIN_SAMPLES | 80 |
| NUM_TRAINER_CPUS | 7 |
| NUM_TRAINER_GPUS | 1 |
| NUM_TRAINER_WORKERS | 4 |
| NUM_VAL_SAMPLES | 20 |
| SEED | 239 |

[flags.yml](flags.yml)
## Scalars

There are no scalars for this run.
## Run Files

| Path | Type | Size | Modified | MD5 |
| ---- | ---- | ---- | -------- | --- |
| ray_results/mwe/basic-variant-state-2023-07-01_07-30-08.json | file | 6.6K | 2023-07-01 07:30:23 UTC | 66f2e24a66b6c7789d2bd50826253702 |
| ray_results/mwe/basic-variant-state-2023-07-01_07-31-53.json | file | 6.6K | 2023-07-01 07:35:13 UTC | 1b8dd32a1109f569aeeded3d24cff08e |
| ray_results/mwe/experiment_state-2023-07-01_07-30-08.json | file | 12.2K | 2023-07-01 07:30:23 UTC | 7d1227b5bc6b3d7085a3a29d3550932e |
| ray_results/mwe/experiment_state-2023-07-01_07-31-53.json | file | 12.2K | 2023-07-01 07:35:13 UTC | ae76fe14f72e0df4a50a35d15b69bd2b |
| ray_results/mwe/trainable.pkl | file | 7.9K | 2023-07-01 07:31:51 UTC | 90ae7045e73a30c3096901f0fd98924b |
| ray_results/mwe/tuner.pkl | file | 1.4K | 2023-07-01 07:31:51 UTC | bede61a633c30e6d72a5be20def90338 |

[runfiles.csv](runfiles.csv)
## Source Code

| Path | Size | Modified | MD5 |
| ---- | ---- | -------- | --- |
| [FIX.md](sourcecode/FIX.md) | 182 | 2023-07-01 07:30:04 UTC | f651494c34eceb07582b05812276a57c |
| [README.md](sourcecode/README.md) | 1.4K | 2023-07-01 07:30:04 UTC | 93cff220c682543cd75dcacb2b6b925d |
| [guild.yml](sourcecode/guild.yml) | 211 | 2023-07-01 07:30:04 UTC | 91c04e6e0e225b3fba5223af9d17e737 |
| [mwe.py](sourcecode/mwe.py) | 5.6K | 2023-07-01 07:30:04 UTC | 16bdb36b80e2f765afdbde12b75b3e60 |
| [requirements.txt](sourcecode/requirements.txt) | 71 | 2023-07-01 07:30:04 UTC | f0bd64d1b02c027d4968fedb904967d2 |

[sourcecode.csv](sourcecode.csv)
## Output

```
2023-07-01 07:31:50.393639: I tensorflow/core/util/port.cc:110] oneDNN custom operations are on. You may see slightly different numerical results due to floating-point round-off errors from different computation orders. To turn them off, set the environment variable `TF_ENABLE_ONEDNN_OPTS=0`.
2023-07-01 07:31:50.418679: I tensorflow/core/platform/cpu_feature_guard.cc:182] This TensorFlow binary is optimized to use available CPU instructions in performance-critical operations.
To enable the following instructions: AVX2 AVX_VNNI FMA, in other operations, rebuild TensorFlow with the appropriate compiler flags.
2023-07-01 07:31:50.784138: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
INFO: [torch.distributed.nn.jit.instantiator] Created a temporary directory at /tmp/tmp9xduudlk
INFO: [torch.distributed.nn.jit.instantiator] Writing /tmp/tmp9xduudlk/_remote_module_non_scriptable.py
INFO: [ray.tune.impl.tuner_internal] A `RunConfig` was passed to both the `Tuner` and the `LightningTrainer`. The run config passed to the `Tuner` is the one that will be used.
2023-07-01 07:31:53,050	INFO worker.py:1625 -- Started a local Ray instance.
2023-07-01 07:31:53,607	INFO tune.py:218 -- Initializing Ray automatically. For cluster usage or custom Ray initialization, call `ray.init(...)` before `Tuner(...)`.
== Status ==
Current time: 2023-07-01 07:31:58 (running for 00:00:05.02)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:32:03 (running for 00:00:10.02)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:32:08 (running for 00:00:15.03)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:32:13 (running for 00:00:20.04)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:32:18 (running for 00:00:25.05)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:32:23 (running for 00:00:30.05)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:32:28 (running for 00:00:35.06)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:32:33 (running for 00:00:40.06)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:32:38 (running for 00:00:45.07)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:32:43 (running for 00:00:50.08)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:32:48 (running for 00:00:55.08)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:32:53 (running for 00:01:00.09)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:32:58 (running for 00:01:05.09)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


2023-07-01 07:33:03,712	WARNING insufficient_resources_manager.py:128 -- Ignore this message if the cluster is autoscaling. You asked for 29.0 cpu and 4.0 gpu per trial, but the cluster only has 20.0 cpu and 1.0 gpu. Stop the tuning job and adjust the resources requested per trial (possibly via `resources_per_trial` or via `num_workers` for rllib) and/or add more resources to your Ray runtime.
== Status ==
Current time: 2023-07-01 07:33:03 (running for 00:01:10.10)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:33:08 (running for 00:01:15.11)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:33:13 (running for 00:01:20.11)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:33:18 (running for 00:01:25.12)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:33:23 (running for 00:01:30.12)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:33:28 (running for 00:01:35.13)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:33:33 (running for 00:01:40.13)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:33:38 (running for 00:01:45.14)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:33:43 (running for 00:01:50.14)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:33:48 (running for 00:01:55.15)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:33:53 (running for 00:02:00.15)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:33:58 (running for 00:02:05.16)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


2023-07-01 07:34:03,776	WARNING insufficient_resources_manager.py:128 -- Ignore this message if the cluster is autoscaling. You asked for 29.0 cpu and 4.0 gpu per trial, but the cluster only has 20.0 cpu and 1.0 gpu. Stop the tuning job and adjust the resources requested per trial (possibly via `resources_per_trial` or via `num_workers` for rllib) and/or add more resources to your Ray runtime.
== Status ==
Current time: 2023-07-01 07:34:03 (running for 00:02:10.16)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:34:08 (running for 00:02:15.17)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:34:13 (running for 00:02:20.17)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:34:18 (running for 00:02:25.18)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:34:23 (running for 00:02:30.19)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:34:28 (running for 00:02:35.19)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:34:33 (running for 00:02:40.20)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:34:38 (running for 00:02:45.20)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:34:43 (running for 00:02:50.21)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:34:48 (running for 00:02:55.21)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:34:53 (running for 00:03:00.22)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:34:58 (running for 00:03:05.22)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


2023-07-01 07:35:03,841	WARNING insufficient_resources_manager.py:128 -- Ignore this message if the cluster is autoscaling. You asked for 29.0 cpu and 4.0 gpu per trial, but the cluster only has 20.0 cpu and 1.0 gpu. Stop the tuning job and adjust the resources requested per trial (possibly via `resources_per_trial` or via `num_workers` for rllib) and/or add more resources to your Ray runtime.
== Status ==
Current time: 2023-07-01 07:35:03 (running for 00:03:10.23)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:35:08 (running for 00:03:15.23)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


2023-07-01 07:35:10,851	WARNING tune.py:184 -- Stop signal received (e.g. via SIGINT/Ctrl+C), ending Ray Tune run. This will try to checkpoint the experiment state one last time. Press CTRL+C (or send SIGINT/SIGKILL/SIGTERM) to skip. 
== Status ==
Current time: 2023-07-01 07:35:13 (running for 00:03:20.24)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


== Status ==
Current time: 2023-07-01 07:35:13 (running for 00:03:20.24)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe
Number of trials: 2/2 (2 PENDING)
+------------------------------+----------+-------+------------------------+
| Trial name                   | status   | loc   |   lightning_config/_mo |
|                              |          |       |    dule_init_config/lr |
|------------------------------+----------+-------+------------------------|
| LightningTrainer_42993_00000 | PENDING  |       |             0.0011888  |
| LightningTrainer_42993_00001 | PENDING  |       |             0.00765266 |
+------------------------------+----------+-------+------------------------+


2023-07-01 07:35:13,860	ERROR tune.py:941 -- Trials did not complete: [LightningTrainer_42993_00000, LightningTrainer_42993_00001]
2023-07-01 07:35:13,860	INFO tune.py:945 -- Total run time: 200.25 seconds (200.24 seconds for the tuning loop).
2023-07-01 07:35:13,860	WARNING tune.py:954 -- Experiment has been interrupted, but the most recent state was saved.
Continue running this experiment with: Tuner.restore(path="/home/garrett/.guild/runs/eb1d91774b7e4ffa998306eb483e028a/ray_results/mwe", trainable=...)
```

[output.txt](output.txt)

