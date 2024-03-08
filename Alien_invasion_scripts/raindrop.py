import pygame
from pygame.sprite import Sprite

class Raindrop(Sprite):

    def __init__(self, rd_game):
        super().__init__()
        self.screen = rd_game.screen
        self.settings = rd_game.settings
        # Load the rain image and set its rect attribute. 
        self.image = pygame.image.load('images/raindrop.bmp')
        self.rect = self.image.get_rect()

        # Start each new raindrop near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the rain's exact vertical position.
        self.y = float(self.rect.y)

    def check_edges(self):
        '''Return True if rain is at the bottom of screen.'''
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom)

    def update(self):
        '''Move the rain down.'''
        self.y += self.settings.rain_speed * self.settings.raindrop_direction
        self.rect.y = self.y
    