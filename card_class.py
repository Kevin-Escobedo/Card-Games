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
