# Exer-04-Optimizing-small-objects-with-slots

class Hand:
    __slots__ = ('hand', 'bet')
    
    def __init__(self, bet, hand=None):
        self.hand = hand or []
        self.bet = bet
    
    def deal(self, card):
        self.hand.append(card)
    
        def __repr__(self):
            return "".format(
                class_ = self.__class__.__name__,
                **vars(self)
            )

from ch06_r04 import Card, Hand

h1 = Hand(2)
h1.deal(Card(rank=4, suit='♣'))
h1.deal(Card(rank=8, suit='♡'))
h1

###

h1.bet *= 2
h1

# h1.some_other_attribute = True # AttributeError:


