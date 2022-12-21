# Managing global and singleton objects

"""
for row in source:
    count('input')
    some_processing()
print(counts())
"""

# counter.py

from collections import Counter

_global_counter = Counter()

def count(key, increment=1):
    _global_counter[key] += increment
def counts():
    return _global_counter.most_common()

d = Dice1(1)
for _ in range(1000):
    if sum(d.roll()) == 7: count('seven')
    else: count('other')
print(counts())

###

# counter.py
from collections import Counter

_global_counter = Counter()

def count(key, increment=1):
    _global_counter[key] += increment
def counts():
    return _global_counter.most_common()

###

from ch07_r04 import count, counts
from ch07_r03 import Dice1

d = Dice1(1)

for _ in range(1000):
    if sum(d.roll()) == 7: count('seven')
    else: count('other')
print(counts())

###

from collections import Counter

class EventCounter:
    _counts = Counter()
    
    def count(self, key, increment=1):
        EventCounter._counts[key] += increment
    def counts(self):
        return EventCounter._counts.most_common()

###

from ch07_r04 import EventCounter

c1 = EventCounter()
c1.count('input')
c2 = EventCounter()
c2.count('input')
c3 = EventCounter()
c3.counts()
