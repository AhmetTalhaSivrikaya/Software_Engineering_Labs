import unittest
from Logic import BowlingGame

class TestBowling(unittest.TestCase):
    def test_gutter_game(self):
        game = BowlingGame()
        for _ in range(20):
            game.roll(0)
        self.assertEqual(game.score(), 0)

if __name__ == '__main__':
    unittest.main()