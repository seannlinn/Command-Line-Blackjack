from rich.console import Console

console = Console()

class Card:
    def __init__(self, value, suit):
        self.cost = value
        self.value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"][value-1]
        self.suit = "♦♣♥♠" [suit]
    
    def card_value(self):
        # if card is Ace, set card value to 11
        if self.cost == 1:
            return 11
        
        # if card is 10, J, Q, K, set card value to 10
        elif self.cost >= 10:
            return 10
        
        # if card is from 2-9, set card value to its own value
        else:
            return self.cost
    
    def show_card(self):
        # if suit is a diamond, print with blue for suit
        if self.suit == 0:
            console.print("[" + self.value + "[blue]" + self.suit + "][/]")
        
        # if suit is a club, print with green for suit
        elif self.suit == 1:
            console.print("[" + self.value + "[green]" + self.suit + "][/]")

        # if suit is a heart, print with red for suit
        elif self.suit == 2:
            console.print("[" + self.value + "[red]" + self.suit + "][/]")  

        # if suit is a spade, print with no colour
        else:
            console.print("[" + self.value + self.suit + "]")
