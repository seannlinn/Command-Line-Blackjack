import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []

    def generateAndShuffle(self):
        for i in range(1, 14):
            for j in range(4):
                self.cards.append(Card(i, j))
        random.shuffle(self.cards)

    def drawCard(self, num):
        drawnCards = []
        for i in range(num):
            card = self.cards.pop()
            drawnCards.append(card)
        return drawnCards
    
    