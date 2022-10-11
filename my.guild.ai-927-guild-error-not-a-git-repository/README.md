---
doctest-type: bash
---

# Guild error - Not a git repository

https://my.guild.ai/t/guild-error-not-a-git-repository/927

## Problem

User code is relying on the project git repo, which is not available
in the run directory.

## Recreating

Running the test without the git repo dependency fails.

    $ guild run test-without-repo -y
    fatal: not a git repository (or any of the parent directories): .git
    ...
    subprocess.CalledProcessError: Command '['git', 'rev-parse', 'HEAD']'
    returned non-zero exit status 128.
    <exit 1>

Running with the git repo succeeds.

    $ guild run test-with-repo -y
    Resolving git-repo dependency
    HEAD: ...

We can alternative run with a link to the project git repo. Note that
this operation will yield different results if there are changes to
the git repo between the time the run is staged and the time the git
repo is read by the operation. To be safe, a copy should be used (but
at the expense of time and disk space).

    $ guild run test-with-repo-2 -y
    Resolving git-repo dependency
    HEAD: ...

## Workarounds

The behavior is by design - see [`guild.yml`](guild.yml) for advice on
configuring an operation for access to the git repo.

## Fix

Not applicable

## Related Issues

None
