# Exer-03-Applying-transformations-to-a-collection

"""
for item in source:
    new_item = some transformation of item
    yield new_item


def start_gen(tail_gen):
    for row in tail_gen:
        new_row = start_datetime(row)
        yield new_row


start_gen = (start_datetime(row) for row in tail_gen)

"""

data = [
    ("2016-04-24 11:05:01,462", "INFO", "module1", "Sample Message One"),
    ("2016-04-24 11:06:02,624", "DEBUG", "module2", "Debugging"),
    (
        "2016-04-24 11:07:03,246",
        "WARNING",
        "module1",
        "Something might have gone wrong",
    ),
]

import datetime


def parse_date_iter(source):
    for item in source:
        date = datetime.datetime.strptime(item[0], "%Y-%m-%d %H:%M:%S,%f")
        new_item = (date,) + item[1:]
        yield new_item


###

for row in parse_date_iter(data):
    print(row[0], row[3])

###

"""
for item in source:
    new_item = transformation(item)
    yield new_item
"""


def parse_date(item):
    date = datetime.datetime.strptime(item[0], "%Y-%m-%d %H:%M:%S, %f")
    new_item = (date,) + item[1:]
    return new_item


"""
for item in collection:
    new_item = parse_date(item)
    yield new_item
"""
(parse_date(item) for item in data)

for row in map(parse_date, data):
    print(row[0], row[3])
