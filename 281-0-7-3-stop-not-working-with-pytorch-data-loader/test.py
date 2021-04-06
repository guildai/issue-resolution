import multiprocessing as mp
import os

import mod

count = 5
sleep = 99.0

print("Main process %i" % os.getpid())

ps = [mp.Process(target=mod.f, args=[sleep]) for _ in range(count)]
for p in ps:
    p.start()
for p in ps:
    p.join()
