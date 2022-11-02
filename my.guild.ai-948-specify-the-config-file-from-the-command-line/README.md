---
doctest-type: bash
---

# Specify the config file from the command line?

https://my.guild.ai/t/specify-the-config-file-from-the-command-line/948

## Problem

User wants to change the config file used in a `flags-dest` spec using a flag
value.

## Recreating

These tests should be run with Guild 0.8.2 or earlier.

    $ guild check -n --version '<=0.8.2'
    <exit 0>

### Basic example

The [`test-basic`](guild.yml#L1-L7) operation uses the [`config
file`](config.yml) specified in the Guild file. This corresponds to the OP.

    $ guild run test-basic --help-op
    ...
    Flags:
      msg  (default is hello)

    $ guild run test-basic -y
    Resolving config:config.yml
    hello

### Enable a flag for the config

The operation [`test-basic-with-flag`](guild.yml#L9-L29) exposes the config
file as a flag.

    $ guild run test-basic-with-flag --help-op
    ...
    Flags:
      config  Config file to use
      msg     Message to print (default is hello)

    $ guild run test-basic-with-flag -y
    Resolving config
    hello

    $ guild run test-basic-with-flag config=config-2.yml -y
    Resolving config
    Using config-2.yml for config resource
    hello

Note this is NOT what we expect -- we expect to get the flag values from
[`config-2.yml`](config-2.yml):

    $ cat config-2.yml
    msg: hola

Instead we got the flag values defined in [`config.yml`](config.yml) because
those values are imported and then written to the run directory when the config
resource is resolved.

## Workarounds

The underlying problem is that Guild uses Guild-file-specified config file when
it imports flag values. It ought to first resolve flags defined in the Guild
file and then use those values when it resolves a file for flag imports.

As a workaround, we need to disable flag imports and define any
command-line-modifiable flags explicitly in the Guild file.

The [`test-without-flag-import`](guild.yml#L29-L45) operation does this.

    $ guild run test-without-flag-import --help-op
    ...
    Flags:
      config  Config file to use
      msg     Message to print

The flags here are defined explicitly in the Guild file -- they aren't
imported.

When we run the operation without any flags, we get the config defined in
[`config.yml`](config.yml).

    $ guild run test-without-flag-import -y
    Resolving config
    hello

We can change the value for `msg` on the command line as expected.

    $ guild run test-without-flag-import msg=whoop -y
    Resolving config
    whoop

We can also change the config file used.

    $ guild run test-without-flag-import config=config-2.yml -y
    Resolving config
    Using config-2.yml for config resource
    hola

The value for `msg` here is defined in [`config-2.yml`].

    $ cat config-2.yml
    msg: hola

Finally, we can override the value for 'msg' even when specifying a different
config file.

    $ guild run test-without-flag-import config=config-2.yml msg=whoop -y
    Resolving config
    Using config-2.yml for config resource
    whoop

Note that any flag that the user can override must explicitly be defined in the
Guild file. Any attempt to import flag values will trigger the problems above
-- those values will always come from the specified configuration file and end
up replacing the values in alternative config files.

## Fix

Guild should resolve flags explicitly defined in the Guild file before
importing flags as those initial flag values can influence where Guild imports
flags from.

Additionally, the configuration required to pull this off is nearly black magic
levels! Guild should make this MUCH easier.
