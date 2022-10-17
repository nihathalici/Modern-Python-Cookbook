# Exer-06-Using-set-methods-and-operators

import random 

def arrival1(n=8):
    while True:
        yield random.randrange(n)

def samples(limit, generator):
    for n, value in enumerate(generator):
        if n == limit: break
        yield value

random.seed(1)

print(list(samples(10, arrival1())))

###

from fractions import Fraction

def expected(n=8):
    return n * sum(Fraction(1, (i+1)) for i in range(n))

print(expected(8))
print(round(float(expected(8))))

###

def coupon_collector(n, data):
    count, collection = 0, set()
    for item in data:
        count += 1
        collection.add(item)
        if len(collection) == n:
            yield count
            count, collection = 0, set()

