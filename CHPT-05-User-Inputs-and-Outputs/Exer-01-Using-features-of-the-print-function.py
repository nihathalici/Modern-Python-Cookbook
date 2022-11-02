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


    
