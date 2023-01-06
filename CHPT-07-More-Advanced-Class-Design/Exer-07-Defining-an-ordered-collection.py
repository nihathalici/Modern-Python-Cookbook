# Exer-07-Defining-an-ordered-collection

from ch07_r06a import *
import bisect


class Hand:
    def __init__(self, card_iter):
        self.cards = list(card_iter)
        self.cards.sort()

    def add(self, aCard: Card):
        bisect.insort(self.cards, aCard)

    def index(self, aCard: Card):
        i = bisect.bisect_left(self.cards, aCard)
        if i != len(self.cards) and self.cards[i] == aCard:
            return i
        raise ValueError

    def __contains__(self, aCard: Card):
        try:
            self.index(aCard)
            return True
        except ValueError:
            return False

    def __iter__(self):
        return iter(self.cards)

    def __le__(self, other):
        for card in self:
            if card not in other:
                return False
        return True


from ch07_r06 import make_deck, make_card, Hand
import random

random.seed(4)

deck = make_deck()
random.shuffle(deck)
h = Hand(deck[:12])
h.cards

pinochle = Hand([make_card(11, "♢"), make_card(12, "♠")])
pinochle <= h

sum(c.points() for c in h)

###

while lo < hi:
    mid = (lo + hi) // 2
    if x < a[mid]:
        hi = mid
    else:
        lo = mid + 1
