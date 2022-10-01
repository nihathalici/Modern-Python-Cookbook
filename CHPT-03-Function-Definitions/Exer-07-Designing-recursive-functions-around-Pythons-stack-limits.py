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
