# Exer-08-Deleting-from-a-list-of-mappings

source = [
    {"title": "Eruption", "writer": ["Emerson"], "time": "2:43"},
    {"title": "Stones of Years", "writer": ["Emerson", "Lake"], "time": "3:43"},
    {"title": "Iconoclast", "writer": ["Emerson"], "time": "1:16"},
    {"title": "Mass", "writer": ["Emerson", "Lake"], "time": "3:09"},
    {"title": "Manticore", "writer": ["Emerson"], "time": "1:49"},
    {"title": "Battlefield", "writer": ["Lake"], "time": "3:57"},
    {"title": "Aquatarkus", "writer": ["Emerson"], "time": "3:54"},
]

from pprint import pprint

data = source.copy()
for item in data:
    if "Lake" in item["writer"]:
        print("remove", item["title"])

###

# data = source.copy()
# for index in range(len(data)):
#    if "Lake" in data[index]["writer"]:
#        del data[index]  # IndexError: list index out of range

###

# while x in list:
#    list.remove(x)

###


def index(data):
    for i in range(len(data)):
        if "Lake" in data[i]["writer"]:
            return i


data = source.copy()
position = index(data)
while position:
    del data[position]  # or data.pop(position)
    position = index(data)

i = 0

if "Lake" in data[i]["writer"]:
    del data[i]
else:
    i += 1

###

i = 0

while i != len(data):
    if "Lake" in data[i]["writer"]:
        del data[i]
    else:
        i += 1

pprint(data)

###

data = [item for item in source if not ("Lake" in item["writer"])]

###

data = list(filter(lambda item: not ("Lake" in item["writer"]), source))

###


def writer_rule(iterable):
    for item in iterable:
        if "Lake" in item["writer"]:
            continue
        yield item


data = list(writer_rule(source))
pprint(data)
