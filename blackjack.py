from deck import Deck
from player import Player
from rich.console import Console
import time

console = Console()

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.deck.generate_and_shuffle()
        self.player = Player(False, self.deck, 50)
        self.dealer = Player(True, self.deck, 100)
        self.possible_winnings = 0
    
    
    def initial_bet(self):
        console.print("\n\n")
        self.player.show_money()
        if self.player.money >= 2:
            name = console.input("MIN $2 TO PLAY ~ ARE YOU IN? ENTER (y) OR (n)\n")
            # possible bet sizes based on how much money player has
            possible_bets = []
            for n in range(2, int(self.player.money+1)):
                possible_bets.append(n)
            if name.lower() == "y":
                # asks for amount of money to put in until valid number is entered
                while True:
                    bet_amount = int(input("HOW MUCH ARE YOU PUTTING IN?\n"))
                    if bet_amount not in possible_bets:
                        console.print("INVALID AMOUNT, ENTER AGAIN")
                        continue
                    else:
                        break                    
                self.player.money -= bet_amount
                self.possible_winnings = bet_amount
                self.deal_hand()
                        
            else:
                quit("THANKS FOR COMING")
        else:
            console.print("INSUFFICIENT FUNDS ~ THANKS FOR COMING")
            quit()


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
        if self.player.total == 21:
            self.move_stand()
        elif len(self.player.hand) == 2 and self.player.total != 21:
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
        self.eval_aces_player()
        if self.player.total > 21:
            self.player.show_hand()
            console.print("OVER 21 ~ YOU LOSE\n")
            self.reset_table()
        else:
            self.player.show_hand()
            self.make_move()


    def move_double_down(self):
        self.possible_winnings *= 2
        self.player.money -= self.possible_winnings
        self.player.hit()
        self.eval_aces_player()
        if self.player.total > 21:
            self.player.show_hand()
            console.print("OVER 21 ~ YOU LOSE\n")
            self.reset_table()
        else:
            self.player.show_hand()
            self.move_stand()

    def move_stand(self):
        self.dealer.show_hand()
        while self.dealer.total < 17:
            time.sleep(1)
            self.dealer.hit()
            self.dealer.show_hand()
            self.eval_aces_dealer()
            if self.dealer.total > 21:
                console.print("DEALER BUSTS ~ YOU WIN $" + str(self.possible_winnings*2))
                self.player.money += self.possible_winnings*2
                self.reset_table()
        if self.player.total < self.dealer.total:
            console.print("DEALER WINS")
            self.reset_table()
        elif self.player.total > self.dealer.total and self.player.total == 21:
            console.print("BLACKJACK ~ YOU WIN $" + str(self.possible_winnings*2.5))
            self.player.money += self.possible_winnings*2.5
            self.reset_table()
        elif self.player.total > self.dealer.total:
            console.print("YOU WIN $" + str(self.possible_winnings*2))
            self.player.money += self.possible_winnings*2
            self.reset_table()
        else:
            console.print("PUSH ~ NO WINNER")
            self.player.money += self.possible_winnings
            self.reset_table()
        
    def eval_aces_dealer(self):
        a_count = 0
        for c in self.dealer.hand:
            if c.card_value() == 11:
                a_count += 1
        while self.dealer.total > 21 and a_count > 0:
            self.dealer.total -= 10
            a_count -= 1

    def eval_aces_player(self):
        a_count = 0
        for c in self.player.hand:
            if c.card_value() == 11:
                a_count += 1
        while self.player.total > 21 and a_count > 0:
            self.player.total -= 10
            a_count -= 1

    def reset_table(self):
        self.player.hand.clear()
        self.dealer.hand.clear()
        self.deck.generate_and_shuffle()
        self.initial_bet()
    

        



b = Blackjack()
b.initial_bet()