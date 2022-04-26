import argparse

p = argparse.ArgumentParser()
p.add_argument("--foo", action=argparse.BooleanOptionalAction, default=True)
p.add_argument("--bar", action=argparse.BooleanOptionalAction, default=False)

args = p.parse_args()

print(f"bar={args.bar} foo={args.foo}")
