# Exer-07-Implementing-there-exists-processing


def find_first(predicate, iterable):
    for item in iterable:
        if predicate(item):
            yield item
            break


lambda i: n % i == 0

import math


def prime(n):
    factors = find_first(
        lambda i: n % i == 0,
        range(2, int(math.sqrt(n) + 1)),
    )
    return len(list(factors)) == 0


###

from itertools import takewhile

n = 13

list(takewhile(lambda i: n % i != 0, range(2, 4)))

n = 15

list(takewhile(lambda i: n % i != 0, range(2, 4)))

###


def prime_t(n):
    tests = set(range(2, int(math.sqrt(n) + 1)))
    non_factors = set(takewhile(lambda i: n % i != 0, tests))
    return tests == non_factors
