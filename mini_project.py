import random

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        for s in( "H", "D", "S", "C" ):
            for v in range(1, 14):
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()
    
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def show(self):
        print ("{} of {}".format(self.value, self.suit))


class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand=[]

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()

deck = Deck()
deck.shuffle()

bob = Player("bob")
bob.draw(deck).draw(deck)
bob.showHand()
