# Exer-10-Controlling-the-order-of-dict-keys
from pathlib import Path
import csv
data_path = Path('craps.csv')
with data_path.open() as data_file:
    reader = csv.DictReader(data_file)
    data = list(reader)
for row in data:
    print(row)