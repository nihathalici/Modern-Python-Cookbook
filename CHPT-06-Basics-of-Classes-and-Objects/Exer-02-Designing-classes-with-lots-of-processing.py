# Exer-02-Designing-classes-with-lots-of-processing

# Counter({15: 7, 17: 5, 20: 4, 16: 3, ... etc., 45: 1})

import math

class CounterStatistics:
    
    def __init__(self, raw_counter: Counter):
        self.raw_counter = raw_counter
        self.mean = self.compute_mean()
        self.stddev = self.compute_stddev()
    
    def compute_mean(self):
        total, count = 0, 0
        for value, frequency in self.raw_counter.items():
            total += value*frequency
            count += frequency
        return total/count
    
    def compute_stddev(self):
        total, count = 0, 0
        for value, frequency in self.raw_counter.items():
            total += frequency*(value-self.mean)**2
            count += frequency
        return math.sqrt(total/(count-1))

from ch04_r06 import *

from collections import Counter

def raw_data(n=8, limit=1000, arrival_function=arrival1):
    expected_time = float(expected(n))
    data = samples(limit, arrival_function(n))
    wait_times = Counter(coupon_collector(n, data))
    return wait_times

###

import random 

from ch06_r02 import CounterStatistics
random.seed(1)

data = raw_data()
stats = CounterStatistics(data)
print("Mean: {0:.2f}".format(stats.mean))
print("Standard Deviation: {0:.3f}".format(stats.stddev))

###

def add(self, value):
    self.raw_counter[value] += 1
    self.mean = self.compute_mean()
    self.stddev = self.compute_stddev()

def __init__(self, counter:Counter=None):
    if counter:
        self.raw_counter = counter
        self.count = sum(self.raw_counter[k] for k in self.raw_counter)
        self.sum = sum(self.raw_counter[k]*k for k in self.raw_counter)
        self.sum2 = sum(self.raw_counter[k]*k**2 for k in self.raw_counter)
        self.mean = self.sum/self.count
        self.stddev = math.sqrt((self.sum2 - self.sum**2/self.count) / (self.count - 1))
    else:
        self.raw_counter = Counter()
        self.count = 0
        self.sum = 0
        self.sum2 = 0
        self.mean = None
        self.stddev = None

###

def add(self, value):
    self.raw_counter[value] += 1
    self.count += 1
    self.sum += value
    self.sum += value**2
    self.mean = self.sum/self.count
    if self.count > 1:
        self.stddev = math.sqrt(
            (self.sum2 - self.sum**2 / self.count)/(self.count-1))

