import os
import sys

if len(sys.argv) != 2:
    raise SystemExit("usage: %s LOGDIR" % sys.argv[0])

logdir = sys.argv[1]

import tensorflow as tf

if not os.path.exists(logdir):
    os.makedirs(logdir)

with tf.summary.create_file_writer(logdir).as_default():
    tf.summary.scalar("hello", data=1.123, step=0)
