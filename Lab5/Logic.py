class BowlingGame:
    def __init__(self):
        self._total_score = 0

    def roll(self, pins):

        self._total_score += pins

    def score(self):

        return self._total_score