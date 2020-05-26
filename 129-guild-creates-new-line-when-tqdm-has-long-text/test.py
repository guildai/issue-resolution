from tqdm import tqdm
import time


t = tqdm(range(100))
for _ in t:
    t.set_postfix(text='very long string very long string very long string very long string very long string')
    time.sleep(0.1)
