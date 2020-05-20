# Double printing of warnings and info

https://github.com/guildai/guildai/issues/181

## Problem

The reported behavior is by design.

Guild configures the root logger by default as it logs messages for
various reasons and configures log level to `logging.DEBUG` when
`guild --debug run ...` is used.

Handlers added by the script are applied *after* of Guild's default
log initialization. This initialization is performed by
`guild.op_main`, which is used when `main` is used to define an
operation and when a Python script is run directly.

## Recreating

To recreate the behavior, run `test.py` directly:

    $ guild run test.py

Both the Guild handler and the added handler log output:

    aaa
    INFO: [ciao] aaa
    bbbb
    WARNING: [ciao] bbbb

Run without adding the handler:

    $ guild run test.py add_handler=no

Guild's default logging behavior is used:

    INFO: [ciao] aaa
    WARNING: [ciao] bbbb

## Workarounds

### Bypass Guild log init

There are two ways to bypass Guild's log init:

- Set the environment variable `LOG_INIT_SKIP` to the value `1`
- Use `exec` with the appropriate command spec to bypass Guild's use
  of `guild.op_main` to run the operation

Both of these methods are illustrated in [`guild.yml`](guild.yml).

Run with `LOG_INIT_SKIP` environment variable:

    $ guild run no-log-init
    aaa
    bbbb

Run using `exec`:

    $ guild run alt
    aaa
    bbbb

### Avoid adding multiple handlers

If a script wants to coordinate with Guild's log init (e.g. preserve
Guild's log init behavior when being run as a Guild operation), it can
check if there are existing handlers before adding handlers.

This is illustrated by [`test2.py`](test2.py).

## Fix

The reported behavior is as designed. Refer to *Workarounds* above for
ways to bypass Guild's default log init.
