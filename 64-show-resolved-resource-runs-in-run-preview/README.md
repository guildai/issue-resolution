# Show resolved resource runs in run preview

https://github.com/guildai/guildai/issues/64

## Problem

Guild lazily resolves required operations. This is *painful*. It means
that a user can't know ahead of time which run Guild will select. In
practice, you have to *watch the run output for a run ID* and then, as
the run proceeds, confirm that it's the expected/desired resource.

Guild should resolve this up front and include any resolved run ID in
the preview.

## Recreating

```
$ guild run upstream -y

$ guild run downstream
You are about to run downstream
Continue? (Y/n)
Resolving operation:upstream dependency
Using output from run ... for operation:upstream resource
```

Guild doesn't show the resolved run ID (`...` above) until *after*
downstream starts.

## Workarounds

Specify the upstream run ID explicitly.

    $ guild run downstream upstream=...

## Fix

Pending
