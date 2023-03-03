---
doctest-type: bash
---

# Fix

Requirements:

- guild>0.9.0

    $ guild check -n --version '>0.9.0'

Show the test INI file. Note the dots in the section names.

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

Run the operation without flag values.

    $ guild run test -y
    Resolving config:test.ini

Show the resolved INI file.

    $ guild cat -p test.ini
    [ingredients]
    greens = cabbage
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
    <BLANKLINE>
    [ingredients.meat]
    marbled = true
    type = pork belly

Run the operation with flag values.

    $ guild run test ingredients.carbs.make.water.container=bowl -y
    Resolving config:test.ini

Show the resolved INI file.

    $ guild cat -p test.ini
    [ingredients]
    greens = cabbage
    <BLANKLINE>
    [ingredients.carbs]
    type = noodles
    <BLANKLINE>
    [ingredients.carbs.make]
    <BLANKLINE>
    [ingredients.carbs.make.water]
    add_miso = true
    container = bowl
    temp = 100
    <BLANKLINE>
    [ingredients.meat]
    marbled = true
    type = pork belly