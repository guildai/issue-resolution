# Staged runs tied to project via use of Guild file

https://github.com/guildai/guildai/issues/69

## Problem

Guild staging is predicated on isolation of the staged run. Without
isolation, a staged run is a bug trap - any changes to the upstream
project can make their way into the staged run and negate the
experiment!

Guild currently uses Python system path level isolation, but only in
part. Guild still includes the project location in the system path
when running an operation. This is wrong.

Guild includes the project location to accommodate a seldom-used
feature of cross-project inheritance. Cross project inheritance
dynamically loads a Guild file across multiple sources. Each source is
included in the system path so its respective Python modules can be be
loaded.

This scheme is a train wreck for staged run!

## Recreating

Requirements:

- guild<=0.6.6

Unable to recreate - the above understanding appears to be incorrect.

## Workarounds

Pending

## Fix

Guild must save the Guild file in the run directory. The Guild file
must reflect the fully resolved data and not rely in any way on
upstream projects.

An operation must not include the project location in the Python
system path. Any Python support it needs must be available in one of
two ways: (a) as modules under the run directory, or (b) as installed
packages in the environment.

It must be possible to run a staged operation when any of the upstream
projects are missing.

UPDATE: There's a confluence of issues here. Holding off on any work
until the problem is better understood.
