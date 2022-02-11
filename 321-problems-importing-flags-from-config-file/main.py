from logging import warn
import sys
from argparse import ArgumentParser, Namespace
from os.path import isfile
import yaml


def load_cli_args(args_options_path: str = "options.yml"):
    """
    Modify command line args if desired, or load from YAML file.
    """
    if len(sys.argv) <= 3:
        if isfile(args_options_path):  # if file exists
            with open(args_options_path, "r") as f:
                res = yaml.safe_load(f)
            sys.argv = [sys.argv[0]]
            for k, v in res.items():
                sys.argv += [f"--{k}", str(v)]


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
    load_cli_args()
    args = init_cli_args()
    if args.verbose:
        print(args)


def init_cli_args() -> Namespace:
    p = ArgumentParser()
    #### GENERAL ####
    p.add_argument(
        "--seed",
        type=int,
        default=42,
        help="seed for randomization",
    )
    p.add_argument(
        "--verbose",
        type=str2bool,
        default=True,
        help="print information to shell",
    )
    p.add_argument(
        "--some-flag",
        type=str,
    )

    # return p.parse_args()
    # Ignore unrecognized args
    return p.parse_known_args()[0]


if __name__ == "__main__":
    main()
