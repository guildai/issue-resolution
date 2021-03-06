# Reproducibility problems with file dependencies

https://github.com/guildai/guildai/issues/111

This issue is addressed in part in 0.7.0.rc10. This version supports a
`target-type: copy` option, which tells Guild to create a copy of a
source file rather than link to the source.

This is still not a complete solution. The default is to link, as
before. This is incorrect (seebelow). The default should be based on
the resource type. File and URL types should copy by
default. Operation types should link by default.

## Problem

Guild links to required files located in the project. This is a train
wreck of an idea for control over runs. Any changes to the project are
reflected in past runs, negating the purported values of experiment
tracking in the first place!

This is also a problem, though much less so, for linked cached
resources.

Guild needs a way to copy into the run directory required resources.

I think an exception to this is operation dependencies. Since these
are runs that in turn are carefully managed, we should be able to
safely link. We're left with the problem of dependencies across runs,
but we can tackle this as a separate concern.

## Recreating

Requirements:

- guild<=0.7.0.rc9

Change to this directory and run:

    $ guild run test-default -y

Cat the run file `msg.txt`:

    $ guild cat -p msg.txt
    Hello

Modify the local `msg.txt` file:

    $ echo Hola > msg.txt

Cat the run file `msg.txt` again:

    $ guild cat -p msg.txt
    Hola

## Workarounds

As of 0.7.0.rc10, Guild supports a `target-type` attribute, which can
be set to `copy` to create copies of resources. This simulates the
correct behavior for reproducibility, though it must be enabled
explicitly until the default is changed.

To test this behavior, run the steps above but use the `test-copy`
operation. Note that `msg.txt` generated by the run is not a link, but
a copy. Changes to the project file do not effect the run.
