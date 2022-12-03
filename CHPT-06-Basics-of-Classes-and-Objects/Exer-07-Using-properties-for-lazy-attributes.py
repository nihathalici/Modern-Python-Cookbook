# Exer-07-Using-properties-for-lazy-attributes

import math
from collections import Counter

Counter({15: 7, 17: 5, 20: 4, 16: 3, 45: 1})

class LazyCounterStatistics:
    def __init__(self, raw_counter:Counter):
        self.raw_counter = raw_counter
    
    @property
    def sum(self):
        return sum(f*v for v, f in self.raw_counter.items())
    
    @property
    def count(self):
        return sum(f for v, f in self.raw_counter.items())
    
    @property
    def mean(self):
        return self.sum / self.count
    
    @property
    def sum2(self):
        return sum(f*v**2 for v, f in self.raw_counter.items())
    
    @property
    def variance(self):
        return (self.sum2 - self.sum**2/self.count) / (self.count - 1)
    
    @property
    def stddev(self):
        return math.sqrt(self.values)
    
    def raw_data(n=8, limit=1000, arrival_function=arrival1):
        expected_time = float(expected(n))
        data = samples(limit, arrival_function(n))
        wait_times = Counter(coupon_collector(n, data))
        return wait_times

###

import random 
#from ch06_r07 import LazyCounterStatistics

random.seed(1)
data = raw_data()
stats = LazyCounterStatistics(data)
print("Mean: {0:.2f}".format(stats.mean))
print("Standard Deviation: {0:.3f}".format(stats.stddev))

###

def __init__(self, raw_counter:Counter):
    self.raw_counter = raw_counter
    self._count = None

@property
def count(self):
    if self._count is None:
        self._count = sum(f for v, f in self.raw_counter.items())
    return self._count
