# Exer-08-Using-settable-properties-to-update-eager-attributes

leg_1 = Leg()
leg_1.rate = 6.0  # knots
leg_1.distance = 35.6  # nautical miles
print("Cover {leg.distance:.1f}nm at {leg.rate:.2f}kt = {leg.time:.2f}hr".format(leg=leg_1))

class Leg:
    def __init__(self):
        self._rate = rate
        self._time = time 
        self._distance = distance

    @property
    def rate(self):
        return self._rate
    
    @rate.setter
    def rate(self, value):
        self._rate = value
        self._calculate('rate')
    
    @property
    def time(self):
        return self._time
    @time.setter
    def time(self, value):
        self._time = value
        self._calculate('time')
    @property
    def distance(self):
        return self._distance
    @distance.setter
    def distance(self, value):
        self._distance = value
        self._calculate('distance')

###

from collections import deque

# self._changes = deque(maxlen=2)

def _calculate(self, change):
    if change not in self._changes:
        self._changes.append(change)
    compute = {'rate', 'time', 'distance'} - set(self._changes)
    if compute == {'distance'}:
        self._distance = self._time * self._rate
    elif compute == {'time'}:
        self._time = self._distance / self._rate
    elif compute == {'rate'}:
        self._rate = self._distance / self._time
    
