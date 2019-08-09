# flags-import matches partial arguments

https://github.com/guildai/guildai/issues/31

## Recreating

As of 0.6.5, this issue cannot be recreated.

To show the current behavior:

    $ cd issue-31
    $ ./recreate

Output should look like this:

```
The config from the issue is missing a space in '-import'. As of
0.6.5, Guild no longer loads this file:

  - model: argstest
    operations:
      train:
        main: guild_flag_test
        flags-import:
          -import

ERROR: error loading guildfile from bad-spec: error in issue-31/bad-spec/guild.yml:
invalid flags-import value '-import': expected yes/all, no, or a list of flag names
guild: guildfile in 'bad-spec' contains an error (see above for details)

When fixed, Guild loads the file:

  - model: argstest
    operations:
      train:
        main: guild_flag_test
        flags-import:
          - import

The preview looks like this:

You are about to run argstest:train
  import: test_file
Continue? (Y/n)
Terminated
```

This script does not modify your system.
