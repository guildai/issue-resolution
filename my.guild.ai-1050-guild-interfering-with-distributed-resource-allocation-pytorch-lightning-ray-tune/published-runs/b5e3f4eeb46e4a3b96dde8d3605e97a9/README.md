[Published runs](../README.md)

# mwe

| ID                   | Operation           | Started                  | Time                | Status           | Label                |
| --                   | ---------           | ---------                | ----                | ------           | -----                |
| b5e3f4ee | mwe | 2023&#8209;07&#8209;03 08:08:19 UTC | 0:01:23 | completed | NUM_DATALOADER_WORKERS=7 NUM_IN_FEATURES=10 NUM_TRAINER_CPUS=7 NUM_TRAINER_GPUS=1 NUM_TRAINER_WORKERS=1 NUM_TRAIN_SAMPLES=8000 NUM_VAL_SAMPLES=20 SEED=239 |

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
| NUM_TRAIN_SAMPLES | 8000 |
| NUM_TRAINER_CPUS | 7 |
| NUM_TRAINER_GPUS | 1 |
| NUM_TRAINER_WORKERS | 1 |
| NUM_VAL_SAMPLES | 20 |
| SEED | 239 |

[flags.yml](flags.yml)
## Scalars

| Key | Step | Value |
| --- | ---- | ----- |
| mwe/version_0#epoch | 3999 | 4.0 |
| mwe/version_0#hp_metric | 0 | -1.0 |
| mwe/version_0#train/loss | 3999 | 0.09560998529195786 |
| mwe/version_0#val/loss | 3999 | 0.09679657220840454 |
| mwe/version_1#epoch | 3999 | 4.0 |
| mwe/version_1#hp_metric | 0 | -1.0 |
| mwe/version_1#train/loss | 3999 | 0.09152068942785263 |
| mwe/version_1#val/loss | 3999 | 0.09357253462076187 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#ray/tune/done | 5 | 1.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#ray/tune/epoch | 5 | 4.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#ray/tune/iterations_since_restore | 5 | 5.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#ray/tune/should_checkpoint | 5 | 1.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#ray/tune/step | 5 | 4000.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#ray/tune/time_since_restore | 5 | 61.42856216430664 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#ray/tune/time_this_iter_s | 5 | 9.677968978881836 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#ray/tune/train/loss | 5 | 0.09560998529195786 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#ray/tune/val/loss | 5 | 0.09679657220840454 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu0/fanspeed | 1 | 0.3100000023841858 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu0/mem_free | 1 | 10622074880.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu0/mem_total | 1 | 11554258944.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu0/mem_used | 1 | 932184064.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu0/mem_util | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu0/powerdraw | 1 | 75.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu0/pstate | 1 | 2.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu0/temp | 1 | 33.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu0/util | 1 | 0.009999999776482582 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu1/fanspeed | 1 | 0.3199999928474426 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu1/mem_free | 1 | 10622074880.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu1/mem_total | 1 | 11554258944.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu1/mem_used | 1 | 932184064.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu1/mem_util | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu1/powerdraw | 1 | 63.400001525878906 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu1/pstate | 1 | 2.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu1/temp | 1 | 35.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu1/util | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu2/fanspeed | 1 | 0.3100000023841858 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu2/mem_free | 1 | 11553210368.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu2/mem_total | 1 | 11554258944.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu2/mem_used | 1 | 1048576.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu2/mem_util | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu2/powerdraw | 1 | 21.969999313354492 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu2/pstate | 1 | 8.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu2/temp | 1 | 33.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu2/util | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu3/fanspeed | 1 | 0.30000001192092896 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu3/mem_free | 1 | 11465129984.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu3/mem_total | 1 | 11551113216.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu3/mem_used | 1 | 85983232.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu3/mem_util | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu3/powerdraw | 1 | 16.209999084472656 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu3/pstate | 1 | 8.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu3/temp | 1 | 35.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/gpu3/util | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/mem_free | 1 | 88915083264.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/mem_total | 1 | 134842548224.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/mem_used | 1 | 19279380480.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/mem_util | 1 | 0.15299999713897705 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/swap_free | 1 | 1920937984.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/swap_total | 1 | 2147479552.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/swap_used | 1 | 226541568.0 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32#sys/swap_util | 1 | 0.10499999672174454 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#performance/sec_per_step | 5 | 7.946107864379883 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#performance/step_per_sec | 5 | 0.12584777176380157 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#ray/tune/done | 5 | 1.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#ray/tune/epoch | 5 | 4.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#ray/tune/iterations_since_restore | 5 | 5.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#ray/tune/should_checkpoint | 5 | 1.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#ray/tune/step | 5 | 4000.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#ray/tune/time_since_restore | 5 | 61.151920318603516 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#ray/tune/time_this_iter_s | 5 | 7.943993091583252 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#ray/tune/train/loss | 5 | 0.09152068942785263 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#ray/tune/val/loss | 5 | 0.09357253462076187 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu/util | 5 | 0.09193749725818634 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu0/util | 5 | 0.9580000042915344 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu1/util | 5 | 0.06300000101327896 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu10/util | 5 | 0.006000000052154064 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu11/util | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu12/util | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu13/util | 5 | 0.12700000405311584 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu14/util | 5 | 0.006000000052154064 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu15/util | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu16/util | 5 | 0.9259999990463257 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu17/util | 5 | 0.003000000026077032 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu18/util | 5 | 0.006000000052154064 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu19/util | 5 | 0.0010000000474974513 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu2/util | 5 | 0.49799999594688416 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu20/util | 5 | 0.003000000026077032 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu21/util | 5 | 0.003000000026077032 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu22/util | 5 | 0.003000000026077032 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu23/util | 5 | 0.008999999612569809 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu24/util | 5 | 0.003000000026077032 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu25/util | 5 | 0.004000000189989805 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu26/util | 5 | 0.0010000000474974513 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu27/util | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu28/util | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu29/util | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu3/util | 5 | 0.05999999865889549 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu30/util | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu31/util | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu4/util | 5 | 0.10700000077486038 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu5/util | 5 | 0.11299999803304672 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu6/util | 5 | 0.01899999938905239 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu7/util | 5 | 0.009999999776482582 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu8/util | 5 | 0.008999999612569809 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/cpu9/util | 5 | 0.004000000189989805 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/devnvme0n1p1/rkbps | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/devnvme0n1p1/rps | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/devnvme0n1p1/util | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/devnvme0n1p1/wkbps | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/devnvme0n1p1/wps | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/devnvme0n1p2/rkbps | 5 | 5.538986682891846 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/devnvme0n1p2/rps | 5 | 0.503544270992279 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/devnvme0n1p2/util | 5 | 0.010070884600281715 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/devnvme0n1p2/wkbps | 5 | 166.6731414794922 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/devnvme0n1p2/wps | 5 | 21.274744033813477 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu0/fanspeed | 5 | 0.3100000023841858 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu0/mem_free | 5 | 10622074880.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu0/mem_total | 5 | 11554258944.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu0/mem_used | 5 | 932184064.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu0/mem_util | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu0/powerdraw | 5 | 74.83000183105469 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu0/pstate | 5 | 2.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu0/temp | 5 | 36.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu0/util | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu1/fanspeed | 5 | 0.3100000023841858 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu1/mem_free | 5 | 11553210368.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu1/mem_total | 5 | 11554258944.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu1/mem_used | 5 | 1048576.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu1/mem_util | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu1/powerdraw | 5 | 18.440000534057617 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu1/pstate | 5 | 8.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu1/temp | 5 | 37.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu1/util | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu2/fanspeed | 5 | 0.3100000023841858 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu2/mem_free | 5 | 11553210368.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu2/mem_total | 5 | 11554258944.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu2/mem_used | 5 | 1048576.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu2/mem_util | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu2/powerdraw | 5 | 20.940000534057617 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu2/pstate | 5 | 8.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu2/temp | 5 | 33.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu2/util | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu3/fanspeed | 5 | 0.30000001192092896 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu3/mem_free | 5 | 11465129984.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu3/mem_total | 5 | 11551113216.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu3/mem_used | 5 | 85983232.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu3/mem_util | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu3/powerdraw | 5 | 15.449999809265137 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu3/pstate | 5 | 8.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu3/temp | 5 | 36.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/gpu3/util | 5 | 0.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/mem_free | 5 | 91572027392.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/mem_total | 5 | 134842548224.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/mem_used | 5 | 16669356032.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/mem_util | 5 | 0.1340000033378601 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/swap_free | 5 | 1920937984.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/swap_total | 5 | 2147479552.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/swap_used | 5 | 226541568.0 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34#sys/swap_util | 5 | 0.10499999672174454 |

[scalars.csv](scalars.csv)
## Run Files

| Path | Type | Size | Modified | MD5 |
| ---- | ---- | ---- | -------- | --- |
| mwe/version_0/checkpoints/epoch=2-step=2400.ckpt | file | 10.5K | 2023-07-03 01:09:16 UTC | 2d2b187e75e5a696f5aea4edfa54308e |
| mwe/version_0/checkpoints/last.ckpt | file | 10.5K | 2023-07-03 01:09:35 UTC | c30ec98ce5f6791555f72c3e120076e1 |
| mwe/version_0/events.out.tfevents.1688371722.lambda2.8640.0 | file | 8.4K | 2023-07-03 01:09:35 UTC | 02e47097a09f55db34a7d9c60261eacd |
| mwe/version_0/hparams.yaml | file | 4.9K | 2023-07-03 01:08:42 UTC | d6eb00f24d25bcdf3a282e74397086a9 |
| mwe/version_1/checkpoints/epoch=3-step=3200.ckpt | file | 10.5K | 2023-07-03 01:09:31 UTC | 30a13621ab20a637e62e6c3ae7f18e68 |
| mwe/version_1/checkpoints/last.ckpt | file | 10.5K | 2023-07-03 01:09:39 UTC | 7e9cbee66589f75d362ca3f554b21146 |
| mwe/version_1/events.out.tfevents.1688371729.lambda2.8942.0 | file | 8.4K | 2023-07-03 01:09:39 UTC | aae3babe5153df7b79f4a2d250f9ed57 |
| mwe/version_1/hparams.yaml | file | 4.9K | 2023-07-03 01:08:49 UTC | 668a8ef9e0f8b6297999fa9b3a52b392 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000000/.is_checkpoint | file | 0 | 2023-07-03 01:08:58 UTC | d41d8cd98f00b204e9800998ecf8427e |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000000/.metadata.pkl | file | 199 | 2023-07-03 01:08:58 UTC | 682f2a86c16bd4e757a0e38d2b61ef1b |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000000/.tune_metadata | file | 738 | 2023-07-03 01:08:58 UTC | 22b09d5bd0883bf5df355bac26e7785e |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000000/_preprocessor | file | 4 | 2023-07-03 01:08:58 UTC | 8a76b3f1259a772a2ee2738c8264cf1f |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000000/model | file | 10.5K | 2023-07-03 01:08:58 UTC | d00b47856276503653d08971dc2f9e9c |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000001/.is_checkpoint | file | 0 | 2023-07-03 01:09:07 UTC | d41d8cd98f00b204e9800998ecf8427e |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000001/.metadata.pkl | file | 199 | 2023-07-03 01:09:07 UTC | 8d026a9479386d8dd50201927c9d7719 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000001/.tune_metadata | file | 738 | 2023-07-03 01:09:07 UTC | ad02dc4bc9e6c1ca274de2742e748459 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000001/_preprocessor | file | 4 | 2023-07-03 01:09:07 UTC | 8a76b3f1259a772a2ee2738c8264cf1f |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000001/model | file | 10.5K | 2023-07-03 01:09:07 UTC | 58cb37b844d088da2801c07737f23f68 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000002/.is_checkpoint | file | 0 | 2023-07-03 01:09:16 UTC | d41d8cd98f00b204e9800998ecf8427e |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000002/.metadata.pkl | file | 199 | 2023-07-03 01:09:16 UTC | b89631a14e10e4124b99938fc2bb85de |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000002/.tune_metadata | file | 738 | 2023-07-03 01:09:16 UTC | a9d05cf6ea81514a3f69033ad7871e5f |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000002/_preprocessor | file | 4 | 2023-07-03 01:09:16 UTC | 8a76b3f1259a772a2ee2738c8264cf1f |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000002/model | file | 10.5K | 2023-07-03 01:09:16 UTC | 2d2b187e75e5a696f5aea4edfa54308e |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000003/.is_checkpoint | file | 0 | 2023-07-03 01:09:26 UTC | d41d8cd98f00b204e9800998ecf8427e |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000003/.metadata.pkl | file | 199 | 2023-07-03 01:09:26 UTC | 9da9ec36bf3229ed0758f3319b643017 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000003/.tune_metadata | file | 738 | 2023-07-03 01:09:26 UTC | aa0aeefe745abdf492a1ba29bdeee0b3 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000003/_preprocessor | file | 4 | 2023-07-03 01:09:26 UTC | 8a76b3f1259a772a2ee2738c8264cf1f |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000003/model | file | 10.5K | 2023-07-03 01:09:26 UTC | 3f631c7994975dadd1d949ff1f29f1dc |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000004/.is_checkpoint | file | 0 | 2023-07-03 01:09:35 UTC | d41d8cd98f00b204e9800998ecf8427e |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000004/.metadata.pkl | file | 199 | 2023-07-03 01:09:35 UTC | 1b76a8632eba4744e5fc29ff00706f98 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000004/.tune_metadata | file | 738 | 2023-07-03 01:09:35 UTC | a645db717b96817cfc5a9e6426548f70 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000004/_preprocessor | file | 4 | 2023-07-03 01:09:35 UTC | 8a76b3f1259a772a2ee2738c8264cf1f |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/checkpoint_000004/model | file | 10.5K | 2023-07-03 01:09:35 UTC | c30ec98ce5f6791555f72c3e120076e1 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/events.out.tfevents.1688371712.lambda2 | file | 23.9K | 2023-07-03 01:09:35 UTC | fc1b5caab4f6790d0ae9090f1fa792c1 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/params.json | file | 230 | 2023-07-03 01:08:32 UTC | 85733acb2d45845106e8e44cbf0efde2 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/params.pkl | file | 180 | 2023-07-03 01:08:32 UTC | bdcfafdab4e9fe67b26dd8cd0126010b |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/progress.csv | file | 1.2K | 2023-07-03 01:09:35 UTC | b0559d33153f57684b4a1f73d02beaa5 |
| ray_results/mwe/LightningTrainer_cce97_00000_0_lr=0.0611_2023-07-03_01-08-32/result.json | file | 3.4K | 2023-07-03 01:09:35 UTC | acfd52ba134865e2b201b97ab27d9cec |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000000/.is_checkpoint | file | 0 | 2023-07-03 01:09:03 UTC | d41d8cd98f00b204e9800998ecf8427e |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000000/.metadata.pkl | file | 199 | 2023-07-03 01:09:03 UTC | 682f2a86c16bd4e757a0e38d2b61ef1b |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000000/.tune_metadata | file | 738 | 2023-07-03 01:09:04 UTC | 4a60ca63038783d4b5e851ae609001ea |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000000/_preprocessor | file | 4 | 2023-07-03 01:09:03 UTC | 8a76b3f1259a772a2ee2738c8264cf1f |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000000/model | file | 10.5K | 2023-07-03 01:09:03 UTC | a43e5da6b443c086c9f31e68baae7842 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000001/.is_checkpoint | file | 0 | 2023-07-03 01:09:13 UTC | d41d8cd98f00b204e9800998ecf8427e |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000001/.metadata.pkl | file | 199 | 2023-07-03 01:09:13 UTC | 8d026a9479386d8dd50201927c9d7719 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000001/.tune_metadata | file | 738 | 2023-07-03 01:09:13 UTC | 33877067903ed5895d9b56859ab59cbe |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000001/_preprocessor | file | 4 | 2023-07-03 01:09:13 UTC | 8a76b3f1259a772a2ee2738c8264cf1f |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000001/model | file | 10.5K | 2023-07-03 01:09:12 UTC | 9f8eba7a49a211d234e5a9dab93335d6 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000002/.is_checkpoint | file | 0 | 2023-07-03 01:09:22 UTC | d41d8cd98f00b204e9800998ecf8427e |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000002/.metadata.pkl | file | 199 | 2023-07-03 01:09:22 UTC | b89631a14e10e4124b99938fc2bb85de |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000002/.tune_metadata | file | 738 | 2023-07-03 01:09:22 UTC | 5ba6171a34e886ddc7939b4e759b28a3 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000002/_preprocessor | file | 4 | 2023-07-03 01:09:22 UTC | 8a76b3f1259a772a2ee2738c8264cf1f |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000002/model | file | 10.5K | 2023-07-03 01:09:22 UTC | c58c461e0f74b2d016a83443355f013a |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000003/.is_checkpoint | file | 0 | 2023-07-03 01:09:31 UTC | d41d8cd98f00b204e9800998ecf8427e |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000003/.metadata.pkl | file | 199 | 2023-07-03 01:09:31 UTC | 9da9ec36bf3229ed0758f3319b643017 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000003/.tune_metadata | file | 738 | 2023-07-03 01:09:31 UTC | ec989437703f7592bb97d819c22a0a80 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000003/_preprocessor | file | 4 | 2023-07-03 01:09:31 UTC | 8a76b3f1259a772a2ee2738c8264cf1f |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000003/model | file | 10.5K | 2023-07-03 01:09:31 UTC | 30a13621ab20a637e62e6c3ae7f18e68 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000004/.is_checkpoint | file | 0 | 2023-07-03 01:09:39 UTC | d41d8cd98f00b204e9800998ecf8427e |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000004/.metadata.pkl | file | 199 | 2023-07-03 01:09:39 UTC | 1b76a8632eba4744e5fc29ff00706f98 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000004/.tune_metadata | file | 738 | 2023-07-03 01:09:39 UTC | 11418fc182b7b6d42bbfde5f7247a853 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000004/_preprocessor | file | 4 | 2023-07-03 01:09:39 UTC | 8a76b3f1259a772a2ee2738c8264cf1f |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/checkpoint_000004/model | file | 10.5K | 2023-07-03 01:09:39 UTC | 7e9cbee66589f75d362ca3f554b21146 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/events.out.tfevents.1688371714.lambda2 | file | 211.8K | 2023-07-03 01:09:39 UTC | ee57538fa1544260ba833eb0abfd7512 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/params.json | file | 230 | 2023-07-03 01:08:34 UTC | 2b6a153bd06d9b5836d534123655b391 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/params.pkl | file | 180 | 2023-07-03 01:08:34 UTC | e41b0ee19e0081e853a402130f348a48 |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/progress.csv | file | 1.2K | 2023-07-03 01:09:39 UTC | 0e5f75d480ebe78ab41f09081aa411eb |
| ray_results/mwe/LightningTrainer_cce97_00001_1_lr=0.0065_2023-07-03_01-08-34/result.json | file | 3.4K | 2023-07-03 01:09:39 UTC | 12d6f7ad8cbb667912bcec66f44b68e5 |
| ray_results/mwe/basic-variant-state-2023-07-03_01-08-31.json | file | 6.6K | 2023-07-03 01:09:39 UTC | 5776201fb471aa11f442a8f7c2ddd191 |
| ray_results/mwe/experiment_state-2023-07-03_01-08-31.json | file | 39.4K | 2023-07-03 01:09:39 UTC | 3f311a017a00bde51c9baff1e2726639 |
| ray_results/mwe/trainable.pkl | file | 8.1K | 2023-07-03 01:08:21 UTC | 789ab2d629aa2d9df374f6ef50ff9b5b |
| ray_results/mwe/tuner.pkl | file | 1.4K | 2023-07-03 01:08:21 UTC | ed8b4a86927ab10bdf93ae58bda0f4ed |

[runfiles.csv](runfiles.csv)
## Source Code

| Path | Size | Modified | MD5 |
| ---- | ---- | -------- | --- |
| [FIX.md](sourcecode/FIX.md) | 182 | 2023-07-03 01:08:18 UTC | f651494c34eceb07582b05812276a57c |
| [README.md](sourcecode/README.md) | 5.4K | 2023-07-03 01:08:18 UTC | f6b98acd583d92b65439d50e9316e744 |
| [guild.yml](sourcecode/guild.yml) | 211 | 2023-07-03 01:08:18 UTC | 91c04e6e0e225b3fba5223af9d17e737 |
| [mwe.py](sourcecode/mwe.py) | 5.6K | 2023-07-03 01:08:18 UTC | 18e602051fb1a42198ed0ca9626554fe |
| [requirements.txt](sourcecode/requirements.txt) | 71 | 2023-07-03 01:08:18 UTC | f0bd64d1b02c027d4968fedb904967d2 |

[sourcecode.csv](sourcecode.csv)
## Output

```
INFO: [torch.distributed.nn.jit.instantiator] Created a temporary directory at /tmp/tmpdcve0m1g
INFO: [torch.distributed.nn.jit.instantiator] Writing /tmp/tmpdcve0m1g/_remote_module_non_scriptable.py
INFO: [ray.tune.impl.tuner_internal] A `RunConfig` was passed to both the `Tuner` and the `LightningTrainer`. The run config passed to the `Tuner` is the one that will be used.
2023-07-03 01:08:22,935	INFO worker.py:1616 -- Started a local Ray instance. View the dashboard at [1m[32m127.0.0.1:8265 [39m[22m
2023-07-03 01:08:31,960	INFO tune.py:218 -- Initializing Ray automatically. For cluster usage or custom Ray initialization, call `ray.init(...)` before `Tuner(...)`.
== Status ==
Current time: 2023-07-03 01:08:34 (running for 00:00:02.53)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 8.0/32 CPUs, 1.0/4 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/davina/.guild/runs/b5e3f4eeb46e4a3b96dde8d3605e97a9/ray_results/mwe
Number of trials: 2/2 (1 PENDING, 1 RUNNING)
+------------------------------+----------+---------------------+------------------------+
| Trial name                   | status   | loc                 |   lightning_config/_mo |
|                              |          |                     |    dule_init_config/lr |
|------------------------------+----------+---------------------+------------------------|
| LightningTrainer_cce97_00000 | RUNNING  | 131.179.80.122:8205 |             0.0611121  |
| LightningTrainer_cce97_00001 | PENDING  |                     |             0.00650997 |
+------------------------------+----------+---------------------+------------------------+


[2m[36m(RayTrainWorker pid=8640)[0m 2023-07-03 01:08:37,128	INFO config.py:86 -- Setting up process group for: env:// [rank=0, world_size=1]
[2m[36m(RayTrainWorker pid=8640)[0m GPU available: True (cuda), used: True
[2m[36m(RayTrainWorker pid=8640)[0m TPU available: False, using: 0 TPU cores
[2m[36m(RayTrainWorker pid=8640)[0m IPU available: False, using: 0 IPUs
[2m[36m(RayTrainWorker pid=8640)[0m HPU available: False, using: 0 HPUs
[2m[36m(RayTrainWorker pid=8640)[0m Missing logger folder: /home/davina/.guild/runs/b5e3f4eeb46e4a3b96dde8d3605e97a9/mwe
== Status ==
Current time: 2023-07-03 01:08:39 (running for 00:00:07.55)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 16.0/32 CPUs, 2.0/4 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/davina/.guild/runs/b5e3f4eeb46e4a3b96dde8d3605e97a9/ray_results/mwe
Number of trials: 2/2 (2 RUNNING)
+------------------------------+----------+---------------------+------------------------+
| Trial name                   | status   | loc                 |   lightning_config/_mo |
|                              |          |                     |    dule_init_config/lr |
|------------------------------+----------+---------------------+------------------------|
| LightningTrainer_cce97_00000 | RUNNING  | 131.179.80.122:8205 |             0.0611121  |
| LightningTrainer_cce97_00001 | RUNNING  | 131.179.80.122:8642 |             0.00650997 |
+------------------------------+----------+---------------------+------------------------+


[2m[36m(RayTrainWorker pid=8640)[0m LOCAL_RANK: 0 - CUDA_VISIBLE_DEVICES: [1]
[2m[36m(RayTrainWorker pid=8640)[0m 
[2m[36m(RayTrainWorker pid=8640)[0m   | Name | Type    | Params
[2m[36m(RayTrainWorker pid=8640)[0m ---------------------------------
[2m[36m(RayTrainWorker pid=8640)[0m 0 | loss | MSELoss | 0     
[2m[36m(RayTrainWorker pid=8640)[0m 1 | fc1  | Linear  | 55    
[2m[36m(RayTrainWorker pid=8640)[0m 2 | fc2  | Linear  | 60    
[2m[36m(RayTrainWorker pid=8640)[0m ---------------------------------
[2m[36m(RayTrainWorker pid=8640)[0m 115       Trainable params
[2m[36m(RayTrainWorker pid=8640)[0m 0         Non-trainable params
[2m[36m(RayTrainWorker pid=8640)[0m 115       Total params
[2m[36m(RayTrainWorker pid=8640)[0m 0.000     Total estimated model params size (MB)
[2m[36m(RayTrainWorker pid=8640)[0m /home/davina/mambaforge/envs/ap/lib/python3.9/site-packages/torch/utils/data/dataloader.py:563: UserWarning: This DataLoader will create 7 worker processes in total. Our suggested max number of worker in current system is 2, which is smaller than what this DataLoader is going to create. Please be aware that excessive worker creation might get DataLoader running slow or even freeze, lower the worker number to avoid potential slowness/freeze if necessary.
[2m[36m(RayTrainWorker pid=8640)[0m   warnings.warn(_create_warning_msg(
[2m[36m(RayTrainWorker pid=8942)[0m HPU available: False, using: 0 HPUs
[2m[36m(RayTrainWorker pid=8942)[0m HPU available: False, using: 0 HPUs
[2m[36m(RayTrainWorker pid=8942)[0m HPU available: False, using: 0 HPUs
[2m[36m(RayTrainWorker pid=8942)[0m HPU available: False, using: 0 HPUs
[2m[36m(RayTrainWorker pid=8942)[0m HPU available: False, using: 0 HPUs
== Status ==
Current time: 2023-07-03 01:08:44 (running for 00:00:12.56)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 16.0/32 CPUs, 2.0/4 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/davina/.guild/runs/b5e3f4eeb46e4a3b96dde8d3605e97a9/ray_results/mwe
Number of trials: 2/2 (2 RUNNING)
+------------------------------+----------+---------------------+------------------------+
| Trial name                   | status   | loc                 |   lightning_config/_mo |
|                              |          |                     |    dule_init_config/lr |
|------------------------------+----------+---------------------+------------------------|
| LightningTrainer_cce97_00000 | RUNNING  | 131.179.80.122:8205 |             0.0611121  |
| LightningTrainer_cce97_00001 | RUNNING  | 131.179.80.122:8642 |             0.00650997 |
+------------------------------+----------+---------------------+------------------------+


[2m[36m(RayTrainWorker pid=8640)[0m /home/davina/mambaforge/envs/ap/lib/python3.9/site-packages/pytorch_lightning/trainer/connectors/logger_connector/result.py:432: PossibleUserWarning: It is recommended to use `self.log('val/loss', ..., sync_dist=True)` when logging on epoch level in distributed setting to accumulate the metric across devices.
[2m[36m(RayTrainWorker pid=8640)[0m   warning_cache.warn(
== Status ==
Current time: 2023-07-03 01:08:49 (running for 00:00:17.56)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 16.0/32 CPUs, 2.0/4 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/davina/.guild/runs/b5e3f4eeb46e4a3b96dde8d3605e97a9/ray_results/mwe
Number of trials: 2/2 (2 RUNNING)
+------------------------------+----------+---------------------+------------------------+
| Trial name                   | status   | loc                 |   lightning_config/_mo |
|                              |          |                     |    dule_init_config/lr |
|------------------------------+----------+---------------------+------------------------|
| LightningTrainer_cce97_00000 | RUNNING  | 131.179.80.122:8205 |             0.0611121  |
| LightningTrainer_cce97_00001 | RUNNING  | 131.179.80.122:8642 |             0.00650997 |
+------------------------------+----------+---------------------+------------------------+


[2m[36m(RayTrainWorker pid=8942)[0m 0.000     Total estimated model params size (MB)
[2m[36m(RayTrainWorker pid=8942)[0m 0.000     Total estimated model params size (MB)
[2m[36m(RayTrainWorker pid=8942)[0m 0.000     Total estimated model params size (MB)
[2m[36m(RayTrainWorker pid=8942)[0m ---------------------------------[32m [repeated 2x across cluster] (Ray deduplicates logs by default. Set RAY_DEDUP_LOGS=0 to disable log deduplication, or see https://docs.ray.io/en/master/ray-observability/ray-logging.html#log-deduplication for more options.)[0m
[2m[36m(RayTrainWorker pid=8942)[0m 0.000     Total estimated model params size (MB)
[2m[36m(RayTrainWorker pid=8942)[0m 2 | fc2  | Linear  | 60    [32m [repeated 2x across cluster][0m
[2m[36m(RayTrainWorker pid=8942)[0m 0.000     Total estimated model params size (MB)
[2m[36m(RayTrainWorker pid=8942)[0m 0.000     Total estimated model params size (MB)
[2m[36m(RayTrainWorker pid=8942)[0m 0.000     Total estimated model params size (MB)
[2m[36m(RayTrainWorker pid=8942)[0m 0.000     Total estimated model params size (MB)
[2m[36m(RayTrainWorker pid=8942)[0m /home/davina/mambaforge/envs/ap/lib/python3.9/site-packages/torch/utils/data/dataloader.py:563: UserWarning: This DataLoader will create 7 worker processes in total. Our suggested max number of worker in current system is 2, which is smaller than what this DataLoader is going to create. Please be aware that excessive worker creation might get DataLoader running slow or even freeze, lower the worker number to avoid potential slowness/freeze if necessary.
[2m[36m(RayTrainWorker pid=8942)[0m   warnings.warn(_create_warning_msg(
[2m[36m(RayTrainWorker pid=8942)[0m   warning_cache.warn(
[2m[36m(RayTrainWorker pid=8942)[0m   warning_cache.warn(
== Status ==
Current time: 2023-07-03 01:08:54 (running for 00:00:22.57)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: None
Logical resource usage: 16.0/32 CPUs, 2.0/4 GPUs (0.0/1.0 accelerator_type:RTX)
Result logdir: /home/davina/.guild/runs/b5e3f4eeb46e4a3b96dde8d3605e97a9/ray_results/mwe
Number of trials: 2/2 (2 RUNNING)
+------------------------------+----------+---------------------+------------------------+
| Trial name                   | status   | loc                 |   lightning_config/_mo |
|                              |          |                     |    dule_init_config/lr |
|------------------------------+----------+---------------------+------------------------|
| LightningTrainer_cce97_00000 | RUNNING  | 131.179.80.122:8205 |             0.0611121  |
| LightningTrainer_cce97_00001 | RUNNING  | 131.179.80.122:8642 |             0.00650997 |
+------------------------------+----------+---------------------+------------------------+


Result for LightningTrainer_cce97_00000:
  _report_on: train_epoch_end
  date: 2023-07-03_01-08-58
  done: false
  epoch: 0
  hostname: lambda2
  iterations_since_restore: 1
  node_ip: 131.179.80.122
  pid: 8205
  should_checkpoint: true
  step: 800
  time_since_restore: 23.717363119125366
  time_this_iter_s: 23.717363119125366
  time_total_s: 23.717363119125366
  timestamp: 1688371738
  train/loss: 0.0913718193769455
  training_iteration: 1
  trial_id: cce97_00000
  val/loss: 0.09642121940851212
  
== Status ==
Current time: 2023-07-03 01:09:03 (running for 00:00:31.43)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: -0.09642121940851212
Logical resource usage: 16.0/32 CPUs, 2.0/4 GPUs (0.0/1.0 accelerator_type:RTX)
Current best trial: cce97_00000 with val/loss=0.09642121940851212 and parameters={'lightning_config': {'_module_init_config': {'lr': 0.061112067431094506}, '_trainer_init_config': {}, '_trainer_fit_params': {}, '_ddp_strategy_config': {}, '_model_checkpoint_config': {}}}
Result logdir: /home/davina/.guild/runs/b5e3f4eeb46e4a3b96dde8d3605e97a9/ray_results/mwe
Number of trials: 2/2 (2 RUNNING)
+------------------------------+----------+---------------------+------------------------+--------+------------------+--------------+------------+---------+
| Trial name                   | status   | loc                 |   lightning_config/_mo |   iter |   total time (s) |   train/loss |   val/loss |   epoch |
|                              |          |                     |    dule_init_config/lr |        |                  |              |            |         |
|------------------------------+----------+---------------------+------------------------+--------+------------------+--------------+------------+---------|
| LightningTrainer_cce97_00000 | RUNNING  | 131.179.80.122:8205 |             0.0611121  |      1 |          23.7174 |    0.0913718 |  0.0964212 |       0 |
| LightningTrainer_cce97_00001 | RUNNING  | 131.179.80.122:8642 |             0.00650997 |        |                  |              |            |         |
+------------------------------+----------+---------------------+------------------------+--------+------------------+--------------+------------+---------+


Result for LightningTrainer_cce97_00001:
  _report_on: train_epoch_end
  date: 2023-07-03_01-09-03
  done: false
  epoch: 0
  hostname: lambda2
  iterations_since_restore: 1
  node_ip: 131.179.80.122
  pid: 8642
  should_checkpoint: true
  step: 800
  time_since_restore: 25.60190773010254
  time_this_iter_s: 25.60190773010254
  time_total_s: 25.60190773010254
  timestamp: 1688371743
  train/loss: 0.0973598062992096
  training_iteration: 1
  trial_id: cce97_00001
  val/loss: 0.09279364347457886
  
Result for LightningTrainer_cce97_00000:
  _report_on: train_epoch_end
  date: 2023-07-03_01-09-07
  done: false
  epoch: 1
  hostname: lambda2
  iterations_since_restore: 2
  node_ip: 131.179.80.122
  pid: 8205
  should_checkpoint: true
  step: 1600
  time_since_restore: 33.126001834869385
  time_this_iter_s: 9.408638715744019
  time_total_s: 33.126001834869385
  timestamp: 1688371747
  train/loss: 0.08117934316396713
  training_iteration: 2
  trial_id: cce97_00000
  val/loss: 0.10229046642780304
  
== Status ==
Current time: 2023-07-03 01:09:12 (running for 00:00:40.68)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: -0.10229046642780304 | Iter 1.000: -0.09460743144154549
Logical resource usage: 16.0/32 CPUs, 2.0/4 GPUs (0.0/1.0 accelerator_type:RTX)
Current best trial: cce97_00001 with val/loss=0.09279364347457886 and parameters={'lightning_config': {'_module_init_config': {'lr': 0.006509974933809896}, '_trainer_init_config': {}, '_trainer_fit_params': {}, '_ddp_strategy_config': {}, '_model_checkpoint_config': {}}}
Result logdir: /home/davina/.guild/runs/b5e3f4eeb46e4a3b96dde8d3605e97a9/ray_results/mwe
Number of trials: 2/2 (2 RUNNING)
+------------------------------+----------+---------------------+------------------------+--------+------------------+--------------+------------+---------+
| Trial name                   | status   | loc                 |   lightning_config/_mo |   iter |   total time (s) |   train/loss |   val/loss |   epoch |
|                              |          |                     |    dule_init_config/lr |        |                  |              |            |         |
|------------------------------+----------+---------------------+------------------------+--------+------------------+--------------+------------+---------|
| LightningTrainer_cce97_00000 | RUNNING  | 131.179.80.122:8205 |             0.0611121  |      2 |          33.126  |    0.0811793 |  0.10229   |       1 |
| LightningTrainer_cce97_00001 | RUNNING  | 131.179.80.122:8642 |             0.00650997 |      1 |          25.6019 |    0.0973598 |  0.0927936 |       0 |
+------------------------------+----------+---------------------+------------------------+--------+------------------+--------------+------------+---------+


Result for LightningTrainer_cce97_00001:
  _report_on: train_epoch_end
  date: 2023-07-03_01-09-13
  done: false
  epoch: 1
  hostname: lambda2
  iterations_since_restore: 2
  node_ip: 131.179.80.122
  pid: 8642
  should_checkpoint: true
  step: 1600
  time_since_restore: 34.74346113204956
  time_this_iter_s: 9.141553401947021
  time_total_s: 34.74346113204956
  timestamp: 1688371752
  train/loss: 0.0766768828034401
  training_iteration: 2
  trial_id: cce97_00001
  val/loss: 0.0919446125626564
  
Result for LightningTrainer_cce97_00000:
  _report_on: train_epoch_end
  date: 2023-07-03_01-09-16
  done: false
  epoch: 2
  hostname: lambda2
  iterations_since_restore: 3
  node_ip: 131.179.80.122
  pid: 8205
  should_checkpoint: true
  step: 2400
  time_since_restore: 42.46973657608032
  time_this_iter_s: 9.343734741210938
  time_total_s: 42.46973657608032
  timestamp: 1688371756
  train/loss: 0.08950082212686539
  training_iteration: 3
  trial_id: cce97_00000
  val/loss: 0.09627053141593933
  
== Status ==
Current time: 2023-07-03 01:09:22 (running for 00:00:50.03)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: -0.09711753949522972 | Iter 1.000: -0.09460743144154549
Logical resource usage: 16.0/32 CPUs, 2.0/4 GPUs (0.0/1.0 accelerator_type:RTX)
Current best trial: cce97_00001 with val/loss=0.0919446125626564 and parameters={'lightning_config': {'_module_init_config': {'lr': 0.006509974933809896}, '_trainer_init_config': {}, '_trainer_fit_params': {}, '_ddp_strategy_config': {}, '_model_checkpoint_config': {}}}
Result logdir: /home/davina/.guild/runs/b5e3f4eeb46e4a3b96dde8d3605e97a9/ray_results/mwe
Number of trials: 2/2 (2 RUNNING)
+------------------------------+----------+---------------------+------------------------+--------+------------------+--------------+------------+---------+
| Trial name                   | status   | loc                 |   lightning_config/_mo |   iter |   total time (s) |   train/loss |   val/loss |   epoch |
|                              |          |                     |    dule_init_config/lr |        |                  |              |            |         |
|------------------------------+----------+---------------------+------------------------+--------+------------------+--------------+------------+---------|
| LightningTrainer_cce97_00000 | RUNNING  | 131.179.80.122:8205 |             0.0611121  |      3 |          42.4697 |    0.0895008 |  0.0962705 |       2 |
| LightningTrainer_cce97_00001 | RUNNING  | 131.179.80.122:8642 |             0.00650997 |      2 |          34.7435 |    0.0766769 |  0.0919446 |       1 |
+------------------------------+----------+---------------------+------------------------+--------+------------------+--------------+------------+---------+


Result for LightningTrainer_cce97_00001:
  _report_on: train_epoch_end
  date: 2023-07-03_01-09-22
  done: false
  epoch: 2
  hostname: lambda2
  iterations_since_restore: 3
  node_ip: 131.179.80.122
  pid: 8642
  should_checkpoint: true
  step: 2400
  time_since_restore: 44.102758169174194
  time_this_iter_s: 9.359297037124634
  time_total_s: 44.102758169174194
  timestamp: 1688371762
  train/loss: 0.08541711419820786
  training_iteration: 3
  trial_id: cce97_00001
  val/loss: 0.09136997163295746
  
Result for LightningTrainer_cce97_00000:
  _report_on: train_epoch_end
  date: 2023-07-03_01-09-26
  done: false
  epoch: 3
  hostname: lambda2
  iterations_since_restore: 4
  node_ip: 131.179.80.122
  pid: 8205
  should_checkpoint: true
  step: 3200
  time_since_restore: 51.75059175491333
  time_this_iter_s: 9.280855178833008
  time_total_s: 51.75059175491333
  timestamp: 1688371766
  train/loss: 0.09037958085536957
  training_iteration: 4
  trial_id: cce97_00000
  val/loss: 0.10074372589588165
  
== Status ==
Current time: 2023-07-03 01:09:31 (running for 00:00:59.30)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: -0.10074372589588165 | Iter 2.000: -0.09711753949522972 | Iter 1.000: -0.09460743144154549
Logical resource usage: 16.0/32 CPUs, 2.0/4 GPUs (0.0/1.0 accelerator_type:RTX)
Current best trial: cce97_00001 with val/loss=0.09136997163295746 and parameters={'lightning_config': {'_module_init_config': {'lr': 0.006509974933809896}, '_trainer_init_config': {}, '_trainer_fit_params': {}, '_ddp_strategy_config': {}, '_model_checkpoint_config': {}}}
Result logdir: /home/davina/.guild/runs/b5e3f4eeb46e4a3b96dde8d3605e97a9/ray_results/mwe
Number of trials: 2/2 (2 RUNNING)
+------------------------------+----------+---------------------+------------------------+--------+------------------+--------------+------------+---------+
| Trial name                   | status   | loc                 |   lightning_config/_mo |   iter |   total time (s) |   train/loss |   val/loss |   epoch |
|                              |          |                     |    dule_init_config/lr |        |                  |              |            |         |
|------------------------------+----------+---------------------+------------------------+--------+------------------+--------------+------------+---------|
| LightningTrainer_cce97_00000 | RUNNING  | 131.179.80.122:8205 |             0.0611121  |      4 |          51.7506 |    0.0903796 |   0.100744 |       3 |
| LightningTrainer_cce97_00001 | RUNNING  | 131.179.80.122:8642 |             0.00650997 |      3 |          44.1028 |    0.0854171 |   0.09137  |       2 |
+------------------------------+----------+---------------------+------------------------+--------+------------------+--------------+------------+---------+


Result for LightningTrainer_cce97_00001:
  _report_on: train_epoch_end
  date: 2023-07-03_01-09-31
  done: false
  epoch: 3
  hostname: lambda2
  iterations_since_restore: 4
  node_ip: 131.179.80.122
  pid: 8642
  should_checkpoint: true
  step: 3200
  time_since_restore: 53.20792818069458
  time_this_iter_s: 9.105170011520386
  time_total_s: 53.20792818069458
  timestamp: 1688371771
  train/loss: 0.0884844958782196
  training_iteration: 4
  trial_id: cce97_00001
  val/loss: 0.09049825370311737
  
Result for LightningTrainer_cce97_00000:
  _report_on: train_epoch_end
  date: 2023-07-03_01-09-35
  done: true
  epoch: 4
  hostname: lambda2
  iterations_since_restore: 5
  node_ip: 131.179.80.122
  pid: 8205
  should_checkpoint: true
  step: 4000
  time_since_restore: 61.428561210632324
  time_this_iter_s: 9.677969455718994
  time_total_s: 61.428561210632324
  timestamp: 1688371775
  train/loss: 0.09560998529195786
  training_iteration: 5
  trial_id: cce97_00000
  val/loss: 0.09679657220840454
  
Trial LightningTrainer_cce97_00000 completed.
[2m[36m(RayTrainWorker pid=8640)[0m `Trainer.fit` stopped: `max_epochs=5` reached.
Result for LightningTrainer_cce97_00001:
  _report_on: train_epoch_end
  date: 2023-07-03_01-09-39
  done: true
  epoch: 4
  hostname: lambda2
  iterations_since_restore: 5
  node_ip: 131.179.80.122
  pid: 8642
  should_checkpoint: true
  step: 4000
  time_since_restore: 61.15192127227783
  time_this_iter_s: 7.943993091583252
  time_total_s: 61.15192127227783
  timestamp: 1688371779
  train/loss: 0.09152068942785263
  training_iteration: 5
  trial_id: cce97_00001
  val/loss: 0.09357253462076187
  
Trial LightningTrainer_cce97_00001 completed.
== Status ==
Current time: 2023-07-03 01:09:39 (running for 00:01:07.81)
Using AsyncHyperBand: num_stopped=2
Bracket: Iter 4.000: -0.09562098979949951 | Iter 2.000: -0.09711753949522972 | Iter 1.000: -0.09460743144154549
Logical resource usage: 8.0/32 CPUs, 1.0/4 GPUs (0.0/1.0 accelerator_type:RTX)
Current best trial: cce97_00001 with val/loss=0.09357253462076187 and parameters={'lightning_config': {'_module_init_config': {'lr': 0.006509974933809896}, '_trainer_init_config': {}, '_trainer_fit_params': {}, '_ddp_strategy_config': {}, '_model_checkpoint_config': {}}}
Result logdir: /home/davina/.guild/runs/b5e3f4eeb46e4a3b96dde8d3605e97a9/ray_results/mwe
Number of trials: 2/2 (1 RUNNING, 1 TERMINATED)
+------------------------------+------------+---------------------+------------------------+--------+------------------+--------------+------------+---------+
| Trial name                   | status     | loc                 |   lightning_config/_mo |   iter |   total time (s) |   train/loss |   val/loss |   epoch |
|                              |            |                     |    dule_init_config/lr |        |                  |              |            |         |
|------------------------------+------------+---------------------+------------------------+--------+------------------+--------------+------------+---------|
| LightningTrainer_cce97_00001 | RUNNING    | 131.179.80.122:8642 |             0.00650997 |      5 |          61.1519 |    0.0915207 |  0.0935725 |       4 |
| LightningTrainer_cce97_00000 | TERMINATED | 131.179.80.122:8205 |             0.0611121  |      5 |          61.4286 |    0.09561   |  0.0967966 |       4 |
+------------------------------+------------+---------------------+------------------------+--------+------------------+--------------+------------+---------+


== Status ==
Current time: 2023-07-03 01:09:39 (running for 00:01:07.82)
Using AsyncHyperBand: num_stopped=2
Bracket: Iter 4.000: -0.09562098979949951 | Iter 2.000: -0.09711753949522972 | Iter 1.000: -0.09460743144154549
Logical resource usage: 0/32 CPUs, 0/4 GPUs (0.0/1.0 accelerator_type:RTX)
Current best trial: cce97_00001 with val/loss=0.09357253462076187 and parameters={'lightning_config': {'_module_init_config': {'lr': 0.006509974933809896}, '_trainer_init_config': {}, '_trainer_fit_params': {}, '_ddp_strategy_config': {}, '_model_checkpoint_config': {}}}
Result logdir: /home/davina/.guild/runs/b5e3f4eeb46e4a3b96dde8d3605e97a9/ray_results/mwe
Number of trials: 2/2 (2 TERMINATED)
+------------------------------+------------+---------------------+------------------------+--------+------------------+--------------+------------+---------+
| Trial name                   | status     | loc                 |   lightning_config/_mo |   iter |   total time (s) |   train/loss |   val/loss |   epoch |
|                              |            |                     |    dule_init_config/lr |        |                  |              |            |         |
|------------------------------+------------+---------------------+------------------------+--------+------------------+--------------+------------+---------|
| LightningTrainer_cce97_00000 | TERMINATED | 131.179.80.122:8205 |             0.0611121  |      5 |          61.4286 |    0.09561   |  0.0967966 |       4 |
| LightningTrainer_cce97_00001 | TERMINATED | 131.179.80.122:8642 |             0.00650997 |      5 |          61.1519 |    0.0915207 |  0.0935725 |       4 |
+------------------------------+------------+---------------------+------------------------+--------+------------------+--------------+------------+---------+


2023-07-03 01:09:39,805	INFO tune.py:945 -- Total run time: 67.84 seconds (67.82 seconds for the tuning loop).
[2m[36m(RayTrainWorker pid=8942)[0m `Trainer.fit` stopped: `max_epochs=5` reached.
```

[output.txt](output.txt)

