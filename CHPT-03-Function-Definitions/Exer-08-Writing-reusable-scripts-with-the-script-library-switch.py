# Exer-08-Writing-reusable-scripts-with-the-script-library-switch

import csv 
import pathlib
from math import radians, sin, cos, sqrt, asin
from functools import partial

MI = 3959
NM = 3440
KM = 6373

def haversine(lat_1: float, lon_1: float,
              lat_2: float, lon_2: float, *, R: float) -> float:
              ... and more ...

nm_haversine = partial(haversine, R=NM)

source_path = pathlib.Path('waypoints.csv')
with source_path.open() as source_file:
    reader = csv.DictReader(source_file)
    start = next(reader)
    for point in reader:
        d = nm_haversine(
            float(start['lat']), float(start['lon']),
            float(point['lat']), float(point['lon'])
        )
        print(start, point, d)
        start = point

###

