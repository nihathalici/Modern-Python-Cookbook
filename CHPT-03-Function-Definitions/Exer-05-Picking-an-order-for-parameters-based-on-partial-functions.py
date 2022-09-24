# Exer-05-Picking-an-order-for-parameters-based-on-partial-functions

from math import radians, sin, cos, sqrt, asin

MI= 3959
NM= 3440
KM= 6372

def haversine(lat_1: float, lon_1: float,
    lat_2: float, lon_2: float, R: float) -> float:
    """Distance between points.
    
    R is Earth's radius.
    R=MI computes in miles. Default is nautical miles.
    """
    Δ_lat = radians(lat_2) - radians(lat_1)
    Δ_lon = radians(lon_2) - radians(lon_1)
    lat_1 = radians(lat_1)
    lat_2 = radians(lat_2)

    a = sin(Δ_lat/2)**2 + cos(lat_1)*cos(lat_2)*sin(Δ_lon/2)**2
    c = 2*asin(sqrt(a))

    return R * c


