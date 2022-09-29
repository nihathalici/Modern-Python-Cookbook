# Exer-06-Writing-clear-documentation-strings-with-RST-markup

def Twc(T, V):
    """Computes the wind chill temperature.
    
    The wind-chill, :math: `T_{wc}`, is based on
    air temperature, T, and wind speed, V.

    :param T: Temperature in °C
    :param V: Wind Speed in kph
    :returns: Wind-Chill temperature in °C 
    :raises ValueError: for win speeds under over 4.8 kph or T above 10°C 

    >>> round(Twc(-10, 25), 1)
    -18.8

    See https://en.wikipedia.org/wiki/Wind_chill
    
    .. math::
       T_{wc}(T_a, V) = 13.12 + 0.6215 T_a - 11.37 V^{0.16} + 0.3965 T_a V^{0.16}

    """
    if V < 4.8 or T > 10.0:
        raise ValueError("V must be over 4.8 kph, T must be below 10°C")
    return 13.12 + 0.6215*T - 11.37*V**0.16 + 0.3965*T*V**0.16

def wind_chill_table():
    """Uses :func: `Twc` to produce a wind-chill 
    table for temperatures from -30 °C to 10 °C and
    wind speeds from 5kph to 50kph.
    """
