# Exer-08-Creating-a-partial-function


def prod(iterable):
    return reduce(operator.mul, iterable), 1


def standardize(mean, stdev, x):
    return (x - mean) / stdev


text_parse = lambda text: (r.split() for r in text.splitlines())

###

from types import SimpleNamespace

row_build = lambda rows: (SimpleNamespace(x=float(x), y=float(y)) for x, y in rows)

###

import statistics

mean_x = statistics.mean(item.x for item in data_1)
stdev_x = statistics.stdev(item.x for item in data_1)

for row in data_1:
    z_x = standardize(mean_x, stdev_x, row.x)
    print(row, z_x)

for row in data_2:
    z_x = standardize(mean_x, stdev_x, row.x)
    print(row, z_x)

###

from functools import partial

z = partial(standardize, mean_x, stdev_x)

lambda x: standardize(mean_v1, stdev_v1, x)

z = lambda x: standardize(mean_v1, stdev_v1, x)

###

for row in data_1:
    print(row, z(row.x))

for row in data_2:
    print(row, z(row.x))

###

for row in data_1:
    row.z = z(row.v1)

for row in data_2:
    row.z = z(row.v1)

###

z = lambda x, m=mean_v1, s=stdev_v1: standardize(m, s, x)

###

def reduce(function, iterable, initializer=None)

prod = partial(reduce(mul, initializer=1))

###

from operator import mul
from functools import reduce

prod = lambda x: reduce(mul, x, 1)

###

factorial = lambda x: prod(range(2, x+1))
factorial(5)

###

def prepare_z(data):
    mean_x = statistics.mean(item.x for item in data_1)
    stdev_x = statistics.stdev(item.x for item in data_1)
    return partial(standardize, mean_x, stdev_x)

z = prepare_z(data_1)
for row in data_2:
    print(row, z(row.x))
