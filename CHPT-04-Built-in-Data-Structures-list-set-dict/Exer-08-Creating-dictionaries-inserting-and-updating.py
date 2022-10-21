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

###

histogram = {}

for customer in source:
    if customer not in histogram:
        histogram[customer] = 0
    histogram[customer] += 1

###

histogram = {}
for customer in source:
    histogram.setdefault(customer, 0)
    histogram[customer] += 1

###

from collections import defaultdict

def summarize_3(source):
    histogram = defaultdict(int)
    for item in source:
        histogram[item] += 1
    return histogram

###

from collections import Counter

def summarize_4(source):
    histogram  = Counter(source)
    return histogram

###

import random
from pprint import pprint

random.seed(1)

histogram = summarize_4(samples(1000, arrival2(8)))
pprint(histogram)

for key in sorted(histogram):
    print(key, histogram[key])