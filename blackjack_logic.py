#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
from card_class import Card

class Blackjack:
    def __init__(self):
        self.suits = ["Heart", "Diamond", "Spade", "Club"]
        self.values = [x for x in range(2, 11)] + ["J", "Q", "K", "A"]
        self.deck = [Card(x, y) for x in self.suits for y in self.values]



if __name__ == "__main__":
    b = Blackjack()
