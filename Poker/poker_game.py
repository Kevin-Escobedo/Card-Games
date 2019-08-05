#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com

#Texas Hold'em Rules
#Hole - Each player is dealt 2 cards face down
#Community - 5 more cards dealt face up
#   Dealt in 3 stages
#       Flop - First 3 cards
#       Turn - One more card
#       River - Last card
#Players construct best five card hand from 7 cards

import card_class

class PokerGame:
    def __init__(self):
        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []
        self.flop = []
        self.turn = []
        self.river = []
        
    def create_deck(self) -> [card_class.Card]:
        '''Makes the deck'''
        values = [x for x in range(2, 11)] + ["J", "Q", "K", "A"]
        suits = ["Heart", "Diamond", "Spade", "Club"]
        return [card_class.Card(suit, value) for suit in suits for value in values]

    def check_royal_flush(self, hand) -> bool:
        '''Checks if cards contain five cards of the same suit (10 - A) #1'''
        cards = sorted(hand + self.flop + self.turn + self.river, key = lambda c: int(c))
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
        cards = sorted(hand + self.flop + self.turn + self.river, key = lambda c: int(c))
        lower = 2
        higher = 6

        collected_cards = []
        collected_values = []

        while higher != int(card_class.Card("Heart", "A")) + 1:
            reach = range(lower, higher+1)
            for card in cards:
                if int(card) in reach and int(card) not in collected_values:
                    collected_cards.append(card)
                    collected_values.append(int(card))
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
        cards = sorted(hand + self.flop + self.turn + self.river, key = lambda c: int(c))
        totals = dict()
        for card in cards:
            if int(card) in totals:
                totals[int(card)] += 1
            else:
                totals[int(card)] = 1
        for key in totals:
            if totals[key] == 4:
                return True
        return False

    def check_full_house(self, hand) -> bool:
        '''Checks if cards contain three of a kind with a pair #4'''
        cards = sorted(hand + self.flop + self.turn + self.river, key = lambda c: int(c))
        totals = dict()
        for card in cards:
            if int(card) in totals:
                totals[int(card)] += 1
            else:
                totals[int(card)] = 1
      check_totals = [totals[key] for key in totals]
      return 3 in check_totals and 2 in check_totals

  def check_flush(self, hand) -> bool:
      '''Checks if cards contain 5 cards of the same suit #5'''
      cards = sorted(hand + self.flop + self.turn + self.river, key = lambda c: int(c))
      
      clubs = [card for card in cards if card.suit == "Club"]
      diamonds = [card for card in cards if card.suit == "Diamond"]
      spades = [card for card in cards if card.suit == "Spade"]
      hearts = [card for card in cards if card.suit == "Heart"]

      temp = [clubs, diamonds, spades, hearts]

      check_totals = [len(stacks) >= 5 for stacks in L]

      return any(check_totals)



if __name__ == "__main__":
    p = PokerGame()
    assert len(p.deck) == 52
    
