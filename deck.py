import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []

    def generate_and_shuffle(self):
        for i in range(1, 14):
            for j in range(4):
                self.cards.append(Card(i, j))
        random.shuffle(self.cards)

    def draw_card(self, num):
        drawn_cards = []
        for i in range(num):
            card = self.cards.pop()
            drawn_cards.append(card)
        return drawn_cards