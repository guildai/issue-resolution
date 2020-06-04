# Support snapshotting of non-project libraries

https://github.com/guildai/guildai/issues/195

## Problem

Guild's support for code snapshotting only applies to project level
files. It would be handle to copy required libraries.

## Recreating

Requirements:

- guild<=0.7.0
- Python 3

## Workarounds

See [test.py](test.py) for an example of snapshotting a Python module
or package before importing it.

To run the workaround, change to this directory and run:

    $ PYTHONPATH=$(realpath .) guild run test.py -y
    shared module loaded from <run dir>/.guild/sourcecode/shared/__init__.pyc
    hello

List the source code files for the run:

    $ guild run ls --sourcecode

Note that `shared` is located with the run.

This operation requires `PYTHONPATH` to be set externally. Try running
`test.py` without setting `PYTHONPATH`:

    $ guild run test.py -y
    Traceback (most recent call last):
    ...
    ImportError: No module named shared

List the source code files for the failed run:

    $ guild run ls --sourcecode

Note that `shared` is NOT located with the run.

The `shared` library source is located in the project directory but
contains the marker `.guild-nocopy`, which prevents it from being
copied as source code. This simulates the case where a required
library is available on the system but it not available to the
project.

Setting `PYTHONPATH` makes `shared` available to the script.

`test.py` does not import `shared` outright. It checks if it's running
under Guild (reads `GUILD_SOURCECODE` environment variable) and uses
the `imp` module to find the location of `shared`. Then it copies that
directory to the Guild source code directory.

When `shared` is imported, it is imported from the Guild source code
location.

This scheme effectively lets you dynamically control Guild source code
via the `PYTHONPATH` environment variable. While the code snippet in
`test.py` is not ideal, it's not a lot of code either.

## Fix

There are a couple approaches that we consider here.

### Extend source code snappshotting

Possible spelling of "copy the `shared` package as sourcecode":

```
test:
  sourcecode:
    - include: $(find shared $PYTHONPATH)

```

Other spellings of the the `include` for `shared`:

Alt 'macro' names:

    $(package shared)

This syntax resembles Make and bash functions. This seems the obvious
syntax but would require a new facility in Guild that I would hope
could generalize to labels and flag defaults. Getting fancy.

Guild var 'template' syntax:

    ${'shared'|find-package}

The template syntax is consistent with that used for labels. It also
suggests that flag can be used to resolve sourcecode specs. This
approach has the advantage of being consistent with existing function
application support.

The other spelling of course is to just extend the `sourcecode` spec
to support `package` and `module` attributes (following the pattern of
`dir`).

```
test:
  sourcecode:
    - include:
        package: shared
```

### Extend (fix?) module dependency

The current `module` dependency is a weak construct in Guild. It is
resolved by merely attempting to import the specified modules. This is
only slightly useful in that it can prevent a potential import error
after a run starts (potentially saving a lot of time, e.g. if the
missing module is only imported after a long-running training
operation). It also can be used to print a user-friendly message to
resovle the issue.

We might consider beefing up this dependency and copying the module
code to the run directory. This might be to the source code
destination by default. A user can change the destination by
specifying an alternative `target-path` for the resource source.

```
op:
  requires:
   - module: shared
     target-path: .guild/sourcecode  # default for module
     target-type: copy               # default post 0.7.0
```

The `target-type` could be used here to copy or link as needed.

We might extend `target-type` in this case to the value
`verify-source` (or similar) to not link or copy but just verify the
source.
