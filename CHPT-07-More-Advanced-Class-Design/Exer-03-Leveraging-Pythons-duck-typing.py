# Exer-03-Leveraging-Pythons-duck-typing

import random

class Dice1:
    def __init__(self, seed=None):
        self._rng = random.Random(seed)
        self.roll()
    def roll(self):
        self.dice = (self._rng.randint(1,6),
                      self._rng.randint(1,6))
        return self.dice

class Die:
    def __init__(self, rng):
        self._rng = rng
    def roll(self):
        return self._rng.randint(1,6)

class Dice2:
    def __init__(self, seed=None):
        self._rng = random.Random(seed)
        self._dice = [Die(self._rng) for _ in range(2)]
        self.roll()
    def roll(self):
        self.dice = tuple(d.roll() for d in self._dice)
        return self.dice

def roller(dice_class, seed=None, *, samples=10):
    dice = dice_class(seed)
    for _ in range(samples):
        yield dice.roll()

print(list(roller(Dice1, 1, samples=5)))
print(list(roller(Dice2, 1, samples=5)))