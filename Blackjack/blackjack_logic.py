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
        card = self.deck.pop()
        if self.turn % 2 == 0:
            self.player_hand.append(card)
        else:
            self.comp_hand.append(card)
        self.add_values(card)
        self.increment_turn()

    def increment_turn(self):
        self.turn += 1

    def add_values(self, card): #Need to fix for ace values
        if self.turn % 2 == 0:
            self.player_total += card.get_card_value()
        else:
            self.comp_total += card.get_card_value()



if __name__ == "__main__":
    b = Blackjack()
