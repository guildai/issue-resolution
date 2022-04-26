import argparse

p = argparse.ArgumentParser()
p.add_argument("--foo", action=argparse.BooleanOptionalAction, default=True)
p.add_argument("--bar", action=argparse.BooleanOptionalAction, default=False)

print(p.parse_args())
