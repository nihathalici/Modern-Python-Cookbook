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

###


def row_merge(source_iter):
    group = []
    for row in source_iter:
        if len(row[0]) != 0:
            if group:
                yield group
            group = row.copy()
        else:
            group.extend(row)
    if group:
        yield group


###

import datetime


def start_datetime(row):
    travel_date = datetime.datetime.strptime(row[0], "%m/%d/%y").date()
    start_time = datetime.datetime.strptime(row[1], "%I:%M:%S %p").time()
    start_datetime = datetime.datetime.combine(travel_date, start_time)
    new_row = row + [start_datetime]
    return new_row


def end_datetime(row):
    travel_date = datetime.datetime.strptime(row[0], "%m/%d/%y").date()
    end_time = datetime.datetime.strptime(row[4], "%I:%M:%S %p").time()
    end_datetime = datetime.datetime.combine(travel_date, end_time)
    new_row = row + [end_datetime]
    return new_row


"""
for starting and ending.def duration(row):
    travel_hours = round((row[10]-row[9]).total_seconds()/60/60, 1)
    new_row = row+[travel_hours]
    return new_row
"""


def skip_header_date(rows):
    for row in rows:
        if row[0] == "date":
            continue
        yield row


def date_conversion(source):
    tail_gen = skip_header_date(source)
    start_gen = (start_datetime(row) for row in tail_gen)
    end_gen = (end_datetime(row) for row in start_gen)
    duration_gen = (duration(row) for row in end_gen)
    return duration_gen
