# guild: command not found' using remote conda environment

https://github.com/guildai/guildai/issues/150

## Problem

Guild command not found due to ssh without shell/tty.

## Recreating

Requirements:

- guild<=0.7.0.rc9

See https://github.com/guildai/guildai/issues/150 for details.

## Workarounds

### Use env activation to set PATH

Use an environment by specifying `guild-env` or `conda-env` and edit
the activation script (e.g. `<venv>/bin/activate` for virtualenv/Guild
envs) to set `PATH` to include the Guild location.

The remote attr `venv-activate` can be used to set `PATH` as well.

``` yaml
remotes:
  my-remote:
    venv-activate: PATH=<path that inludes Guild>
```

To force the behavior of ssh via terminal, use `venv-activate` to
source the appropriate bash init.

``` yaml
remotes:
  my-remote:
    venv-activate: source ~/.bashrc
```

### Define a symlink to Guild in available path

If setting the PATH via activation above for some reason doesn't work,
create a symlink to Guild in the available PATH.

Get the `PATH` available for ssh commands:

```
[local] $ ssh remote-host 'bash -c echo $PATH'
```

Get the full path to Guild by ssh'ing to the remote host and running:

```
[remote-host] $ which guild
```

On the remote host, create a symlink somewhere on the `PATH` from
above to the location of `guild`.

## Fix

Pending.

Guild should do a better job finding remote Guild's
location. Currently Guild requires that remote Guild be on the
`PATH`.
