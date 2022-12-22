# Exer-05-Using-more-complex-structures-maps-of-lists

from collections import defaultdict

module_details = defaultdict(list)

for row in data:
    module_details[row[2]].append(row)

from typing import *

def summarize(data) -> Mapping[str, List]:
    # the body of the function.


class ModuleEvents(dict):
    def add_event(self, event):
        if event[2] not in self:
            self[event[2]] = list()
        self[event[2]].append(row)

module_details = ModuleEvents()
for row in data:
    module_details.add_event(row)

