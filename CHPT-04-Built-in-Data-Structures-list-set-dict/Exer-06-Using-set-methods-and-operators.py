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


from statistics import mean

expected_time = float(expected(n))
data = samples(100, arrival1())
wait_times = list(coupon_collector(n, data))
average_time = mean(wait_times)

###

collection = set()
collection.add(1)
print(collection)

collection.add(1)
collection
1 in collection
item = 3
collection.union({item})

###

collection = collection | {item}
collection

###

collection.update( {4} )
collection