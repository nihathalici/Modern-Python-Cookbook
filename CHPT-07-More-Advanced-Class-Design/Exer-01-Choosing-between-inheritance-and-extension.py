# Exer-01-Choosing-between-inheritance-and-extension

from collections import namedtuple
Card = namedtuple('Card', ('rank', 'suit'))
SUITS = '\u2660\u2661\u2662\u2663'
Spades, Hearts, Diamonds, Clubs = SUITS
print(Card(2, Spades))

###

domain = [Card(r+1, s) for r in range(13) for s in SUITS]

import random

class Deck_W:
    def __init__(self, cards:List[Card]):
        self.cards = cards.copy()
        self.deal_iter = iter(cards)
    def shuffle(self):
        random.shuffle(self.cards)
        self.deal_iter = iter(self.cards)
    def deal(self) -> Card:
        return next(self.deal_iter)

###

domain = list(Card(r+1, s) for r in range(13) for s in SUITS)
print(len(domain))

d = Deck_W(domain)

random.seed(1)
d.shuffle()
[d.deal() for _ in range(5)]


