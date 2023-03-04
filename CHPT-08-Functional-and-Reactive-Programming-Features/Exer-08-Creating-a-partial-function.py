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
