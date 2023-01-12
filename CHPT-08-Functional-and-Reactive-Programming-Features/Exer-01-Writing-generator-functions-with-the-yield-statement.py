# Exer-01-Writing-generator-functions-with-the-yield-statement

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

###

import datetime


def parse_date_iter(source):
    for item in source:
        date = datetime.datetime.strptime(item[0], "%Y-%m-%d %H:%M:%S,%f")
        new_item = (date,) + item[1:]
        yield new_item


###

from pprint import pprint

# for item in parse_date_iter(data):
#    pprint(item)

print(parse_date_iter(data))
