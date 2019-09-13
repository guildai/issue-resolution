# Guild overrides log settings configured via basicConfig

https://github.com/guildai/guildai/issues/55

## Problem

In `guild.op_main` we initialize logging. Python's `basicConfig` is
notorious for its refusal to re-initialize logging. Because we
initialize logging, naive Python log inits generally fail. This is a
bug as Guild should not tamper with standard Python functions.

## Recreating

Requirements:

- guild<=0.6.6

Run [`test.py`](test.py) using Python:

    $ python test.py
    test - INFO - Info msg
    test - WARNING - Warning msg
    test - ERROR - Error msg

Run `test.py` using Guild:

    $ guild run test.py
    INFO: [test] Info msg
    WARNING: [test] Warning msg
    ERROR: [test] Error msg

Note that Guild imposes it's own formatting on the log output.

Next, run `test.py` specifying a log file:

    $ python test.py --log-dir /tmp/guild-issue-55-test.log
    test - INFO - Info msg
    test - WARNING - Warning msg
    test - ERROR - Error msg

And view the file:

    $ cat /tmp/guild-issue-55-test.log
    test - INFO - Info msg
    test - WARNING - Warning msg
    test - ERROR - Error msg

Run the `test` operation (defined in [`guild.yml`](guild.yml), which
should cause `test.log` to be written to the run directory:

    $ guild run test -y
    INFO: [test] Info msg
    WARNING: [test] Warning msg
    ERROR: [test] Error msg

List the run files:

    $ guild ls
    ~/.guild/runs/a94e6dd5a3d5453d9d622b1b51a4672a:
      test.log

And cat the file:

    $ guild cat -p test.log
    test - INFO - Info msg
    test - WARNING - Warning msg
    test - ERROR - Error msg

Note that this file is created with the expected format!

Here's what's going on:

- Guild initializes logging first using its own config format

- `test.py` attempts to initialize logging using `basicConfig`, but
  `basicConfig` ["does nothing if the root logger already has handlers
  configured for
  it"](https://docs.python.org/3/library/logging.html#logging.basicConfig)

- `test.py` *appends* the file handler (rather than attempt to
  configure via `basicConfig`), which works as expected

## Workarounds

See `test2` operation in [`guild.yml`](guild.yml) and
[`test.py`](test.py) for a way to:

- Control the log formatting used by Guild for an operation
- Log an additional file

To test the workaround, run:

    $ guild run test2 -y
    test - INFO - Info msg
    test - WARNING - Warning msg
    test - ERROR - Error msg

And confirm that the log file is created as expected:

    $ guild cat -p test.log
    test - INFO - Info msg
    test - WARNING - Warning msg
    test - ERROR - Error msg

## Fix

As of Guild 0.6.6 this is has not been fixed. However, there is a
work-around for common cases (see above).

There are a few approaches we can take:

1. Don't init logging at all
2. Provide an option in Guild config that disables any log inits
3. Provide an env var that can be set for `guild run` commands that
   disables any log inits
4. Provide log settings in Guild config to accommodate most use cases
   (e.g. custom formats, log files, etc.)
5. Document that Guild users cannot use `basicConfig` to configure
   logging but must instead modify Guild's settings

Let's write-off options 4 and 5 as a non-starters. **Guild must not
modify default behavior in Python without a reasonably simple way to
disable the overriding behavior.**

Options 2 and 3 are on the table under the assumption that they allow
users to easily disable Guild behavior.

Option 1 should be considered a prime candidate. Why is Guild
initializing logs anyway? The behavior in `op_main` is associated with
*user code* and not a Guild command. Why does Guild need to assert
itself in user code?

One clear answer is to support debug logging. When you specify the
`--debug` option to the `guild` base command, Guild sets the log level
to `logging.DEBUG`. Without this option, we lose the ability to turn
on debug logging this way:

    $ guild --debug run test.py

Another reason that Guild initializes logs is to support plugin
logging. While Guild plugins can be disabled, they are enabled by
default (with smart disabling so non-applicable plugins aren't
used). *Plugins need support for logging.* Because of this, the
assertion that `op_main` is only associated with user code is not
entirely true.

Let's reconsider options 4 and 5. `basicConfig` failure due to other
libraries being loaded and getting first-crack at log init is a well
known problem and is independent of Guild. The work-around, which is
to add or otherwise modify pre-existing handlers, is very much
standard procedure for Python modules in this case.

We might therefore consider the following changes, which combine
options 2 through 5:

1. Introduce a `logging` attr at the model and operation levels. The
   option would support:

   - Disabling logging
   - Setting default log level
   - Setting log format

   This provides a way to control Guild's otherwise implicit log init
   behavior.

   Note that Guild should *not* support log init features beyond with
   Guild uses. E.g. Guild should not support a `filename` attr for
   writing to a file. This is something the user can reasonably do
   herself and it avoids building a dependency on Guild.

2. Support env vars that can be set on a per run basis so a user
   doesn't have to create or modify a Guild file to control Guild's
   log init behavior.

3. Document this scheme using a Guide or KB article.
