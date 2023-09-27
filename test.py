from deck import Deck
from player import Player
from rich.console import Console

console = Console()

class Test:
    def __init__(self):
        self.deck = Deck()
        self.deck.generate_and_shuffle()
        self.player = Player(False, self.deck)
        self.dealer = Player(True, self.deck)

    def play(self):
        p_status = self.player.deal()
        d_status = self.dealer.deal()

        console.print("[red]DEALER'S HAND[/]")
        self.dealer.hand[0].show_card()
        console.print("\[[grey93]??[/]]\n\n")
        self.player.show_hand()

        

t = Test()
t.play()