# Exer-05-String-parsing-with-regular-expressions

ingredient = "Kumquat: 2 cups"
# (ingredient words): (amount digits) (unit words)

import re
pattern_text = r'(?P<ingredient>\w+):\s+(?P<amount>\d+)\s+(?P<unit>\w+)'
pattern = re.compile(pattern_text)
match = pattern.match(ingredient)
print(match is None)
print(match.groups())

print(match.group('ingredient'))
print(match.group('amount'))
print(match.group('unit'))

###

ingredient_pattern = re.compile(
    r'(?P<ingredient>\w+):\s+'  # name of the ingredient up to the ":"
    r'(?P<amount>\d+)\s+'       # amount, all digits up to a space
    r'(?P<unit>\w+)'            # units, alphanumeric characters
)