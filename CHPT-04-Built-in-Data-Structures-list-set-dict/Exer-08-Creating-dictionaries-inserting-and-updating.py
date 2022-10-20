# Exer-08-Creating-dictionaries-inserting-and-updating

def arrival2(n=8):
    p = 0
    while True:
        step = random.choice([-1, 0, +1])
        p += step
        yield abs(p) % n

import random
from ch04_r06 import samples, arrival2
random.seed(1)
list(samples(10, arrival2(8)))