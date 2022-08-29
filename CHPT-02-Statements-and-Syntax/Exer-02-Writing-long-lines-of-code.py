# Exer-02-Writing-long-lines-of-code

import math

example_value = (63/25) * (17+15*math.sqrt(5)) / (7+15*math.sqrt(5))
mantissa_fraction, exponent = math.frexp(example_value)
mantissa_whole = int(mantissa_fraction*2**53)
message_text = 'the internal representation is {mantissa:d}/2**53*2**{exponent:d}'.format(mantissa=mantissa_whole, exponent=exponent)
print(message_text)

###
# Using backslash

message_text = 'the internal representation is \
{mantissa:d}/2**53*2**{exponent:d}'.\
    format(mantissa=mantissa_whole, exponent=exponent)

print(message_text)

###
# Using the () characters

import math

example_value1 = (63/25) * (17+15*math.sqrt(5)) / (7+15*math.sqrt(5))
example_value2 = (63/25) * ( (17+15*math.sqrt(5)) / (7+15*math.sqrt(5)) )
print(example_value1 == example_value2)

example_value3 = (63/25) * (
    (17+15*math.sqrt(5)) 
  / (7+15*math.sqrt(5))
)
print(example_value3 == example_value1)

###
# Using string literal concatenation

message_text = (
    'the internal representation '
    'is {mantissa:d}/2**53*2**{exponent:d}'
    ).format(
    mantissa=mantissa_whole, exponent=exponent)

print(message_text)

###
# Assigning intermediate results

import math

example_value = (63/25) * (17+15*math.sqrt(5)) / (7+15*math.sqrt(5))
a = (63/25)
b = (17+15*math.sqrt(5))
c = (7+15*math.sqrt(5))
example_value = a * b / c

###

from math import (sin, cos, tan
   sqrt, log, frexp)
