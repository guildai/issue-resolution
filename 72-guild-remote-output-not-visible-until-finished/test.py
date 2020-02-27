import sys
import time

steps = 10

for _ in range(steps):
    sys.stdout.write(".")
    sys.stdout.flush()
    time.sleep(0.2)

sys.stdout.write("\n")
