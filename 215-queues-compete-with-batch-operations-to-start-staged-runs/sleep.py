import os
import time

id = None
seconds = 1.0

id = id or os.getenv("RUN_ID")
desc = "%s " % id if id else ""

print("%ssleeping for %0.1f second(s)" % (desc, seconds))
time.sleep(seconds)
