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
