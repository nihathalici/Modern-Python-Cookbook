# Exer-01-Designing-functions-with-optional-parameters

import random

def die():
    return random.randint(1, 6)

def craps():
    return (die(), die())

random.seed(113)
print( die(), die() )

print( craps() )
print( craps() )

def zonk():
    return tuple(die() for x in range(6))

print(zonk())

def craps():
    return tuple(die() for x in range(2))

def dice(n):
    return tuple(die() for x in range(n)) 

print(dice(2))
print(dice(6))

def dice(n=2):
    return tuple(die() for x in range(n))

###

def dice(n):
    return (die() for x in range(n))

def craps():
    return dice(2)

def zonk():
    return dice(6)

def die(sides=6):
    return random.randint(1, 6)

def dice(n=2, sides=6):
    return tuple(die(sides) for x in range(n))
