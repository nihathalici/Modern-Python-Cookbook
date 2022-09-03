# Exer-05-Designing-complex-if-elif-chains

from re import A


dice = die_1 + die_2
if dice in (2, 3, 12):
    game.craps()
elif dice in (7, 11):
    game.winner()
elif dice in (4, 5, 6, 8, 9, 10):
    game.point(die)
else:
    raise Exception('Design Problem Here: not all conditions accounted for')

###

if a >= b:
    m = a 
elif b >= a:
    m = b 
else:
    raise Exception( 'Design Problem')
assert (m = a or m = b) and m > a and m > b
