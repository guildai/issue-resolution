import argparse

p = argparse.ArgumentParser()
p.add_argument("foo")

print(p.parse_args())
