# Exer-01-Using-a-class-to-encapsulate-data-and-processing

import random

class Dice:
    def __init__(self):
        self.faces = None
    
    def roll(self):
        self.faces = (random.randint(1, 6), random.randint(1, 6))
    
    def total(self):
        return sum(self.faces)
    
    def hardway(self):
        return self.faces[0] == self.faces[1]
    
    def easyway(self):
        return self.faces[0] != self.faces[1]

import random
random.seed(1)

from ch06_r01 import Dice

d1 = Dice()
d1.roll()
d1.total()
d1.faces

###

d2 = Dice()
d2.roll()
d2.total()
d2.hardway()
d2.faces
d1.total()

