# Exer-06-Extending-a-collection-a-list-that-does-statistics

import math

class StatsList(list):
    
    def sum(self):
        return sum(v for v in self)
    
    def count(self):
        return sum(1 for v in self)
    
    def mean(self):
        return self.sum() /self.count()
    
    def sum2(self):
        return sum(v**2 for v in self)
    
    def variance(self):
        return (self.sum2() -
        self.sum()**2/self.count()) / (self.count() - 1)
    
    def stddev(self):
        return math.sqrt(self.variance())


subset1 = StatsList([10, 8, 13, 9, 11])
data = StatsList([14, 6, 4, 12, 7, 5]) 
data.extend(subset1)   
print(data)
print(data.mean())
print(data.variance())
data.sort()
print(data[len(data)//2])

###

from collections.abc import Mapping
class MyFancyMapping(Mapping):
    pass
