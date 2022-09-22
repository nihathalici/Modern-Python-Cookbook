# Exer-04-Writing-explicit-types-on-function-parameters

def temperature(*, f_temp=None, c_temp=None):
    if c_temp is None:
        return {'f_temp': f_temp, 'c_temp': 5*(f_temp-32)/9}
    elif f_temp is None:
        return {'f_temp': 32+9*c_temp/5, 'c_temp': c_temp}
    else:
        raise Exception("Logic Design Problem")

###

def temperature(*, f_temp=None, c_temp=None):
    """Convert between Fahrenheit temperature and
    Celsius temperature.
    
    :key f_temp: Temperature in °F.
    :key c_temp: Temperature in °C.
    :returns: dictionary with two keys:
        :f_temp: Temperature in °F.
        :c_temp: Temperature in °C.
    """

from typing import *

from decimal import Decimal
from typing import *
from unittest import result
Number = Union[int, float, complex, Decimal]

###

def temperature(*,
    f_temp: Optional[Number]=None,
    c_temp: Optional[Number]=None):

###

def temperature(*,
    f_temp: Optional[Number]=None,
    c_temp: Optional[Number]=None) -> Dict[str, Number]:

###

def temperature_bad(*,
    f_temp: Optional[Number]=None,
    c_temp: Optional[Number]=None) -> Number:

    if c_temp is None:
        c_temp = 5*(f_temp - 32) / 9
    elif f_temp is None:
        f_temp = 32 + 9 * c_temp / 5
    else:
        raise Exception( "Logic Design Problem" )
    result = {'c_temp': c_temp, 'f_temp': f_temp}
    return result


