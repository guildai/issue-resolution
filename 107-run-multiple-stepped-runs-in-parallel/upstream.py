import os
import time

sleep = 0

print("Upstream (sleep %i)" % sleep)

time.sleep(sleep)
open("upstream", "w").write(os.getenv("RUN_ID") or "")
