import numpy as np
import tensorflow as tf

writer = tf.summary.create_file_writer("log")
with writer.as_default():
    tf.summary.scalar("Name", np.inf ,step=0)
    writer.flush()
