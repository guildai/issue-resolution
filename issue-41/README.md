# Hash of source code in compare

https://github.com/guildai/guildai/issues/41

## Problem

As of guildai<=0.6.6.dev2

When comparing runs, Guild does not provide any indication that the
source code across the runs is the same or different. Knowing if the
source code is different lets a user investigate further using the
`diff` command. Without an indication, a user has to speculatively run
`diff` on various run combinations.

## Request

Guild should include a source code digest in the compare view:

```
run       operation  started              time     status     label  sourcecode  step  accuracy
456e4219  train      2019-08-06 08:32:41  0:00:00  completed         784ba0e9    2     0.567000
12b605aa  train      2019-08-06 08:23:50  0:00:00  completed         784ba0e9    2     0.567000
7b7ee1f3  train      2019-08-06 08:14:33  0:00:00  completed         991c3ccf    2     0.456000
```

At a glance, it's easy to see that the source code changed between the
last run displayed the first two. While a user doesn't know what
changed, she now can run `diff` across the applicable runs.

Guild should also show the full source code digest in `runs info`:

```
id: e1e9e079824243ef8e2f134ea05491c2
operation: ./SCM/guild-issues/issue-39/ikostrikov:relative-paths
status: completed
started: 2019-08-06 12:58:52
stopped: 2019-08-06 12:58:53
marked: no
label:
sourcecode: 991c3ccfd295262492467d81d01e8a17
run_dir: ~/.guild/runs/e1e9e079824243ef8e2f134ea05491c2
command: /usr/bin/python -um guild.op_main guild.pass --
exit_status: 0
pid:
flags:
```

## Proposal

Guild will generate a unigue digest for the source code files it
copies for a run. Guild will save that digest as a run attribute
(e.g. `RUN_DIR/.guild/attrs/sourecode`).

By default, Guild will include the first 8 characters of the digest
under the `sourcecode` column in Compare.

Guild will display the full `sourcecode` attribute in the `runs info`
command.

### Generating source code digest

Guild should generate a digest that can be replicated across systems
so that a digest for a set of source files on one system is the same
for those files on any other system.

In particular:

- Digests should be updated using file names relative to the source
  code destinations in alphabetical order and with file byte contents
- Guild should not perform line ending conversions

It's tempting to optimize this process by using file size and
modification dates. However this would cause digests to differ across
systems. Again, the same digest generated on different systems should
indicate that the associated soure code files are identical.

### Default behavior

This is potentially expensive operation, especially in default cases
where a Guild file does not specify a `sourcecode` spec for an
operation. Guild already has safeguards to protect against
accidentally copying many text files or large text files in its
default mode.

That said, the safeguards ensure that any digests on uncontrolled
files (i.e. cases where `sourcecode` is not specified for an operation
in a Guild file) are limited to the max matches and max size limits.

We might consider NOT generating digests unless a `sourecode` spec is
provided.

**Working decision:** Generate digests in all cases until we have
information to suggest this is a bad idea.

### Disabling digests

The `sourcecode` spec should support a `digest: yes | no` attribute to
disable the behavior.

Digests must be either generated on the full set of source code files
or not at all, in which case the digest value is empty/null.

## Related Issues

- [Save system info, ala sourcecode snapshots](../issue-42)
