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

###

"""
for i in some_collection:
    process(i)
"""
"""
the_iterator = iter(some_collection)
try:
    while True:
        i = next(the_iterator)
        process(i)
except StopIteration:
    pass
"""


def gen_func():
    print("pre-yield")
    yield 1
    print("post-yield")
    yield 2


y = gen_func()
next(y)
next(y)
next(y)  # StopIteration

###


def primeset(source):
    for i in source:
        if prime(i):
            yield prime


p_10 = set(primeset(range(2, 2000000)))

p_10 = {i for i in range(2, 2000000) if prime(i)}


def map(m, S):
    for s in S:
        yield m(s)


def filter(f, S):
    for s in S:
        if f(s):
            yield s


p_10 = set(filter(prime, range(2, 2000000)))
