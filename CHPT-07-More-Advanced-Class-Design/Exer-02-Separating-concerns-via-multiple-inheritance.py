# Exer-02-Separating-concerns-via-multiple-inheritance

class Card:
    __slots__ = ('rank', 'suit')
    def __init__(self, rank, suit):
        super().__init__()
        self.rank = rank
        self.suit = suit
    def __repr__(self):
        return "{rank:2d} {suit}".format(
            rank=self.rank, suit=self.suit
        )

class AceCard(Card):
    def __repr__(self):
        return " A {suit}".format(
            rank=self.rank, suit=self.suit)

class FaceCard(Card):
    def __repr__(self):
        names = {11: 'J', 12: 'Q', 13: 'K'}
        return " {name} {suit}".format(
            rank=self.rank, suit=self.suit,
            name=names[self.rank]
        )

###

class CribbagePoints:
    def points(self):
        return self.rank

###

class CribbageFacePoints(CribbagePoints):
    def points(self):
        return 10

###

class CribbageAce(AceCard, CribbagePoints):
    pass

class CribbageCard(Card, CribbagePoints):
    pass

class CribbageFace(FaceCard, CribbageFacePoints):
    pass

###

def make_card(rank, suit):
    if rank == 1: return CribbageAce(rank, suit)
    if 2 <= rank < 11: return CribbageCard(rank, suit)
    if 11 <= rank: return CribbageFace(rank, suit)

from ch07_r02 import make_card, SUITS
import random
random.seed(1)

deck = [make_card(rank+1, suit) for rank in range(13) for suit in SUITS]
random.shuffle(deck)
len(deck)
deck[:5]

sum(c.points() for c in deck[:5])

c = deck[5]
print(c)
c.__class__.__name__
c.__class__.mro()

###

class Logged:
    def __init__(self, *args, **kw):
        self.logger = logging.getLogger(self.__class__.__name__)
        super().__init__(*args, **kw)
    def points(self):
        p = super().points()
        self.logger.debug("points {0}".format(p))
        return p

###

class LoggedCribbageAce(Logged, AceCard, CribbagePoints):
    pass

class LoggedCribbageCard(Logged, Card, CribbagePoints):
    pass

class LoggedCribbageFace(Logged, FaceCard, CribbageFacePoints):
    pass

def make_logged_card(rank, suit):
    if rank == 1: return LoggedCribbageAce(rank, suit)
    if 2 <= rank < 11: return LoggedCribbageCard(rank, suit)
    if 11 <= rank: return LoggedCribbageFace(rank, suit)

deck = [make_logged_card(rank+1, suit)
    for rank in range(13)
        for suit in SUITS]