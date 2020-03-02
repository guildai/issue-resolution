# Guild remote output not visible until finished

https://github.com/guildai/guildai/issues/72

## Problem

Guild is buffering lines at two points:

- Watch command
- Run output processing

These issues are fixed in `0.7.0.rc8`.

## Recreating

Requirements:

- guildai<=0.7.0.rc7
- tqdm (required if `use_tqdm=yes` is specified - see below)

### SSH remote config

This test runs on a remote named `localhost`. You can use any host
that you have ssh access to.

Create an ssh remote in `~/.guild/config.yml`:

``` yaml
remotes:
  type: ssh
  host: localhost
```

Save your changes and confirm that you can connect:

```
$ guild remote status localhost
```

You should see:

```
localhost (localhost) is available
```

### Run test on remote

Run the [test op](test.py):

```
$ guild run test -r localhost
```

Guild does not print the progress until the operation completes.

## Workarounds

There are no workarounds. Upgrade to `0.7.0.rc8` or later for a fix.

## Fix

Fixed in `0.7.0.rc8`.

## Related Issues

Possibly:

- https://github.com/guildai/guildai/issues/54
