#Author: Kevin C. Escobedo
#Email: escobedo001@gmail.com
from blackjack_logic import Blackjack
import unittest

class BlackjackTests(unittest.TestCase):
    def setUp(self):
        self.game = Blackjack()

    def test_game_set_up_properly(self):
        self.assertEqual(len(self.game.deck), 52)
        self.assertEqual(len(self.game.player_hand), 0)
        self.assertEqual(len(self.game.comp_hand), 0)

    def test_hit(self):
        for i in range(4):
            self.game.hit()
        self.assertEqual(len(self.game.player_hand), 2)
        self.assertEqual(len(self.game.comp_hand), 2)
        self.assertEqual(len(self.game.deck), 48)

if __name__ == "__main__":
    unittest.main()
