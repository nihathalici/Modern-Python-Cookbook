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