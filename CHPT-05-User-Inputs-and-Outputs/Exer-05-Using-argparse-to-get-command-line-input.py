# Exer-05-Using-argparse-to-get-command-line-input

"""
slott$ python3 ch05_r04.py -r KM 36.12,-86.67 33.94,-118.40
   From (36.12, -86.67) to (33.94, -118.4) in KM = 2887.35
"""

"""
 slott$ python3 ch05_r04.py -r KM 36.12,-86.67 33.94,-118asd
   usage: ch05_r04.py [-h] [-r {NM,MI,KM}] p1 p2
   ch05_r04.py: error: argument p2: could not convert string to float:
   '-118asd'
"""

from ch03_r05 import haversine, MI, NM, KM

def display(lat1, lon1, lat2, lon2, r):
    r_float = {'NM': NM, 'KM': KM, 'MI': MI}[r]
    d = haversine(lat1, lon1, lat2, lon2, r_float)
    print("From {lat1}, {lon1} to {lat2}, {lon2}"
          "in {r} = {d:.2f}".format_map(vars()))

###

from ch03_r04 import display
display(36.12, -86.67, 33.94, -118.4, 'NM')
