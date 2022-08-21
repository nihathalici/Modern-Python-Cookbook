# Exer-03-Choosing-between-true-division-and-floor-division

total_seconds = 7385
hours = total_seconds//3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds//60
seconds = remaining_seconds % 60

print(hours, minutes, seconds)

# the alternative, using the divmod()

total_seconds = 7385
hours, remaining_seconds = divmod(total_seconds, 3600)
minutes, seconds = divmod(remaining_seconds, 60)
print(hours, minutes, seconds)

###

total_seconds = 7385
hours = total_seconds / 3600
print(round(hours, 4))

###

from fractions import Fraction
total_seconds = Fraction(7385)

hours = total_seconds / 3600
print(hours)
print(round(float(hours), 4))

print(7358.0 //3600.0)

from __future__ import division
