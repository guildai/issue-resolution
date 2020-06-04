import argparse

p = argparse.ArgumentParser()
p.add_argument("--list-as-str", default="[4,5,6]")

args = p.parse_args()

print(type(args.list_as_str), args.list_as_str)
