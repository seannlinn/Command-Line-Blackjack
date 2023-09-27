from deck import Deck
from player import Player
from rich.console import Console
from rich.prompt import Prompt
from rich.prompt import IntPrompt


console = Console()

class Test:
    def __init__(self):
        self.deck = Deck()
        self.deck.generate_and_shuffle()
        self.player = Player(False, self.deck, 50)
        self.dealer = Player(True, self.deck, 100)

    def initial_bet(self):
        self.player.show_money()
        if self.player.money >= 2:
            name = console.Prompt.ask("MIN $2 TO PLAY ~ ARE YOU IN? ENTER (y) OR (n)", choices=["y", "n"], default="y")
            # possible bet sizes based on how much money player has
            possible_bets = []
            for n in range(2, self.player.money+1):
                possible_bets += n
            if name.lower() == "y":
                bet_amount = console.IntPrompt("HOW MUCH ARE YOU PUTTING IN?")



    def play(self):
        p_status = self.player.deal()
        d_status = self.dealer.deal()

        console.print("[red]DEALER'S HAND[/]")
        self.dealer.hand[0].show_card()
        console.print("\[[grey93]??[/]]\n\n")
        self.player.show_hand()
        console.print("\n")
        self.player.show_money()

        

t = Test()
t.play()