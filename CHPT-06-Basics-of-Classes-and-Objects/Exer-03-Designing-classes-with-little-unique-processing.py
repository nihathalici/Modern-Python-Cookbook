# Exer-03-Designing-classes-with-little-unique-processing

from collections import namedtuple

Card = namedtuple('Card', ('rank', 'suit'))
eight_hearts = Card(rank=8, suit='\N{White Heart Suit}')
print(eight_hearts)
print(eight_hearts.rank)
print(eight_hearts.suit)
print(eight_hearts[0])

# eight_hearts.suit = '\N{Black Spade Suit}' # AttributeError: can't set attribute

###

class Player:
    pass

p = Player()
p.stake = 100

###

from argparse import Namespace
from types import SimpleNamespace

Player = SimpleNamespace
player_1 = Player(stake=100, hand=[], insurance=None, bet=None)
player_1.bet = 10
player_1.stake -= player_1.bet
player_1.hand.append(eight_hearts)
print(player_1)