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
