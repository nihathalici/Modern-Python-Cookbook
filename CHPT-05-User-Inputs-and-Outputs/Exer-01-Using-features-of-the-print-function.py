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