import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--some_flag', type=str, default='')
args = parser.parse_args()
print(args.some_flag)
