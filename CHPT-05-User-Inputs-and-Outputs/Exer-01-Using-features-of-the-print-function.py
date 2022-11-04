# Exer-01-Using-features-of-the-print-function

from pathlib import Path
import csv
from collections import OrderedDict

def get_fuel_use(source_path):
    with source_path.open() as source_file:
        rdr = csv.DictReader(source_file)
        od = (OrderedDict(
            [(column, row[column]) for column in rdr.fieldnames])
            for row in rdr)
        data = list(od)
    return data

source_path = Path('fuel2.csv')
fuel_use = get_fuel_use(source_path)
print(fuel_use)

###

for leg in fuel_use:
    start = float(leg['fuel height on'])
    finish = float(leg['fuel height off'])
    print("On", leg['date'],
    'from', leg['engine on'],
    'to', leg['engine off'],
    'change', start-finish, 'in.')

print("date", "start", "end", "depth", sep=" | ")
for leg in fuel_use:
    start = float(leg['fuel height on'])
    finish = float(leg['fuel height off'])
    print(leg['date'], leg['engine on'],
    leg['engine off'], start-finish, sep=" | ")

###

for leg in fuel_use:
    start = float(leg['fuel height on'])
    finish = float(leg['fuel height off'])
    print('date', leg['date'], sep='=', end=', ')
    print('on', leg['engine on'], sep='=', end=', ')
    print('off', leg['engine off'], sep='=', end=', ')
    print('change', start-finish, sep="=")

###

import sys

def print(*args, *, sep=None, end=None, file=sys.stdout):
    if sep is None: sep = ' '
    if end is None: end = '\n'
    arg_iter = iter(args)
    first = next(arg_iter)
    sys.stdout.write(repr(first))
    for value in arg_iter:
        sys.stdout.write(sep)
        sys.stdout.write(repr(value()))
    sys.stdout.write(end)

###

import sys
print("Red Alert!", file=sys.stderr)

###

# python3 myapp.py <input.dat >output.dat

from pathlib import Path
target_path = Path('somefile.dat')
with target_path.open('w', encoding='utf-8') as target_file:
    print("Some output", file=target_file)
    print("Ordinary log")


    
