# Exer-02-Using-super-flexible-keyword-parameters

from time import time
import warnings



def rtd(distance = None, rate=None, time=None):
    if distance is None:
        distance = rate * time
    elif rate is None:
        rate = distance / time
    elif time is None:
        time = distance / rate
    else:
        warnings.warning("Nothing to solve for")
    return dict(distance = distance, rate = rate, time = time)

#print(rtd(distance = 31.2, rate = 6))

result = rtd(distance = 31.2, rate = 6)
print( ("At {rate}kt, it takes {time}hrs to cover {distance}nm").format_map(result) )

###

def rtd2(distance, rate, time, **keywords):
    print(keywords) 

rtd2(rate = 6, time = 6.75, something_else = 60)

def rtd2(**keywords):
    rate = keywords.get('rate', None)
    time = keywords.get('time', None)
    distance = keywords.get('distance', None)
    #etc.