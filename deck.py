import random
from card import Card

class Deck:
    def __init__(self):
        self.cards = []

    def generate_and_shuffle(self):
        # from ace to king
        for i in range(1, 14):

            # from diamond to spade
            for j in range(4):

                # inserts each card into deck
                self.cards.append(Card(i, j))

        random.shuffle(self.cards)

    def draw_card(self, num):
        drawn_cards = []

        # pops card from deck and returns to list of drawn cards
        for i in range(num):
            card = self.cards.pop()
            drawn_cards.append(card)
        return drawn_cards