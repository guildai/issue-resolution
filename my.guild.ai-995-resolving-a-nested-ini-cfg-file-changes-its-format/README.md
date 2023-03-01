---
doctest-type: bash
---

# Resolving a nested ini/cfg file changes its format

https://my.guild.ai/t/resolving-a-nested-ini-cfg-file-changes-its-format/995

## Problem

Guild has a particularly destructive save-with-new-values behavior for
INI file formats.

## Recreating

Requirements:

- guild<0.9

    $ guild check -n --version '<=0.9'

The `test` operation uses `test.ini` for flags.

    $ guild run test --help-op
    Usage: guild run [OPTIONS] test [FLAG]...
    <BLANKLINE>
    Use 'guild run --help' for a list of options.
    <BLANKLINE>
    Flags:
      ingredients.carbs.make.water.add_miso
                                      (default is yes)
      ingredients.carbs.make.water.container
                                      (default is 'cooking pot')
      ingredients.carbs.make.water.temp
                                      (default is 100)
      ingredients.carbs.type          (default is noodles)
      ingredients.greens              (default is cabbage)
      ingredients.meat.marbled        (default is yes)
      ingredients.meat.type           (default is 'pork belly')

    $ cat test.ini
    [ingredients]
    greens = cabbage
    <BLANKLINE>
    [ingredients.meat]
    type = pork belly
    marbled = true
    <BLANKLINE>
    [ingredients.carbs]
    type = noodles
    <BLANKLINE>
    [ingredients.carbs.make]
    <BLANKLINE>
    [ingredients.carbs.make.water]
    add_miso = true
    container = cooking pot
    temp = 100

When Guild saves the generated INI file, it applies a new format. It
does not preserve the section names as originally provided in
`test.ini`.

    $ guild run test -y
    Resolving config:test.ini

    $ guild cat -p test.ini
    [ingredients]
    carbs = {'make': {'water': {'add_miso': True, 'container': 'cooking pot', 'temp': 100}}, 'type': 'noodles'}
    greens = cabbage
    meat = {'marbled': True, 'type': 'pork belly'}

## Workarounds

None currently.

## Fix

Apply the suggested (helpful!) patch here:
https://my.guild.ai/t/resolving-a-nested-ini-cfg-file-changes-its-format/995/2?u=garrett

## Related Issues

None
