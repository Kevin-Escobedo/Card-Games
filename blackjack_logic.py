#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
from card_class import Card
import random

class Blackjack:
    def __init__(self):
        self.suits = ["Heart", "Diamond", "Spade", "Club"]
        self.values = [x for x in range(2, 11)] + ["J", "Q", "K", "A"]
        self.deck = [Card(x, y) for x in self.suits for y in self.values]
        self.player_hand = []
        self.player_total = 0
        self.comp_hand = []
        self.comp_total = 0
        self.turn = 0

    def hit(self):
        '''Handles adding cards to a hand'''
        random.shuffle(self.deck)
        if self.turn % 2 == 0:
            self.player_hand.append(self.deck.pop())
        else:
            self.comp_hand.append(self.deck.pop())
        self.add_values()
        self.increment_turn()

    def increment_turn(self):
        self.turn += 1

    def add_values(self):
        pass


if __name__ == "__main__":
    b = Blackjack()
