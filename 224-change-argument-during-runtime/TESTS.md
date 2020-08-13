# Tests

## dynamic_flag_gapi.py

    >>> run("guild run dynamic_flag_gapi.py -y")
    <exit 0>

    >>> run("guild runs info")
    id: ...
    operation: dynamic_flag_gapi.py
    ...
    flags:
      x: 1
      y: 2
    ...
    <exit 0>

## dynamic_flag_yaml.py

    >>> run("guild run dynamic_flag_yaml.py x=2 -y")
    <exit 0>

    >>> run("guild runs info")
    id: ...
    operation: dynamic_flag_yaml.py
    ...
    flags:
      x: 2
      y: 3
    ...
    <exit 0>
