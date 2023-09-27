class Card:
    def __init__(self, value, suit):
        self.cost = value
        self.value = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"][value-1]
        self.suit = "♦♣♥♠" [suit]
    
    def cardValue(self):
        if self.cost == 1:
            return 11
        elif self.cost >= 10:
            return 10
        else:
            return self.cost
    
    def show(self):
        print(f'\[{self.value}{self.suit}\]')