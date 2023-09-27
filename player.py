from rich.console import Console
from deck import Deck

console = Console()

class Player:
    def __init__(self, isDealer, deck):
        self.hand = []
        self.isDealer = isDealer
        self.deck = deck
        self.total = 0

    def hit(self):
        self.hand.extend(self.deck.draw(1))
        self.eval_total()
        if self.score > 21:
            return 1
        return 0
        
    def deal(self):
        self.hand.extend(self.deck.draw(2))
        self.eval_total()
        if self.score == 21:
            return 1
        return 0
    
    def eval_total(self):
        a_count = 0
        self.total = 0
        for card in self.hand:
            if card.card_value() == 11:
                a_count += 1
            self.total += card.card_value()

        # check if over 21 and there is an ace, change value from 11 to 1
        while a_count > 1 and self.total > 21:
            self.total -= 10
            a_count -= 1
        return self.total
    
    def show_hand(self):
        if self.isDealer:
            console.print("DEALER'S HAND")
        else:
            console.print("YOUR HAND")
        for c in self.hand:
            c.show_card()

    