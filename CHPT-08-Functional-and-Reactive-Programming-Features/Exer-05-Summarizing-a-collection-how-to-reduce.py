# Exer-05-Summarizing-a-collection-how-to-reduce

from functools import reduce


def mul(a, b):
    return a * b


def prod(values):
    return reduce(mul, values, 1)


def factorial(n):
    return prod(range(1, n + 1))


# print(factorial(52))

print(factorial(52) // (factorial(5) * factorial(52 - 5)))

###

def reduce(function, iterable, base):
    result = base
    for item in iterable:
        result = function(result, item)
    return result

###

def mul(a, b):
    return a * b

add = lambda a, b: a + b
mul = lambda a, b: a * b

###

def prod2(values):
    return reduce(lambda a, b: a * b, values, 1)

###

from operator import add, mul 

###

def mymax(sequence):
    try:
        base = sequence[0]
        max_rule = lambda a, b: a if a > b else b 
        reduce(max_rule, sequence, base)
    except IndexError:
        raise ValueError

