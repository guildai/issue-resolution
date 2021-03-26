import argparse

parser = argparse.ArgumentParser()
group = parser.add_argument_group("data")
group.add_argument("--src", default="")

print(parser.parse_args())
