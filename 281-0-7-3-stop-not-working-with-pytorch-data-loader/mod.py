import os
import time


def f(sleep):
    print("Starting %i" % os.getpid())
    time.sleep(sleep)
