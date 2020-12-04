# Guild operation main in subdirectory not working on remote

https://github.com/guildai/guildai/issues/246

## Problem

On the face, Guild is not running a package module as
expected. However, with a modified config, the operation can be run as
expected.

## Recreating

Requirements:

- guild<=0.7.0

### Example 1 - No Package in Main Spec

To recreate the issue problem, run `prepare-1`. This operation uses
the main spec `<pkg>/<module>` --- i.e. uses a slash to delimit the
package and module. This notation however means something else in
Guild. The slash denotes a "path to the Python code" rather a package
path. While this works, it runs the code outside of the intended
`operations` package. As a result, relative imports fail.

```
$ guild run prepare-1 -y
Traceback (most recent call last):
  File ".guild/sourcecode/operations/prepare.py", line 4, in <module>
    from . import road_segmentation
ValueError: Attempted relative import in non-package
```

While a possible workaround is to use absolute imports, this should be
considered an anti-pattern.


```
$ guild run prepare-1 relative_import=no -y
hello
```

### Example 2 - Main Spec with Package

`prepare-2` is a modified version that uses the main spec
`<pkg>.<module>` --- i.e. uses a dot delimiter. This specifies the
full module including the package. With this spec, the operation
succeeds.

```
$ guild run prepare-2 -y
hello
```

Note that the `operations` directory must contain `__init__.py` to be
recognized as a Python package.

## Fix

The behavior is by design - nothing to fix.
