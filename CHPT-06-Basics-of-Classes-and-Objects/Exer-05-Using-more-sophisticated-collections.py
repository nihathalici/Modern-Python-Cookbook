# Exer-05-Using-more-sophisticated-collections

import json
user = json.load('˜/app.json')
system = json.load('/etc/app.json')
application = json.load('/opt/app/default.json')

from collections import ChainMap
config = ChainMap(user, system, application)