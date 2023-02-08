# Exer-06-Combining-map-and-reduce-transformations

typical_iterator = iter([0, 1, 2, 3, 4])
print(sum(typical_iterator))
print(sum(typical_iterator))

"""
round(sum_fuel(clean_data(row_merge(log_rows))), 3)
"""


def clean_data(source):
    namespace_iter = map(make_namespace, source)
    filtered_source = filter(remove_date, namespace_iter)
    start_iter = map(start_datetime, filtered_source)
    end_iter = map(end_datetime, start_iter)
    delta_iter = map(duration, end_iter)
    fuel_iter = map(fuel_use, delta_iter)
    per_hour_iter = map(fuel_per_hour, fuel_iter)
    return per_hour_iter


###

from types import SimpleNamespace


def make_namespace(row):
    ns = SimpleNamespace(
        date=row[0],
        start_time=row[1],
        start_fuel_height=row[2],
        end_time=row[4],
        end_fuel_height=row[5],
        other_notes=row[7],
    )
    return ns


###


def remove_date(row_ns):
    return not (row_ns.date == "date")


###

import datetime


def timestamp(date_text, time_text):
    date = datetime.datetime.strptime(date_text, "%m/%d/%y").date()
    time = datetime.datetime.strptime(time_text, "%I:%M:%S %p").time()
    timestamp = datetime.datetime.combine(date, time)
    return timestamp


###


def start_datetime(row_ns):
    row_ns.start_timestamp = timestamp(row_ns.date, row_ns.start_time)
    return row_ns


def end_datetime(row_ns):
    row_ns.end_timestamp = timestamp(row_ns.date, row_ns.end_time)
    return row_ns


def duration(row_ns):
    travel_time = row_ns.end_timestamp - row_ns.start_timestamp
    row_ns.travel_hours = round(travel_time.total_seconds() / 60 / 60, 1)
    return row_ns


###


def fuel_use(row_ns):
    end_height = float(row_ns.end_fuel_height)
    start_height = float(row_ns.start_fuel_height)
    row_ns.fuel_change = start_height - end_height
    return row_ns


def fuel_per_hour(row_ns):
    row_ns.fuel_per_hour = row_ns.fuel_change / row_ns.travel_hours
    return row_ns

###

from statistics import *

def avg_fuel_per_hour(iterable):
    return mean(row.fuel_per_hour for row in iterable)

def stdev_fuel_per_hour(iterable):
    return stdev(row.fuel_per_hour for row in iterable)

round(avg_fuel_per_hour(
    clean_data(row_merge(log_rows))), 3)

###

data = tuple(clean_data(row_merge(log_rows)))
m = avg_fuel_per_hour(data)
s = 2*stdev_fuel_per_hour(data)
print("Fuel use {m:.2f} ±{s:.2f}".format(m=m, s=s))

###

from itertools import tee 

data1, data2 = tee(clean_data(row_merge(log_rows)), 2)
m = avg_fuel_per_hour(data1)
s = 2*stdev_fuel_per_hour(data2)

