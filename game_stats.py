import os

import constants

class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game) -> None:
        self.settings = ai_game.settings
        # High score shouldn't be reset
        self.set_high_score()
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def set_high_score(self):
        """Retrieves the high score from a file if it exists"""
        if os.path.isfile(constants.HIGH_SCORE_FILE):
            self.high_score = int(open(constants.HIGH_SCORE_FILE).read())
        else:
            self.high_score = 0
