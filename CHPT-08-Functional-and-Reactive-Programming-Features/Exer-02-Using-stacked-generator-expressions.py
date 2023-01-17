# Exer-02-Using-stacked-generator-expressions

from pathlib import Path
import csv

with Path("fuel.csv").open() as source_file:
    reader = csv.reader(source_file)
    log_rows = list(reader)
print(log_rows[0])
print(log_rows[-1])

###
"""
total_time = datetime.timedelta(0)
total_fuel = 0

for row in date_conversion(row_merge(source_data)):
    total_time += row['end_time'] - row['start_time']
    total_fuel += row['end_fuel'] - row['start_fuel']
"""
