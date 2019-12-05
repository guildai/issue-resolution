# Feature selection with Guild?

https://github.com/guildai/guildai/issues/93

## Problem

Guild does not provide an (obvious or simple) way to select
features. Something like this:

```
$ guild run train features=[f1,f2,f3]
```

Guild treats this syntax as a signal to run three separate trials: one
for each specified feature.

If a module defines a global variable as a list, Guild will not import
that variable as a flag.

## Recreating

To see how a naive approach doesn't work, refer to
[guild.yml](guild.yml) `naive` operation.

Running the operation:

```
$ guild run naive features=[f1,f2,3]
guild: unsupported flag 'features'
```

## Workarounds

### Option 1 - Integer Bitmap

Features can be implemented using a bitmap over an integer.

Refer to [guild.yml](guild.yml) `bitmap` operation and the
implementation in [bitmap.py](bitmap.py).

To enable features, specify an integer value for the `features`
flag. Each bit in the value enables a feature.

The following will run a trial for each permutation of the three
supported features (3 bits):

```
$ guild run bitmap features=[0,1,2,3,4,5,6,7]
```

The obvious problem with this approach is that a numeric value
provides no intuition about the enabled features.

One could use a label for individual trials:

```
$ guild run bitmap features=5 -l "features=f1,f3"
```

The advantage of this approach is that it works with random and
sequential optimizers.

For random search:

```
$ guild run bitmap features=[0:7]
```

For Bayesian optimization:

```
$ guild run bitmap features=[0:7] -o gp
```

### Option 2 - Encoded List

A second approach is to convey the list of features using an encoded
list.

Refer to [guild.yml](guild.yml) `encoded` operation and the
[encoded.py](encoded.py) implementation for details.

To run an operation, specify one of the available permutations. E.g.

```
$ guild run encoded features=f1,f3
```

The list of permutations can be viewed using ``guild help`` or ``guild
run encoded --help-op``.

## Approaches

Guild does not support list values for single flags. Guild has held
that any values other than strings, numbers, and booleans must be
encoded by the user. Furthermore, Guild uses list syntax to imply
trial values. List syntax cannot therefore be used to convey list
values without potentially confusing a user.

For example, consider an operation that supports flag having both the
historical list-as-trial-values and list-as-value meaning. Without
knowledge of the operation and this nuanced distinction, the following
command is ambiguous:

```
$ guild run features=[f1,f2,f3] learning-rate=[0.01,0.1]
```

In practice, this may not be confusing as the meaning of a list could
be obvious based on the flag. In the above example, the plural
"features" signals that the value is provided as a list.

An alternative list syntax is challenging in shell environments as
many possible list start and end tokens have meaning for shell
commands (e.g. `(..)`, `{..}`, etc.)

Quoting lists is difficult and error prone.

Omitting start and end tokens is a possibility:

```
$ guild run features=f1,f2,f3 learning-rate=[0.01,0.1]
```

This is arguably also confusing. Why the different syntax? Is the
first case a list?

Using a common list syntax at least resolves the question "what type
of flag argument is this?" How that argument type is interpreted by
Guild is a matter of the flag type.

### Approach 1 - Support `list` flag type

- New `list` value for flag `type` attribute
- Conveys value as a list value when using globals interface
- Conveys value as repeating command line option
- Optimizers could use this information to generate permutations

Guild ought to also support a syntax to say "expand to all possible
values". This syntax might also be used for grid search, which is
currently something lacking in Guild.

Possible syntax for a list value:

- `$ guild run features=[f1,f3,f2]`
- `$ guild run features=f1,f3,f2`

Possible syntax for a list with items containing spaces:

- `$ guild run features=[f1,f2 with spaces,f3]`
- `$ guild run features=f1,'f2 with spaces',f3`

Possible syntax for "list of all values":

- `$ guild run features=[..]`
- `$ guild run features=..`

Possible syntax for "list of all permutations":

- `$ guild run features=[...]`
- `$ guild run features=...`
- `$ guild run features=[..!]`
- `$ guild run features=..!`

Regarding expansion syntax, the use of `..` could extend to integer
types when generating trials over a sequential range:

- `$ guild run bitmap=[0..7]`

## Related Issues

None at this time.
