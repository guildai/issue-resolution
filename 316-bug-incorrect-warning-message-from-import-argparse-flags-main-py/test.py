import argparse

p = argparse.ArgumentParser()
p.add_argument("--foo", action="store_true")
print(p.parse_args())
