# Name of package in conflict with directory module when building for remote

https://github.com/guildai/guildai/issues/159

## Problem

Guild does not detect a package name conflict and provide instructions
on what to do about it.

## Recreating

Requirements:

- guild<=0.7.0.rc9

## Reproduce Remote Op Error

This example requires a remote config. The following config is used to
create a `localhost` remote over ssh.

```
# ~/.guild/config.yml

remotes:
  localhost:
    type: ssh
    host: localhost
```

Confirm that ssh is configured correctly by running:

    $ ssh localhost true

Resolve any errors before continuing.

To recreate the problem, change to this directory and run:

    $ guild run train -r localhost -y

Incorrect output:

```
Building package
package src: 159-name-of-package-in-conflict-with-directory-module-when-building-for-remote
package dist: /tmp/guild-remote-stage-M6zMg7
running clean
removing 'build/lib.linux-x86_64-2.7' (and everything under it)
'build/bdist.linux-x86_64' does not exist -- can't clean it
'build/scripts-2.7' does not exist -- can't clean it
removing 'build'
running bdist_wheel
running build
running build_py
creating build
creating build/lib.linux-x86_64-2.7
creating build/lib.linux-x86_64-2.7/foo
copying 159-name-of-package-in-conflict-with-directory-module-when-building-for-remote/foo/__init__.py -> build/lib.linux-x86_64-2.7/foo
copying 159-name-of-package-in-conflict-with-directory-module-when-building-for-remote/foo/model.py -> build/lib.linux-x86_64-2.7/foo
error: package directory '159-name-of-package-in-conflict-with-directory-module-when-building-for-remote/foo/foo' does not exist
```

The operation succeeds if `package` in [`guild.yml`](guild.yml) is
changed to a value other than `foo`.

Note that `foo` exists as a local package.

The expected behavior is that Guild detect the name conflict and
provide some guidance as to how to correct the problem.

## Reproduce Package Error

The same error underlying problem be recreated by running `package`:

    $ guild package

Incorrect output:

```
running bdist_wheel
running build
running build_py
error: package directory './foo/foo' does not exist
```

## Workarounds

Rename `package` to a value that does not coincide with a local
package name.

## Fix

This is fixed in 0.7.0.rc10. Guild now detects the name conflict and
instructs the user to change the name in the Guild file.
