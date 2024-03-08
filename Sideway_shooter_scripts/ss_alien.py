import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''A Class to represent a single alien in the fleet.'''
    
    def __init__(self, ss_game):
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # Load the alien image and set its rect settings. 
        self.original_image = pygame.image.load('images/alien.bmp')
        self.rotated_image = pygame.transform.rotate(self.original_image, -90)
        self.image = self.rotated_image
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top right. 
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height 

        # Store the alien's exact horizontal position. 
        self.x = float(self.rect.x)

    def check_edges(self):
        '''Return True if alien is at the edge of screen.'''
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        '''Move the alien right or left.'''
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    
    