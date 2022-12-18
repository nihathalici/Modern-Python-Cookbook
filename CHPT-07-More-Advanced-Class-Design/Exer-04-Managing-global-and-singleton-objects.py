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
