# Exer-10-Controlling-the-order-of-dict-keys
from pathlib import Path
import csv
data_path = Path('craps.csv')
with data_path.open() as data_file:
    reader = csv.DictReader(data_file)
    data = list(reader)
#for row in data:
    # print(row)

# ( (name, raw_row[name]) for name in reader.fieldnames )

from collections import OrderedDict

with data_path.open() as data_file:
    reader = csv.DictReader(data_file)
    for raw_row in reader:
        column_sequence = ( (name, raw_row[name]) 
           for name in reader.fieldnames )
        good_row = OrderedDict(column_sequence)
        print(good_row)

# OrderedDict( (name, raw_row[name]) for name in reader.fieldnames )