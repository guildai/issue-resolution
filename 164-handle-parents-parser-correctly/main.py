import argparse
from sub import subparser

def main(args):
    print(args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--main-int', type=int, default=1)
    parser.add_argument('--main-float', type=float, default=1.2)

    parser = subparser(parser)

    main(parser.parse_args())


