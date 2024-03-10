from pathlib import Path

class GameStats:
    '''Track statistics for Alien Invasion'''

    def __init__(self, ai_game):
        '''Initalize statistics.'''
        self.settings = ai_game.settings
        self.reset_stats()

        # High score and level should never be reset. 
        path = Path('highscore.txt')
        if path.exists():
            contents = path.read_text()
            self.high_score = int(contents)
        else:
            self.high_score = 0

        path = Path('highestlevel.txt')

        if path.exists():
            contents = path.read_text()
            self.highest_level = int(contents)
        else:
            self.highest_level = 0
    
    def reset_stats(self):
        '''Intialize statistics that can change during the game.'''
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
