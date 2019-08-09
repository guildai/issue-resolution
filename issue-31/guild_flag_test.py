import argparse

parser = argparse.ArgumentParser(description="RL")
parser.add_argument("--import", default="test_file", help="import file")
parser.add_argument("--port", default="sydney", help="port of origin")
parser.add_argument("--not-imported", default="a2c", help="for demonstration")

parser.parse_args()
