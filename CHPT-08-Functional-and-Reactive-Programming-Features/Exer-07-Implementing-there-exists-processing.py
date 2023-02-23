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
