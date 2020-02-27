# Guild remote output not visible until finished

https://github.com/guildai/guildai/issues/72

## Problem

Guild appears to be buffering ssh output per line, which hides any
progress updates that display on a single line.

## Recreating

Requirements:

- guildai<=0.7.0.rc6

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

None at this time.

## Fix

Under development.

## Related Issues

Possibly:

- https://github.com/guildai/guildai/issues/54
