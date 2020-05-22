import sys
import time

from tqdm import tqdm

steps = 10
out = None
wait = 0.01


def _tqdm(iterable):
    if out is None:
        return tqdm(iterable, file=None)
    elif out == "stdout":
        return tqdm(iterable, file=sys.stdout)
    elif out == "stderr":
        return tqdm(iterable, file=sys.stderr)
    elif out == "default":
        return tqdm(iterable)
    else:
        return tqdm(iterable, file=open(out, "w"))


for i in _tqdm(range(steps)):
    tqdm.write(str(i))
    if wait:
        time.sleep(wait)
