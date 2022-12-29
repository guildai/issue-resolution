---
doctest-type: bash
---

# Issues running R tests from RStudio IDE

https://github.com/guildai/guildai/issues/466

## Problem

If user:
- has guildai installed as a standalone app,
- has a shell with an activated venv in which guildai is not installed, and
- attempts to launch a guild batch run of a non-python operation, then

user encounters an error about missing 'click' module.

The `BatchModelProxy` class returns an operation with an
`exec` string that contains `"{python_exe}"`, which resolves
to a path to the python executable of the "wrong" python.
The proposed [patch in pr 467](https://github.com/guildai/guildai/pull/467)
changes how `{python_exe}` resolves. Alternatively, a narrower
fix can also be applied by modifying `BatchModelProxy` to return an exec string that
invokes `sys.executable` directly.

## Recreating

Starting from the issue working directory
(issue-resolution/466-issues-running-r-tests-from-rstudio-ide)
And assuming docker is installed and available:

```bash
docker build -t guild-issue-466 .
```

Expected output

```verbatim
... <ommitted verbose install output from Steps 1-12>

Step 13/13 : RUN /bin/bash -c "source user-project-venv/bin/activate &&   /opt/guild-app/bin/guild run -y user-op x=[2,3]"
 ---> Running in bcecc2d3a894
WARNING: Found more than 100 source code files but will only copy 100 as a safety measure. To control which files are copied, define 'sourcecode' for the operation in a Guild file.
Traceback (most recent call last):
  File "/usr/lib/python3.8/runpy.py", line 194, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/usr/lib/python3.8/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/guildai/guild/batch_main.py", line 15, in <module>
    from guild import batch_util
  File "/guildai/guild/batch_util.py", line 26, in <module>
    from guild import cli
  File "/guildai/guild/cli.py", line 22, in <module>
    import click
ModuleNotFoundError: No module named 'click'
The command '/bin/sh -c /bin/bash -c "source user-project-venv/bin/activate &&   /opt/guild-app/bin/guild run -y user-op x=[2,3]"' returned a non-zero code: 1
```
