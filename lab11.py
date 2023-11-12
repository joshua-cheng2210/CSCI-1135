import random 
#  A: self.alpha
#     self.delta
#     self.left
#     self.right

#  B: def __init__
#     def __repr__
#     def __add__

#C: 5
#E: Error, epsilon is not defined in the add function
#F: 14

#2
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.all_suit = 'CDHS'
        self.all_rank = '23456789TJQKA'
    def __repr__(self):
        if self.rank not in self.all_rank:
            self.rank = '2'
        if self.suit not in self.all_suit:
            self.suit = 'C'
        return self.rank + self.suit

#3 (See Above)

#4

def listmaker():
    out = []
    for rank in '23456789TJQKA':
        for suit in 'CDHS':
            out.append(rank + suit)
    return random.sample(out, len(out))

class Deck:
    def __init__(self):
        self.discard_pile = []
        self.draw_pile = listmaker()
    def discard(self, card):
        self.discard_pile.append(card)
        self.draw_pile.remove(card)
    def draw(self):
        if len(self.draw_pile) != 0:
            return random.choice(self.draw_pile)
        else:
            self.draw_pile = random.sample(self.discard_pile, len(self.discard_pile))
            self.discard_pile = []

#6
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def hit(self, deck):
        self.hand.append(deck.draw())
    def score(self):
        total = 0
        for card in self.hand:
            if card[0].isdigit():
                total += card[0]
            elif card[0] in 'JQK':
                total += 10
            else:
                if total <= 10:
                    total += 11
                else:
                    total += 1
        return total

#8
def blackjack():
    user = Player()
    dealer = Player()
    x = Deck()
    while len(user.hand) < 2:
        user.hand.append(x.draw)
        user.hand.append(x.draw)
        dealer.hand.append(x.draw)
        dealer.hand.append(x.draw)