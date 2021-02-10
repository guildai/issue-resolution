import os
import time

run_id = os.getenv("RUN_ID", "<unset>")


def f(id, seconds):
    print("Starting %s in %s" % (id, run_id))
    time.sleep(seconds)
    print("Ending %s %s" % (id, run_id))
