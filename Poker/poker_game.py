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


    def check_royal_flush(self, hand) -> bool:
        '''Checks if cards contain five cards of the same suit (10 - A) #1'''
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

    def check_straight_flush(self, hand) -> bool:
        '''Checks if cards contain 5 consecutive cards of the same suit #2'''
        cards = sorted(hand + self.flop + self.turn + self.river, key = lambda c: self.card_values[c.value])
        lower = self.card_values[2]
        higher = self.card_values[6]

        collected_cards = []
        collected_values = []

        while higher != self.card_values["A"]:
            reach = range(lower, higher+1)
            for card in cards:
                if self.card_values[card.value] in reach and self.card_values[card.value] not in collected_values:
                    collected_cards.append(card)
                    collected_values.append(self.card_values[card.value])
            if len(collected_cards) >= 5:
                clubs = [card for card in collected_cards if card.suit == "Club"]
                diamonds = [card for card in collected_cards if card.suit == "Diamond"]
                spades = [card for card in collected_cards if card.suit == "Spade"]
                hearts = [card for card in collected_cards if card.suit == "Heart"]
                L = [clubs, diamonds, spades, hearts]
                check_totals = [len(stack) >= 5 for stack in L]
                if any(check_totals):
                    return True
            else:
                collected_cards = []
                collected_values = []
                lower += 1
                higher += 1
        return False

    def check_four_of_a_kind(self, hand) -> bool:
        '''Checks if cards contain four of a kind #3'''
        cards = sorted(hand + self.flop + self.turn + self.river, key = lambda c: self.card_values[c.value])
        totals = dict()
        for card in cards:
            if self.card_values[card.value] in totals:
                totals[self.card_values[card.value]] += 1
            else:
                totals[self.card_values[card.value]] = 1
        for key in totals:
            if totals[key] == 4:
                return True
        return False


