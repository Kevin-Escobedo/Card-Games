#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com

#Texas Hold'em Rules
#Each player is dealt 2 cards face down - "Hole"

#5 more cards dealt face up "Community"
#Dealt in 3 stages

#Flop - First 3 cards
#Turn - One more card
#River - Last card

#Players construct best five card hand from 7 cards

import card_class

class PokerGame:
    def __init__(self):
        self.player_hand = []
        self.dealer_hand = []
        self.flop = []
        self.turn = []
        self.river = []


    def check_royal_flush(self, hand):
        '''Checks if cards contain five cards of the same suit (10 - A)'''
        cards = hand + self.flop + self.turn + self.river





