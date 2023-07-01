[Published runs](../README.md)

# mwe

| ID                   | Operation           | Started                  | Time                | Status           | Label                |
| --                   | ---------           | ---------                | ----                | ------           | -----                |
| aca3d652 | mwe | 2023&#8209;07&#8209;01 12:36:36 UTC | 0:00:21 | completed | okay resources |

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
| NUM_TRAINER_WORKERS | 1 |
| NUM_VAL_SAMPLES | 20 |
| SEED | 239 |

[flags.yml](flags.yml)
## Scalars

| Key | Step | Value |
| --- | ---- | ----- |
| mwe/version_0#epoch | 39 | 4.0 |
| mwe/version_0#hp_metric | 0 | -1.0 |
| mwe/version_0#val/loss | 39 | 0.1602104753255844 |
| mwe/version_1#epoch | 7 | 0.0 |
| mwe/version_1#hp_metric | 0 | -1.0 |
| mwe/version_1#val/loss | 7 | 0.42308664321899414 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40#ray/tune/done | 5 | 1.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40#ray/tune/epoch | 5 | 4.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40#ray/tune/iterations_since_restore | 5 | 5.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40#ray/tune/should_checkpoint | 5 | 1.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40#ray/tune/step | 5 | 40.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40#ray/tune/time_since_restore | 5 | 6.488592147827148 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40#ray/tune/time_this_iter_s | 5 | 0.422011137008667 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40#ray/tune/train/loss | 5 | 0.16710205376148224 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40#ray/tune/val/loss | 5 | 0.1602104753255844 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40#sys/mem_free | 1 | 9757356032.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40#sys/mem_total | 1 | 67119648768.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40#sys/mem_used | 1 | 18197463040.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40#sys/mem_util | 1 | 0.3540000021457672 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40#sys/swap_free | 1 | 2147479552.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40#sys/swap_total | 1 | 2147479552.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40#sys/swap_used | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40#sys/swap_util | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/done | 1 | 1.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/done | 1 | 1.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/epoch | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/epoch | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/iterations_since_restore | 1 | 1.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/iterations_since_restore | 1 | 1.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/should_checkpoint | 1 | 1.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/should_checkpoint | 1 | 1.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/step | 1 | 8.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/step | 1 | 8.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/time_since_restore | 1 | 4.79811954498291 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/time_since_restore | 1 | 4.79811954498291 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/time_this_iter_s | 1 | 4.79811954498291 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/time_this_iter_s | 1 | 4.79811954498291 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/train/loss | 1 | 0.5055351257324219 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/train/loss | 1 | 0.5055351257324219 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/val/loss | 1 | 0.42308664321899414 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#ray/tune/val/loss | 1 | 0.42308664321899414 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu/util | 1 | 0.23680000007152557 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu/util | 1 | 0.23680000007152557 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu0/util | 1 | 0.2370000034570694 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu0/util | 1 | 0.2370000034570694 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu1/util | 1 | 0.1889999955892563 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu1/util | 1 | 0.1889999955892563 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu10/util | 1 | 0.23600000143051147 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu10/util | 1 | 0.23600000143051147 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu11/util | 1 | 0.17299999296665192 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu11/util | 1 | 0.17299999296665192 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu12/util | 1 | 0.20900000631809235 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu12/util | 1 | 0.20900000631809235 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu13/util | 1 | 0.20800000429153442 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu13/util | 1 | 0.20800000429153442 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu14/util | 1 | 0.20100000500679016 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu14/util | 1 | 0.20100000500679016 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu15/util | 1 | 0.19599999487400055 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu15/util | 1 | 0.19599999487400055 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu16/util | 1 | 0.19300000369548798 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu16/util | 1 | 0.19300000369548798 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu17/util | 1 | 0.18700000643730164 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu17/util | 1 | 0.18700000643730164 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu18/util | 1 | 0.18799999356269836 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu18/util | 1 | 0.18799999356269836 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu19/util | 1 | 0.18799999356269836 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu19/util | 1 | 0.18799999356269836 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu2/util | 1 | 0.23899999260902405 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu2/util | 1 | 0.23899999260902405 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu3/util | 1 | 0.18299999833106995 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu3/util | 1 | 0.18299999833106995 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu4/util | 1 | 0.382999986410141 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu4/util | 1 | 0.382999986410141 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu5/util | 1 | 0.1860000044107437 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu5/util | 1 | 0.1860000044107437 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu6/util | 1 | 0.23899999260902405 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu6/util | 1 | 0.23899999260902405 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu7/util | 1 | 0.18400000035762787 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu7/util | 1 | 0.18400000035762787 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu8/util | 1 | 0.7279999852180481 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu8/util | 1 | 0.7279999852180481 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu9/util | 1 | 0.1889999955892563 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/cpu9/util | 1 | 0.1889999955892563 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p1/rkbps | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p1/rkbps | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p1/rps | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p1/rps | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p1/util | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p1/util | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p1/wkbps | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p1/wkbps | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p1/wps | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p1/wps | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p2/rkbps | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p2/rkbps | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p2/rps | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p2/rps | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p2/util | 1 | 0.013514000922441483 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p2/util | 1 | 0.013514000922441483 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p2/wkbps | 1 | 495.51336669921875 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p2/wkbps | 1 | 495.51336669921875 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p2/wps | 1 | 49.67646408081055 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/devnvme0n1p2/wps | 1 | 49.67646408081055 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/mem_free | 1 | 9749880832.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/mem_free | 1 | 9749880832.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/mem_total | 1 | 67119648768.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/mem_total | 1 | 67119648768.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/mem_used | 1 | 18204467200.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/mem_used | 1 | 18204467200.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/mem_util | 1 | 0.3540000021457672 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/mem_util | 1 | 0.3540000021457672 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/swap_free | 1 | 2147479552.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/swap_free | 1 | 2147479552.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/swap_total | 1 | 2147479552.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/swap_total | 1 | 2147479552.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/swap_used | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/swap_used | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/swap_util | 1 | 0.0 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48#sys/swap_util | 1 | 0.0 |

[scalars.csv](scalars.csv)
## Run Files

| Path | Type | Size | Modified | MD5 |
| ---- | ---- | ---- | -------- | --- |
| mwe/version_0/checkpoints/epoch=4-step=40.ckpt | file | 10.5K | 2023-07-01 07:36:47 UTC | 36c2906b57da6afec60321af23dbc2e1 |
| mwe/version_0/checkpoints/last.ckpt | file | 10.5K | 2023-07-01 07:36:47 UTC | 36c2906b57da6afec60321af23dbc2e1 |
| mwe/version_0/events.out.tfevents.1688215004.apache.799099.0 | file | 1.2K | 2023-07-01 07:36:47 UTC | f11d7ef48e3244840715a04fa75f40c4 |
| mwe/version_0/hparams.yaml | file | 4.9K | 2023-07-01 07:36:44 UTC | 1e3c06197ca27355a4a602c0ef3f2c2d |
| mwe/version_1/checkpoints/epoch=0-step=8.ckpt | file | 10.4K | 2023-07-01 07:36:54 UTC | 92c49d182dff8b6fc26a517363278e94 |
| mwe/version_1/checkpoints/last.ckpt | file | 10.5K | 2023-07-01 07:36:54 UTC | 863844a57383f9b7850d098c9b137825 |
| mwe/version_1/events.out.tfevents.1688215012.apache.805155.0 | file | 844 | 2023-07-01 07:36:54 UTC | 02bc622cda0976c9bf1f9ef05d7f16e0 |
| mwe/version_1/hparams.yaml | file | 4.9K | 2023-07-01 07:36:52 UTC | 1e880cc0755eeed3e19b07c42f5c03b9 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000000/.is_checkpoint | file | 0 | 2023-07-01 07:36:46 UTC | d41d8cd98f00b204e9800998ecf8427e |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000000/.metadata.pkl | file | 199 | 2023-07-01 07:36:46 UTC | 682f2a86c16bd4e757a0e38d2b61ef1b |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000000/.tune_metadata | file | 737 | 2023-07-01 07:36:46 UTC | 851958056179ec53b3eb16b28198df2d |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000000/_preprocessor | file | 4 | 2023-07-01 07:36:46 UTC | 8a76b3f1259a772a2ee2738c8264cf1f |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000000/model | file | 10.5K | 2023-07-01 07:36:46 UTC | 0823150618099e5a86b45a6a8ea2ada3 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000001/.is_checkpoint | file | 0 | 2023-07-01 07:36:46 UTC | d41d8cd98f00b204e9800998ecf8427e |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000001/.metadata.pkl | file | 199 | 2023-07-01 07:36:46 UTC | 8d026a9479386d8dd50201927c9d7719 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000001/.tune_metadata | file | 737 | 2023-07-01 07:36:46 UTC | bc2eee4fbd08c6ec124b8021edfe96e4 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000001/_preprocessor | file | 4 | 2023-07-01 07:36:46 UTC | 8a76b3f1259a772a2ee2738c8264cf1f |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000001/model | file | 10.5K | 2023-07-01 07:36:46 UTC | bfca0074dd672812208bf362e66c1b21 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000002/.is_checkpoint | file | 0 | 2023-07-01 07:36:47 UTC | d41d8cd98f00b204e9800998ecf8427e |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000002/.metadata.pkl | file | 199 | 2023-07-01 07:36:47 UTC | b89631a14e10e4124b99938fc2bb85de |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000002/.tune_metadata | file | 737 | 2023-07-01 07:36:47 UTC | e0bf952c9ec3adad621dfa3abd598986 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000002/_preprocessor | file | 4 | 2023-07-01 07:36:47 UTC | 8a76b3f1259a772a2ee2738c8264cf1f |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000002/model | file | 10.5K | 2023-07-01 07:36:47 UTC | c573ffda3809fa407df0523e205d6431 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000003/.is_checkpoint | file | 0 | 2023-07-01 07:36:47 UTC | d41d8cd98f00b204e9800998ecf8427e |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000003/.metadata.pkl | file | 199 | 2023-07-01 07:36:47 UTC | 9da9ec36bf3229ed0758f3319b643017 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000003/.tune_metadata | file | 737 | 2023-07-01 07:36:47 UTC | 2a537855e6f798bb866c42fdeac9f28d |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000003/_preprocessor | file | 4 | 2023-07-01 07:36:47 UTC | 8a76b3f1259a772a2ee2738c8264cf1f |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000003/model | file | 10.5K | 2023-07-01 07:36:47 UTC | 4b86600e4339eef1abfd112f3325754b |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000004/.is_checkpoint | file | 0 | 2023-07-01 07:36:48 UTC | d41d8cd98f00b204e9800998ecf8427e |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000004/.metadata.pkl | file | 199 | 2023-07-01 07:36:48 UTC | 1b76a8632eba4744e5fc29ff00706f98 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000004/.tune_metadata | file | 737 | 2023-07-01 07:36:48 UTC | 9d652c22ab8803250af1cac3dcb88e52 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000004/_preprocessor | file | 4 | 2023-07-01 07:36:48 UTC | 8a76b3f1259a772a2ee2738c8264cf1f |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/checkpoint_000004/model | file | 10.5K | 2023-07-01 07:36:47 UTC | 36c2906b57da6afec60321af23dbc2e1 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/events.out.tfevents.1688215000.apache | file | 6.7K | 2023-07-01 07:36:48 UTC | 97c2e0a1f5c53d56d542e72bbee7d42c |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/params.json | file | 230 | 2023-07-01 07:36:40 UTC | ec662cd4e04a3b6de8683896abdf28f5 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/params.pkl | file | 180 | 2023-07-01 07:36:40 UTC | eb10b1c43be2cdde240801ab830bf3ba |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/progress.csv | file | 1.2K | 2023-07-01 07:36:48 UTC | 9ea532abb5f3713ba8a08152ea801119 |
| ray_results/mwe/LightningTrainer_ed5a9_00000_0_lr=0.0028_2023-07-01_07-36-40/result.json | file | 3.4K | 2023-07-01 07:36:48 UTC | e8ce52c6a9268eeb3d79d989565b1c82 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48/checkpoint_000000/.is_checkpoint | file | 0 | 2023-07-01 07:36:54 UTC | d41d8cd98f00b204e9800998ecf8427e |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48/checkpoint_000000/.metadata.pkl | file | 199 | 2023-07-01 07:36:54 UTC | 682f2a86c16bd4e757a0e38d2b61ef1b |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48/checkpoint_000000/.tune_metadata | file | 737 | 2023-07-01 07:36:54 UTC | 864a642e052d8bbe20881ba303401fce |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48/checkpoint_000000/_preprocessor | file | 4 | 2023-07-01 07:36:54 UTC | 8a76b3f1259a772a2ee2738c8264cf1f |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48/checkpoint_000000/model | file | 10.5K | 2023-07-01 07:36:54 UTC | 863844a57383f9b7850d098c9b137825 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48/events.out.tfevents.1688215008.apache | file | 19.4K | 2023-07-01 07:36:54 UTC | 726abdbafa7985278b22107afae1c66a |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48/params.json | file | 231 | 2023-07-01 07:36:48 UTC | 24cfc74412b1ca6d14ee6a8f0f7e7fa2 |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48/params.pkl | file | 180 | 2023-07-01 07:36:48 UTC | 2a2b91ac206f8abf5177fb8195157f0a |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48/progress.csv | file | 403 | 2023-07-01 07:36:54 UTC | 687de751615ad34a79904dd5573dd31d |
| ray_results/mwe/LightningTrainer_ed5a9_00001_1_lr=0.0051_2023-07-01_07-36-48/result.json | file | 687 | 2023-07-01 07:36:54 UTC | 49a6d36b801214527032a9cb09ce4116 |
| ray_results/mwe/basic-variant-state-2023-07-01_07-36-40.json | file | 6.6K | 2023-07-01 07:36:54 UTC | 959ad219c1db539a567ac36013d7e1b5 |
| ray_results/mwe/experiment_state-2023-07-01_07-36-40.json | file | 34.9K | 2023-07-01 07:36:54 UTC | aac81ec301192676fe098e9b6119c972 |
| ray_results/mwe/trainable.pkl | file | 7.9K | 2023-07-01 07:36:38 UTC | b2cc969807cf13463e229a68ff6c6a74 |
| ray_results/mwe/tuner.pkl | file | 1.4K | 2023-07-01 07:36:38 UTC | 73302c8cb62329bdfb6da3deb9275af3 |

[runfiles.csv](runfiles.csv)
## Source Code

| Path | Size | Modified | MD5 |
| ---- | ---- | -------- | --- |
| [FIX.md](sourcecode/FIX.md) | 182 | 2023-07-01 07:36:36 UTC | f651494c34eceb07582b05812276a57c |
| [README.md](sourcecode/README.md) | 1.4K | 2023-07-01 07:36:36 UTC | 93cff220c682543cd75dcacb2b6b925d |
| [guild.yml](sourcecode/guild.yml) | 211 | 2023-07-01 07:36:36 UTC | 91c04e6e0e225b3fba5223af9d17e737 |
| [mwe.py](sourcecode/mwe.py) | 5.6K | 2023-07-01 07:36:36 UTC | 16bdb36b80e2f765afdbde12b75b3e60 |
| [requirements.txt](sourcecode/requirements.txt) | 71 | 2023-07-01 07:36:36 UTC | f0bd64d1b02c027d4968fedb904967d2 |

[sourcecode.csv](sourcecode.csv)
## Output

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


[2m[36m(RayTrainWorker pid=799099)[0m 2023-07-01 07:36:42,795	INFO config.py:86 -- Setting up process group for: env:// [rank=0, world_size=1]
[2m[36m(RayTrainWorker pid=799099)[0m /home/garrett/Code/guild-issues/my.guild.ai-1050-guild-interfering-with-distributed-resource-allocation-pytorch-lightning-ray-tune/.venv/lib/python3.10/site-packages/torch/cuda/__init__.py:546: UserWarning: Can't initialize NVML
[2m[36m(RayTrainWorker pid=799099)[0m   warnings.warn("Can't initialize NVML")
[2m[36m(RayTrainWorker pid=799099)[0m GPU available: True (cuda), used: True
[2m[36m(RayTrainWorker pid=799099)[0m TPU available: False, using: 0 TPU cores
[2m[36m(RayTrainWorker pid=799099)[0m IPU available: False, using: 0 IPUs
[2m[36m(RayTrainWorker pid=799099)[0m HPU available: False, using: 0 HPUs
[2m[36m(RayTrainWorker pid=799099)[0m You are using a CUDA device ('NVIDIA RTX A1000 Laptop GPU') that has Tensor Cores. To properly utilize them, you should set `torch.set_float32_matmul_precision('medium' | 'high')` which will trade-off precision for performance. For more details, read https://pytorch.org/docs/stable/generated/torch.set_float32_matmul_precision.html#torch.set_float32_matmul_precision
[2m[36m(RayTrainWorker pid=799099)[0m Missing logger folder: /home/garrett/.guild/runs/aca3d6526c03439d8503f4d418d8b9c0/mwe
[2m[36m(RayTrainWorker pid=799099)[0m LOCAL_RANK: 0 - CUDA_VISIBLE_DEVICES: [0]
[2m[36m(RayTrainWorker pid=799099)[0m 
[2m[36m(RayTrainWorker pid=799099)[0m   | Name | Type    | Params
[2m[36m(RayTrainWorker pid=799099)[0m ---------------------------------
[2m[36m(RayTrainWorker pid=799099)[0m 0 | loss | MSELoss | 0     
[2m[36m(RayTrainWorker pid=799099)[0m 1 | fc1  | Linear  | 55    
[2m[36m(RayTrainWorker pid=799099)[0m 2 | fc2  | Linear  | 60    
[2m[36m(RayTrainWorker pid=799099)[0m ---------------------------------
[2m[36m(RayTrainWorker pid=799099)[0m 115       Trainable params
[2m[36m(RayTrainWorker pid=799099)[0m 0         Non-trainable params
[2m[36m(RayTrainWorker pid=799099)[0m 115       Total params
[2m[36m(RayTrainWorker pid=799099)[0m 0.000     Total estimated model params size (MB)
[2m[36m(RayTrainWorker pid=799099)[0m 2023-07-01 07:36:44.253096: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
[2m[36m(RayTrainWorker pid=799099)[0m /home/garrett/Code/guild-issues/my.guild.ai-1050-guild-interfering-with-distributed-resource-allocation-pytorch-lightning-ray-tune/.venv/lib/python3.10/site-packages/pytorch_lightning/trainer/connectors/logger_connector/result.py:432: PossibleUserWarning: It is recommended to use `self.log('val/loss', ..., sync_dist=True)` when logging on epoch level in distributed setting to accumulate the metric across devices.
[2m[36m(RayTrainWorker pid=799099)[0m   warning_cache.warn(
[2m[36m(RayTrainWorker pid=799099)[0m /home/garrett/Code/guild-issues/my.guild.ai-1050-guild-interfering-with-distributed-resource-allocation-pytorch-lightning-ray-tune/.venv/lib/python3.10/site-packages/pytorch_lightning/loops/fit_loop.py:280: PossibleUserWarning: The number of training batches (8) is smaller than the logging interval Trainer(log_every_n_steps=50). Set a lower value for log_every_n_steps if you want to see logs for the training epoch.
[2m[36m(RayTrainWorker pid=799099)[0m   rank_zero_warn(
Result for LightningTrainer_ed5a9_00000:
  _report_on: train_epoch_end
  date: 2023-07-01_07-36-46
  done: false
  epoch: 0
  hostname: apache
  iterations_since_restore: 1
  node_ip: 192.168.1.206
  pid: 799019
  should_checkpoint: true
  step: 8
  time_since_restore: 4.791827440261841
  time_this_iter_s: 4.791827440261841
  time_total_s: 4.791827440261841
  timestamp: 1688215006
  train/loss: 0.480129599571228
  training_iteration: 1
  trial_id: ed5a9_00000
  val/loss: 0.40802401304244995
  
== Status ==
Current time: 2023-07-01 07:36:46 (running for 00:00:06.25)
Using AsyncHyperBand: num_stopped=0
Bracket: Iter 4.000: None | Iter 2.000: None | Iter 1.000: -0.40802401304244995
Logical resource usage: 8.0/20 CPUs, 1.0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Current best trial: ed5a9_00000 with val/loss=0.40802401304244995 and parameters={'lightning_config': {'_module_init_config': {'lr': 0.002799278522512412}, '_trainer_init_config': {}, '_trainer_fit_params': {}, '_ddp_strategy_config': {}, '_model_checkpoint_config': {}}}
Result logdir: /home/garrett/.guild/runs/aca3d6526c03439d8503f4d418d8b9c0/ray_results/mwe
Number of trials: 2/2 (1 PENDING, 1 RUNNING)
+------------------------------+----------+----------------------+------------------------+--------+------------------+--------------+------------+---------+
| Trial name                   | status   | loc                  |   lightning_config/_mo |   iter |   total time (s) |   train/loss |   val/loss |   epoch |
|                              |          |                      |    dule_init_config/lr |        |                  |              |            |         |
|------------------------------+----------+----------------------+------------------------+--------+------------------+--------------+------------+---------|
| LightningTrainer_ed5a9_00000 | RUNNING  | 192.168.1.206:799019 |             0.00279928 |      1 |          4.79183 |      0.48013 |   0.408024 |       0 |
| LightningTrainer_ed5a9_00001 | PENDING  |                      |             0.00513599 |        |                  |              |            |         |
+------------------------------+----------+----------------------+------------------------+--------+------------------+--------------+------------+---------+


Result for LightningTrainer_ed5a9_00000:
  _report_on: train_epoch_end
  date: 2023-07-01_07-36-48
  done: true
  epoch: 4
  hostname: apache
  iterations_since_restore: 5
  node_ip: 192.168.1.206
  pid: 799019
  should_checkpoint: true
  step: 40
  time_since_restore: 6.488592147827148
  time_this_iter_s: 0.422011137008667
  time_total_s: 6.488592147827148
  timestamp: 1688215007
  train/loss: 0.16710205376148224
  training_iteration: 5
  trial_id: ed5a9_00000
  val/loss: 0.1602104753255844
  
Trial LightningTrainer_ed5a9_00000 completed.
[2m[36m(RayTrainWorker pid=799099)[0m `Trainer.fit` stopped: `max_epochs=5` reached.
[2m[36m(RayTrainWorker pid=805155)[0m 2023-07-01 07:36:50,789	INFO config.py:86 -- Setting up process group for: env:// [rank=0, world_size=1]
[2m[36m(RayTrainWorker pid=805155)[0m /home/garrett/Code/guild-issues/my.guild.ai-1050-guild-interfering-with-distributed-resource-allocation-pytorch-lightning-ray-tune/.venv/lib/python3.10/site-packages/torch/cuda/__init__.py:546: UserWarning: Can't initialize NVML
[2m[36m(RayTrainWorker pid=805155)[0m   warnings.warn("Can't initialize NVML")
[2m[36m(RayTrainWorker pid=805155)[0m GPU available: True (cuda), used: True
[2m[36m(RayTrainWorker pid=805155)[0m TPU available: False, using: 0 TPU cores
[2m[36m(RayTrainWorker pid=805155)[0m IPU available: False, using: 0 IPUs
[2m[36m(RayTrainWorker pid=805155)[0m HPU available: False, using: 0 HPUs
[2m[36m(RayTrainWorker pid=805155)[0m You are using a CUDA device ('NVIDIA RTX A1000 Laptop GPU') that has Tensor Cores. To properly utilize them, you should set `torch.set_float32_matmul_precision('medium' | 'high')` which will trade-off precision for performance. For more details, read https://pytorch.org/docs/stable/generated/torch.set_float32_matmul_precision.html#torch.set_float32_matmul_precision
[2m[36m(RayTrainWorker pid=805155)[0m LOCAL_RANK: 0 - CUDA_VISIBLE_DEVICES: [0]
[2m[36m(RayTrainWorker pid=805155)[0m 
[2m[36m(RayTrainWorker pid=805155)[0m   | Name | Type    | Params
[2m[36m(RayTrainWorker pid=805155)[0m ---------------------------------
[2m[36m(RayTrainWorker pid=805155)[0m 0 | loss | MSELoss | 0     
[2m[36m(RayTrainWorker pid=805155)[0m 1 | fc1  | Linear  | 55    
[2m[36m(RayTrainWorker pid=805155)[0m 2 | fc2  | Linear  | 60    
[2m[36m(RayTrainWorker pid=805155)[0m ---------------------------------
[2m[36m(RayTrainWorker pid=805155)[0m 115       Trainable params
[2m[36m(RayTrainWorker pid=805155)[0m 0         Non-trainable params
[2m[36m(RayTrainWorker pid=805155)[0m 115       Total params
[2m[36m(RayTrainWorker pid=805155)[0m 0.000     Total estimated model params size (MB)
[2m[36m(RayTrainWorker pid=805155)[0m 2023-07-01 07:36:52.239451: W tensorflow/compiler/tf2tensorrt/utils/py_utils.cc:38] TF-TRT Warning: Could not find TensorRT
== Status ==
Current time: 2023-07-01 07:36:53 (running for 00:00:13.01)
Using AsyncHyperBand: num_stopped=1
Bracket: Iter 4.000: -0.21034686267375946 | Iter 2.000: -0.3374544680118561 | Iter 1.000: -0.40802401304244995
Logical resource usage: 8.0/20 CPUs, 1.0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Current best trial: ed5a9_00000 with val/loss=0.1602104753255844 and parameters={'lightning_config': {'_module_init_config': {'lr': 0.002799278522512412}, '_trainer_init_config': {}, '_trainer_fit_params': {}, '_ddp_strategy_config': {}, '_model_checkpoint_config': {}}}
Result logdir: /home/garrett/.guild/runs/aca3d6526c03439d8503f4d418d8b9c0/ray_results/mwe
Number of trials: 2/2 (1 RUNNING, 1 TERMINATED)
+------------------------------+------------+----------------------+------------------------+--------+------------------+--------------+------------+---------+
| Trial name                   | status     | loc                  |   lightning_config/_mo |   iter |   total time (s) |   train/loss |   val/loss |   epoch |
|                              |            |                      |    dule_init_config/lr |        |                  |              |            |         |
|------------------------------+------------+----------------------+------------------------+--------+------------------+--------------+------------+---------|
| LightningTrainer_ed5a9_00001 | RUNNING    | 192.168.1.206:805068 |             0.00513599 |        |                  |              |            |         |
| LightningTrainer_ed5a9_00000 | TERMINATED | 192.168.1.206:799019 |             0.00279928 |      5 |          6.48859 |     0.167102 |    0.16021 |       4 |
+------------------------------+------------+----------------------+------------------------+--------+------------------+--------------+------------+---------+


[2m[36m(RayTrainWorker pid=805155)[0m /home/garrett/Code/guild-issues/my.guild.ai-1050-guild-interfering-with-distributed-resource-allocation-pytorch-lightning-ray-tune/.venv/lib/python3.10/site-packages/pytorch_lightning/trainer/connectors/logger_connector/result.py:432: PossibleUserWarning: It is recommended to use `self.log('val/loss', ..., sync_dist=True)` when logging on epoch level in distributed setting to accumulate the metric across devices.
[2m[36m(RayTrainWorker pid=805155)[0m   warning_cache.warn(
[2m[36m(RayTrainWorker pid=805155)[0m /home/garrett/Code/guild-issues/my.guild.ai-1050-guild-interfering-with-distributed-resource-allocation-pytorch-lightning-ray-tune/.venv/lib/python3.10/site-packages/pytorch_lightning/loops/fit_loop.py:280: PossibleUserWarning: The number of training batches (8) is smaller than the logging interval Trainer(log_every_n_steps=50). Set a lower value for log_every_n_steps if you want to see logs for the training epoch.
[2m[36m(RayTrainWorker pid=805155)[0m   rank_zero_warn(
Result for LightningTrainer_ed5a9_00001:
  _report_on: train_epoch_end
  date: 2023-07-01_07-36-54
  done: true
  epoch: 0
  hostname: apache
  iterations_since_restore: 1
  node_ip: 192.168.1.206
  pid: 805068
  should_checkpoint: true
  step: 8
  time_since_restore: 4.798119306564331
  time_this_iter_s: 4.798119306564331
  time_total_s: 4.798119306564331
  timestamp: 1688215014
  train/loss: 0.5055351257324219
  training_iteration: 1
  trial_id: ed5a9_00001
  val/loss: 0.42308664321899414
  
Trial LightningTrainer_ed5a9_00001 completed.
== Status ==
Current time: 2023-07-01 07:36:54 (running for 00:00:14.26)
Using AsyncHyperBand: num_stopped=2
Bracket: Iter 4.000: -0.21034686267375946 | Iter 2.000: -0.3374544680118561 | Iter 1.000: -0.41555532813072205
Logical resource usage: 0/20 CPUs, 0/1 GPUs (0.0/1.0 accelerator_type:RTX)
Current best trial: ed5a9_00000 with val/loss=0.1602104753255844 and parameters={'lightning_config': {'_module_init_config': {'lr': 0.002799278522512412}, '_trainer_init_config': {}, '_trainer_fit_params': {}, '_ddp_strategy_config': {}, '_model_checkpoint_config': {}}}
Result logdir: /home/garrett/.guild/runs/aca3d6526c03439d8503f4d418d8b9c0/ray_results/mwe
Number of trials: 2/2 (2 TERMINATED)
+------------------------------+------------+----------------------+------------------------+--------+------------------+--------------+------------+---------+
| Trial name                   | status     | loc                  |   lightning_config/_mo |   iter |   total time (s) |   train/loss |   val/loss |   epoch |
|                              |            |                      |    dule_init_config/lr |        |                  |              |            |         |
|------------------------------+------------+----------------------+------------------------+--------+------------------+--------------+------------+---------|
| LightningTrainer_ed5a9_00000 | TERMINATED | 192.168.1.206:799019 |             0.00279928 |      5 |          6.48859 |     0.167102 |   0.16021  |       4 |
| LightningTrainer_ed5a9_00001 | TERMINATED | 192.168.1.206:805068 |             0.00513599 |      1 |          4.79812 |     0.505535 |   0.423087 |       0 |
+------------------------------+------------+----------------------+------------------------+--------+------------------+--------------+------------+---------+


2023-07-01 07:36:54,360	INFO tune.py:945 -- Total run time: 14.27 seconds (14.26 seconds for the tuning loop).
```

[output.txt](output.txt)

