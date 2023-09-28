from deck import Deck
from player import Player
from rich.console import Console

console = Console()

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.generate_and_shuffle()
        self.player = Player(False, self.deck, 50)
        self.dealer = Player(True, self.deck, 100)

    def initial_bet(self):
        self.player.show_money()
        if self.player.money >= 2:
            name = console.input("MIN $2 TO PLAY ~ ARE YOU IN? ENTER (y) OR (n)\n")
            # possible bet sizes based on how much money player has
            possible_bets = []
            for n in range(2, self.player.money+1):
                possible_bets.append(n)
            if name.lower() == "y":
                bet_amount = int(input("HOW MUCH ARE YOU PUTTING IN?\n"))
                if bet_amount in possible_bets:
                    self.player.money -= bet_amount
                    self.deal_hand()
            else:
                quit("THANKS FOR COMING")


    def deal_hand(self):
        self.player.deal()
        self.dealer.deal()

        console.print("[red]DEALER'S HAND[/]")
        self.dealer.hand[0].show_card()
        console.print("\[[grey93]??[/]]\n\n")
        self.player.show_hand()
        self.player.show_money()

        self.make_move()

    def make_move(self):
        if len(self.player.hand) == 2 and self.player.total != 21:
            move = console.input("ENTER NEXT MOVE: HIT (h), DOUBLE DOWN (d), STAND (s)\n")
        else:
            move = console.input("ENTER NEXT MOVE: HIT (h), STAND (s)\n")
        if move == "h":
            self.move_hit()
        elif move == "d":
            self.move_double_down()
        else:
            self.move_stand()


    def move_hit(self):
        self.player.hit()
        if self.player.total > 21:
            self.player.show_hand()
            console.print("OVER 21 ~ YOU LOSE\n")
            self.initial_bet()
        else:
            self.player.show_hand()
            self.make_move()


    def move_double_down(self):
        quit()

    def move_stand(self):
        quit()

    def eval_aces(self):
        quit()

b = Blackjack()
b.initial_bet()