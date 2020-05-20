import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--load-model", type=str, default="model")

print(parser.parse_args())
