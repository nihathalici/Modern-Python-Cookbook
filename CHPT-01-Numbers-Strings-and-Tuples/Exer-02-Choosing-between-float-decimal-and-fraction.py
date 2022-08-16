# Exer-02-Choosing-between-float-decimal-and-fraction

from decimal import Decimal

tax_rate = Decimal('7.25')/Decimal(100)
purchase_amount = Decimal('2.95')
print(tax_rate * purchase_amount)

penny = Decimal('0.01')
total_amount = purchase_amount + tax_rate * purchase_amount
print( total_amount.quantize(penny) )

import decimal
print( total_amount.quantize(penny, decimal.ROUND_UP) )

from fractions import Fraction
sugar_cups = Fraction('2.5')
scale_factor = Fraction(5/8)
print(sugar_cups * scale_factor)
print(Fraction(24, 16))

###

answer = (19/155)*(155/19)
print(round(answer, 3))
print(1-answer)

###

print(float(total_amount))
print(float(sugar_cups * scale_factor))

###

print(Fraction(19/155))
print(Decimal(19/155))

###

print(6737037547376141 / 2 ** 53 * 2 ** 226)

###

import math

print(math.frexp(8.066E+67))

###

print((19/155) * (155/19) == 1.0)
print(math.isclose((19/155) * (155/19), 1))

###
import cmath 

# math.sqrt(-2)  # ValueError: math domain error
print(cmath.sqrt(-2))
