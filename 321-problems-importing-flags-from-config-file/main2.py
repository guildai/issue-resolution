from logging import warn
import sys
from argparse import ArgumentParser, Namespace
from os.path import isfile
import yaml


def str2bool(str_value: str, default: bool = False):
    """Convert argparse boolean to true boolean.
    Ref: https://stackoverflow.com/a/43357954/1888794"""
    if isinstance(str_value, bool):
        return str_value
    if str_value.lower() in ("yes", "true", "t", "y", "1"):
        return True
    elif str_value.lower() in ("no", "false", "f", "n", "0"):
        return False
    else:
        warn(
            f"Boolean value expected. Passed {str_value}, which is of type {type(str_value)} and wasn't recognized. Using default value {default}.",
        )
        return default


def main():
    args = init_cli_args()
    print(args)


def init_cli_args() -> Namespace:
    p = ArgumentParser()
    options = yaml.safe_load(open("options.yml"))
    for name, val in options.items():
        assert not isinstance(val, (list, dict)), val
        p.add_argument(f"--{name}", type=arg_type_for_val(val), default=val)
    return p.parse_args()


def arg_type_for_val(val):
    if isinstance(val, bool):
        return str2bool
    return type(val)


if __name__ == "__main__":
    main()
