import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--replay-buffer-size", type=int, default="10000")

args = parser.parse_args()
print("replay-buffer-size: %r" % args.replay_buffer_size)
