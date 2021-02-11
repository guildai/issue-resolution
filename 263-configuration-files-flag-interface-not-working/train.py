import argparse
import sys


def main(args):
    print(f"x={args.x}")


if __name__ == "__main__":
    print("args: %s" % sys.argv[1:])

    parser = argparse.ArgumentParser()

    parser.add_argument("--x", type=int, default=1)

    args = parser.parse_args()
    main(args)
