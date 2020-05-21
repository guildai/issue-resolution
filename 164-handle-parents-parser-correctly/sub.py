import argparse

def subparser(parser):
    parser = argparse.ArgumentParser(parents=[parser])
    parser.add_argument('--sub-int', type=int, default=2)
    parser.add_argument('--sub-float', type=float, default=2.2)

    return parser

