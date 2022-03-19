---
doctest-type: bash
---

# Issue with defining source code in guild.yml

https://my.guild.ai/t/issue-with-defining-source-code-in-guild-yml/833

## Problem

Question about exluding certain files from Guild source code.

The issue is with the YAML spec. Guild is ignoring a `sourcecode`
config that it doesn't recognize. Guild should be complaining about
something.

## Recreating

Working version (test):

    $ guild run test -y
    Hi

    $ guild run test --test-sourcecode
    Copying from the current directory
    Rules:
      exclude dir '__pycache__'
      exclude dir '.*'
      exclude dir '*' with '.guild-nocopy'
      exclude dir '*' with 'bin/activate'
      exclude dir '*' with 'Scripts/activate'
      exclude dir 'build'
      exclude dir '*.egg-info'
      include text '*' size < 1048577, max match 100
      exclude '*.json'
    Selected for copy:
      ./README.md
      ./guild.yml
      ./test.py
    Skipped:
      ./a.json
      ./b.json

    $ guild ls -n --sourcecode
    README.md
    guild.yml
    test.py

Broken version:

    $ guild run test-broken -y
    Hi

    $ guild run test-broken --test-sourcecode
    Copying from the current directory
    Rules:
      exclude dir '__pycache__'
      exclude dir '.*'
      exclude dir '*' with '.guild-nocopy'
      exclude dir '*' with 'bin/activate'
      exclude dir '*' with 'Scripts/activate'
      exclude dir 'build'
      exclude dir '*.egg-info'
      include text '*' size < 1048577, max match 100
    Selected for copy:
      ./README.md
      ./a.json
      ./b.json
      ./guild.yml
      ./test.py
    Skipped:

    $ guild ls -n --sourcecode
    README.md
    a.json
    b.json
    guild.yml
    test.py
