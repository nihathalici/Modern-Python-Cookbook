# Exer-09-Simplifying-complex-algorithms-with-immutable-data-structures

from typing import *


def get(text: str) -> Iterator[List[str]]:
    for line in text.splitlines():
        if len(line) == 0:
            continue
        yield line.split()


###

from collections import namedtuple

DataPair = namedtuple("DataPair", ["x", "y"])


def cleanse(iterable: Iterable[List[str]]) -> Iterator[DataPair]:
    for text_items in iterable:
        try:
            x_amount = float(text_items[0])
            y_amount = float(text_items[1])
            yield DataPair(x_amount, y_amount)
        except Exception as ex:
            print(ex, repr(text_items))
