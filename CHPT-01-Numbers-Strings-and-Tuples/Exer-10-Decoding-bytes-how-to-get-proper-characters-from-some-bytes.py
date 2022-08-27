# Exer-10-Decoding-bytes-how-to-get-proper-characters-from-some-bytes

import urllib.request

warnings_uri = "https://forecast.weather.gov/product_types.php?site=NWS"
with urllib.request.urlopen(warnings_uri) as source:
    warnings_text = source.read()

# curl -O http://www.nws.noaa.gov/view/national.php?prod=SMW&sid=AKQ
#   mv national.php\?prod\=SMW AKQ.html

print(warnings_text[:80])

document = forecast_text.decode('UTF-8')
document[:80]

import re 
title_pattern = re.compile(r"\<h3\>(.*?)\</h3\>")
title_pattern.search(document)

