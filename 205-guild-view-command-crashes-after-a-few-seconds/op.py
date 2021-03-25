import sys
import time

seconds = 5

_stop_at = time.time() + seconds

while time.time() < _stop_at:
    sys.stdout.write("X")
    sys.stdout.flush()
