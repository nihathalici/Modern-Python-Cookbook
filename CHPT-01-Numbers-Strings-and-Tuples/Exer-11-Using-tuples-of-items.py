# Exer-11-Using-tuples-of-items

ingredient = "Kumquat: 2 cups"

import re
ingredient_pattern = re.compile(r'(?P<ingredient>\w+):\s+(?P<amount>\d+)\s+(?P<unit>\w+)')
match = ingredient_pattern.match(ingredient)
print(match.groups())

from fractions import Fraction
my_data = ('Rice', Fraction(1/4), 'cups')

one_tuple = ('item', )
print(len(one_tuple))

print(my_data[1])
ingredient, amount, unit = my_data
print(ingredient)
print(unit)

t = ('Kumquat', '2', 'cups')
print(len(t))
print(t.count('2'))
print(t.index('cups'))
print(t[2])
# print(t.index('Rice'))  # ValueError: tuple.index(x): x not in tuple
print('Rice' in t)  # False