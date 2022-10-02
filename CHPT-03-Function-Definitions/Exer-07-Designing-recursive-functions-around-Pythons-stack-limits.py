# Exer-07-Designing-recursive-functions-around-Pythons-stack-limits


def fact(n: int) -> int:
    if n == 0:
        return 1
    return n * fact(n-1)

def prod(int_iter):
    p = 1
    for x in int_iter:
        p *= x
    return p

def fact(n):
    return prod(range(1, n+1))

###

def ugly_fact(n):
    if n > 0:
        return fact(n - 1) * n
    elif n == 0:
        return 1
    else:
         raise Exception('Logic Error')

p = n  
while n != 1:
    n = n - 1
    p *= n

###

def fibo(n):
    if n <= 1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

###

from functools import lru_cache
from re import A

@lru_cache(128)
def fibo(n):
    if n <= 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

###

def fibo_iter():
    a = 1
    b = 1
    yield a 
    while True:
        yield b
        a, b = b, a+b

###

def fibo(n):
    """ 
    >>> fibo(7)
    21
    """
    for i, f_i in enumerate(fibo_iter()):
        if i == n: break 
    return f_i

