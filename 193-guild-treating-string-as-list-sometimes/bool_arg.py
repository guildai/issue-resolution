# bool_arg.py
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--b', default=False, type=bool)

print(parser.parse_args())
