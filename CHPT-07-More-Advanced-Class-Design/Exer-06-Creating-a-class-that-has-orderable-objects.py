# Exer-06-Creating-a-class-that-has-orderable-objects

from ch07_r02 import AceCard, Card. FaceCard, SUITS

class PinochlePoints:
    _points = {9: 0, 10: 10, 11: 2, 12: 3, 13: 4, 14: 11}
    def points(self):
        return self._points[self.rank]

class SortedCard:
    def __lt__(self, other):
        return (self.rank, self.suit) < (other.rank, other.suit)
    
    def __le__(self, other):
        return (self.rank, self.suit) <= (other.rank, other.suit)
    
    def __gt__(self, other):
        return (self.rank, self.suit) > (other.rank, other.suit)
    
    def __ge__(self, other):
        return (self.rank, self.suit) >= (other.rank, other.suit)
    
    def __eq__(self, other):
        return (self.rank, self.suit) == (other.rank, other.suit)
    
    def __ne__(self, other):
        return (self.rank, self.suit) != (other.rank, other.suit)

###

class PinochleAce(AceCard, SortedCard, PinochlePoints):
    pass

class PinochleFace(FaceCard, SortedCard, PinochlePoints):
    pass

class PinochleNumber(Card, SortedCard, PinochlePoints):
    pass

###

def make_card(rank, suit):
    if rank in (9, 10):
        return PinochleNumber(rank, suit)
    elif rank in (11, 12, 13):
        return PinochleFace(rank, suit)
    else:
        return PinochleAce(rank, suit)

from ch07_r06a import make_card

c1 = make_card(9, '♡')
c2 = make_card(10, '♡')
c1 < c2
c1 == c1
c1 == c2
c1 > c2

###

SUITS = '\u2660\u2661\u2662\u2663'
Spades, Hearts, Diamonds, Clubs = SUITS
def make_deck():
    return [make_card(r, s) for _ in range(2)
        for r in range(9, 15)
        for s in SUITS]
