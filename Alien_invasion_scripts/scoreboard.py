import pygame.font
from pygame.sprite import Group

from ship import Ship
from pathlib import Path 

class Scoreboard:
    '''A class to report scoring information.'''

    def __init__(self, ai_game):
        '''Intialize scorekeeping attributes.'''
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.prep_ships()

        # Font settings for scoring information. 
        self.text_color = (0, 0, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image. 
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_highest_level()
    
    def prep_level(self):
        '''Turn the level into a rendered image.'''
        level_str = f"Level: {self.stats.level}"

        self.level_image = self.font.render(level_str, True, self.text_color,
            self.settings.bg_color)
        
        # Position the level below the score. 
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_ships(self):
        '''Show how many ships are left.'''
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_score(self):
        '''Turn the score into a rendered image.'''
        rounded_score = round(self.stats.score, -1)
        score_str = f"Score: {rounded_score:,}"
        self.score_image = self.font.render(score_str, True, 
                self.text_color, self.settings.bg_color)
        
        # Display the score at the top right of the screen. 
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def prep_high_score(self):
        '''Turn the high score into a rendered image.'''
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"High Score: {high_score:,}"
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color)
        
        # Center the high score at the top of the screen. 
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx - 200
        self.high_score_rect.top = self.score_rect.top
    
    def prep_highest_level(self):
        '''Turn the highest level into a rendered image.'''
        highest_level = self.stats.highest_level
        highest_level_str = f"Highest Level: {highest_level:,}"
        self.highest_level_image = self.font.render(highest_level_str, True,
                self.text_color, self.settings.bg_color)
        
        # Center the highest level at the top of the screen next to high score. 
        self.highest_level_rect = self.high_score_image.get_rect()
        self.highest_level_rect.centerx = self.screen_rect.centerx + 200
        self.highest_level_rect.top = self.score_rect.top

    
    def show_score(self):
        '''Draw scores and level and ships to the screen.'''
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.highest_level_image, self.highest_level_rect)
        self.ships.draw(self.screen)
    
    def check_high_score(self):
        '''Check to see if there's a new high score.'''
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def check_highest_level(self):
        '''Check to see if there's a new highest level.'''
        if self.stats.level > self.stats.highest_level:
            self.stats.highest_level = self.stats.level
            self.prep_highest_level()

    def write_high_score_to_file(self):
        '''Adds highscore to a file so it is saved after restarts.'''
        high_score = round(self.stats.high_score, -1)
        path = Path('highscore.txt')
        path.write_text(str(high_score))
    
    def write_highest_level_to_file(self):
        '''Adds highscore to a file so it is saved after restarts.'''
        highest_level = self.stats.highest_level
        path = Path('highestlevel.txt')
        path.write_text(str(highest_level))


