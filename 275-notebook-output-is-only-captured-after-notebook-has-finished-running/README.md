# Notebook output is only captured after notebook has finished running

https://github.com/guildai/guildai/issues/275

## Problem

Guild uses `jupyter-nbconvert` to execute a notebook in-place. This
command does not render output as it executes. Guild reads output
after the command is executed. This makes it impossible to record
output scalars before the notebook executes fully.

## Recreating

Requirements:

- guild<=0.7.3rc1
- See [requirements.txt](requirements.txt)

Execute `guild run test.ipynb` and in a separate terminal run `guild
tensorboard` to view progress. Scalars are not displayed until after
the notebook completes.

## Workarounds

Write scalars as they are generated to a TF event file using one of
the various [supported
methods](https://my.guild.ai/t/scalars/160#tensorboard-summaries). Since
scalars are logged explicitly, you can disable output scalars for the
operation. See [guild.yml](guild.yml) for a sample configuration.

To test the workaround provided here, run `guild run test` and run
`guild tensorboard` in a separate terminal. Refresh the view as the
notebook runs - TensorBoard should show the latest loss recorded by
the notebook as the notebook runs.

## Fix

None planned at this time. See [Workarounds](#workarounds) above for
information on logging scalars as the notebook runs.
