# Exer-04-Picking-a-subset-three-ways-to-filter
"""
def skip_header_date(rows):
    for row in rows:
        if row[0] == "date":
            continue
        yield row


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
"""

###

import pprint

from pathlib import Path
import csv

with Path("fuel.csv").open() as source_file:
    reader = csv.reader(source_file)
    log_rows = list(reader)
print(log_rows[0])
print(log_rows[-1])


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


pprint(list(row_merge(log_rows)))

###


def pass_non_date(row):
    return row[0] != "date"


###
"""
for item collection:
    if pass_non_date(item):
        yield item
"""

###

(item for item in data if pass_non_date(item))

###

filter(pass_non_date, data)

###

for row in filter(pass_non_date, row_merge(data)):
    print(row[0], row[1], row[4])
