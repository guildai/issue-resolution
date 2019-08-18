# Extremely long operation names when viewing from different machine

https://github.com/guildai/guildai/issues/34

## Problem summary

The OP is describing two problems:

- Runs can be orphaned from their operations, which occurs any time a
  run is moved to a different machine or when a run's associated
  operation definition (e.g. a project) is deleted.

- Operation descriptions can become very long.

We address the second of these two problems here.

When viewing operations, Guild operation names can be very long such
that the operation name causes other attributes to be truncated or not
visible.

Here's an example of `guild runs` output from the issue:

```
[23:3daaad98]  dqn:train
[24:d61e2fa6]  dqn:train
[25:7bf8346e]  .../andrew/Documents/PhD/symbolic-goal-generation/ikostrikov:trai
[26:7bf83220]  .../andrew/Documents/PhD/symbolic-goal-generation/ikostrikov:trai
[27:7bd80658]  .../andrew/Documents/PhD/symbolic-goal-generation/ikostrikov:trai
```

Guild should use fewer characters to display operation names in such
cases. Ideally, Guild operations communicate just the information
needed to identify them and no more.

## Background

Guild runs are associated with operations. An associated operation is
defined in the run's *opref*, which is s file located in
`RUN_DIR/.guild/opref`. Opefs include information such as the type of
reference, the package name and version, the model name, and finally
the operation name.

Opref types include packages, Guild files, and scripts.

Guild renders operation descriptions differently for each opref type.

- Packages: `PACKAGE_NAME '/' [ MODEL_NAME ':' ] OPERATION_NAME`
- Guild files: `[ PROJECT_PATH '/' ] [ MODEL_NAME ':' ] OPERATION_NAME`
- Scripts: `[ PROJECT_PATH '/' ] SCRIPT_PATH `

The problem arises in Guild's rendering of `PROJECT_PATH` - which is a
string that identifies the operation project. If the operation is
defined in the current project (current directory or directory
specified using `-C` option) `PATH` and its trailing `/` are omitted
altogether. As of Guild 0.6.5, if the project is not current, Guild
uses the following logic to render the operation description:

- If the project relative path (relative to the current directory)
  contains more than one sequence of leading `../`, the whole sequence
  is replaced with `.../`

- Leading `./` characters are dropped

As Guild does not truncate these paths, any long relative path appears
in the operation description.

Examples of script types:

| Script Relative Path      | Operation Description |
| --------------------      | --------------------- |
| `./train.py`              | `train.py`            |
| `./a/train.py`            | `a/train.py`          |
| `../train.py`             | `../train.py`         |
| `../a/train.py`           | `../a/train.py`       |
| `../../a/train.py`        | `.../a/train.py`      |
| `../../../a/b/c/train.py` | `.../a/b/c/train.py`  |

## Approaches

The 0.6.5 scheme lets too much information about an operation project
location leak into the operation description. We want to show the
highest possible signal so users can identify each operation.

We consider various approaches below.

### Drop `PROJECT_PATH`

We could omit `PROJECT_PATH` altogether:

| Script Relative Path      | Operation Description |
| --------------------      | --------------------- |
| `./train.py`              | `train.py`            |
| `./a/train.py`            | `train.py`            |
| `../train.py`             | `train.py`            |
| `../b/train.py`           | `train.py`            |
| `../../a/train.py`        | `train.py`            |
| `../../../b/a/c/train.py` | `train.py`            |

This is obviously a problem as each run appears to be of the same
operation. While it's clear the operation is `train.py`, there's no
information about what is being trained.

### Include `PROJECT_PATH` as needed but shorten

| Script Path          | Run From | Op Spec       | Displayed From | Op Desc          |
| -------------------- | -------- | -------       | -------------- | -------          |
| `/train.py`          | `/`      | `train.py`    | `/`            | `train.py`       |
| `/train.py`          | `/`      | `train.py`    | `/a`           | `train.py (/)`   |
| `/train.py`          | `/`      | `train.py`    | `/a/b`         | `train.py (/)`   |
| `/train.py`          | `/a/b`   | `train.py`    | `/a/b`         | `train.py (/)`   |
| `/a/train.py`        | `/a`     | `train.py`    | `/a`           | `train.py`       |
| `/a/train.py`        | `/a`     | `train.py`    | `/a/b`         | `train.py (/a)`  |
| `/a/train.py`        | `/a`     | `train.py`    | `/a/b/c`       | `train.py (/a)`  |
| `/a/train.py`        | `/`      | `a/train.py`  | `/`            | `a/train.py`     |
| `/a/train.py`        | `/`      | `a/train.py`  | `/a`           | `a/train.py (/)` |
| `/a/train.py`        | `/`      | `/a/train.py` | `/`            | `train.py (a)`   |
| `/a/train.py`        | `/`      | `/a/train.py` | `/a`           | `train.py`       |
| `/a/b/train.py`      | `/a/b`   | `train.py`    | `/a/b`         | `train.py`       |
| `/a/b/train.py`      | `/a/b`   | `train.py`    | `/a`           | `train.py (b)`   |
| `/a/b/train.py`      | `/a/b`   | `train.py`    | `/`            | `train.py (a/b)` |

Note the rules:

1. Op spec is preserved as specified, unless it is an absolute path,
   in which case it is assumed to refer to the basename of the
   referenced script.

2. The project location is assumed to be the current directory, unless
   the operation is an absolute path, in which case it is assumed to
   be the parent directory of the referenced script.

3. Operations are always shown using their *names* (from rule 1).

4. If the current directory is the same as the project location (from
   rule 2) the operation is shown as-is without qualification.

5. If the current directory is different from the project location
   (from rule 2) the operation name (from rule 1) is shown with a
   location qualifier. If the project location is a subpath of the
   current directory, the location is shown are a relative path. If
   the the project location is outside the current directory, it is
   shown as an absolute path.

6. Qualifiers that are too long (i.e. are longer than some fixed
   number of characters), they are shortened to remove path segments,
   replaced b `/.../` up to the point their length is under the set
   limit.

## Implementation

The new scheme for showing operations is implemented in 0.6.6.

Refer to
[guild/tests/op-desc.md](https://github.com/guildai/guildai/blob/master/guild/tests/op-desc.md)
for test coverage with examples.

## Related topics

- [Operations Description tests](https://github.com/guildai/guildai/blob/master/guild/tests/op-desc.md)
- [Shorten dirs tests](https://github.com/guildai/guildai/blob/master/guild/tests/utils.md#shorten-dirs)
