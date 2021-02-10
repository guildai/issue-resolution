from multiprocessing import Pool
import os

import mod

seconds = 30
workers = 3
calls = 3


if __name__ == "__main__":
    with Pool(workers) as p:
        p.starmap(mod.f, [[id, seconds] for id in range(calls)])
