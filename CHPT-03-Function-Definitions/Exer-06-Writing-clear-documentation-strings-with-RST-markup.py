# Exer-06-Writing-clear-documentation-strings-with-RST-markup

def Twc(T, V):
    """Computes the wind chill temperature.
    
    The wind-chill, :math: `T_{wc}`, is based on
    air temperature, T, and wind speed, V.

    :param T: Temperature in °C
    :param V: Wind Speed in kph
    :returns: Wind-Chill temperature in °C 
    :raises ValueError: for win speeds under over 4.8 kph or T above 10°C 
    """
    if V < 4.8 or T > 10.0:
        raise ValueError("V must be over 4.8 kph, T must be below 10°C")
    return 13.12 + 0.6215*T - 11.37*V**0.16 + 0.3965*T*V**0.16
