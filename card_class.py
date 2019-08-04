#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com

class Card:
    def __init__(self, suit:str, value:str or int):
        '''Sets up card instance'''
        self.suit = suit
        self.value = value
        self.card_value = self.get_card_value()

    def get_card_value(self):
        '''Gets the value needed for blackjack'''
        if type(self.value) == int:
            return self.value
        else:
            return 10

##    def ace_value(self, turn, total): #Fix Later
##        '''Gets the ace value'''
##        if turn % 2 == 0:
##            self.player_choice(decision)
##        else:
##            if total <= 10:
##                return 11
##            else:
##                return 1
##
##    def player_choice(self, decision):
##        '''Gets the player's choice for the ace value'''
##        return decision

    def __repr__(self):
        if type(self.value) == str:
            return "Card('{}', '{}')".format(self.suit, self.value)
        else:
            return "Card('{}', {})".format(self.suit, self.value)

    def __str__(self):
        return "{} {}".format(self.suit, self.value)

    def __int__(self):
        values = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7,
                  8:8, 9:9, "J":10, "Q": 11, "K":12, "A": 13}
        return values[self.value]


if __name__ == "__main__":
    card_values = {2:2, 3:3, 4:4, 5:5, 6:6, 7:7,
                8:8, 9:9, 10:10, "J": 10, "Q": 11, "K": 13, "A": 14}
    suits = ["Diamond", "Spade", "Heart", "Club"]
    values = [x for x in range(2, 11)] + ["J", "Q", "K", "A"]
    deck = [Card(suit, value) for suit in suits for value in values]
