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

