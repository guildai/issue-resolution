import sys
import time

use_tqdm = False
steps = 10

def progress(iter):
    if use_tqdm:
        import tqdm
        return tqdm.tqdm(iter)
    def dots():
        for x in iter:
            yield x
            sys.stdout.write(".")
            sys.stdout.flush()
        sys.stdout.write("\n")
    return dots()

for _ in progress(range(steps)):
    time.sleep(0.2)
