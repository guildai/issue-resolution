import argparse
import os

p = argparse.ArgumentParser()
p.add_argument("--resource", required=True)

args = p.parse_args()

if not os.path.exists(args.resource):
    raise FileNotFoundError(args.resource)

print("Success!")
