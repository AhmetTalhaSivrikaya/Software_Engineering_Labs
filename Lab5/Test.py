import unittest
from Logic import BowlingGame

class TestBowling(unittest.TestCase):
    def test_gutter_game(self):
        game = BowlingGame()
        for _ in range(20):
            game.roll(0)
        self.assertEqual(game.score(), 0)

    def test_all_ones(self):
        game = BowlingGame()
        for _ in range(20):
            game.roll(1)
        self.assertEqual(game.score(), 20)
    def test_one_spare(self):
        game = BowlingGame()
        game.roll(5)
        game.roll(5) 
        game.roll(3) 
        for _ in range(17):
            game.roll(0)
        self.assertEqual(game.score(), 16)



if __name__ == '__main__':
    unittest.main()