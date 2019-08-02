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
        self.card_values = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7,
                8:8, 9:9, 10:10, "J": 10, "Q": 11, "K": 13, "A": 14}


    def check_royal_flush(self, hand):
        '''Checks if cards contain five cards of the same suit (10 - A)'''
        cards = sorted(hand + self.flop + self.turn + self.river, key = lambda c: self.card_values[c.value])
        royal = [card for card in cards if card.value in [10, "J", "Q", "K", "A"]]
        if len(royal) >= 5:
            clubs = [card for card in royal if card.suit == "Club"]
            diamonds = [card for card in royal if card.suit == "Diamond"]
            spades = [card for card in royal if card.suit == "Spade"]
            hearts = [card for card in royal if card.suit == "Heart"]
            L = [clubs, diamonds, spades, hearts]
            check_totals = [len(stacks) >= 5 for stacks in L]
            return any(check_totals)
        else:
            return False

    def check_straight_flush(self, hand):
        '''Checks if cards contain 5 consecutive cards of the same suit'''
        cards = sorted(hand + self.flop + self.turn + self.river, key = lambda c: self.card_values[c.value])

        




