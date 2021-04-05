import multiprocessing as mp

import mod

count = 5
sleep = 5.0

ps = [mp.Process(target=mod.f, args=[sleep]) for _ in range(count)]
for p in ps:
    p.start()
for p in ps:
    p.join()
