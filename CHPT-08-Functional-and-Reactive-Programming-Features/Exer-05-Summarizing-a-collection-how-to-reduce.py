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
