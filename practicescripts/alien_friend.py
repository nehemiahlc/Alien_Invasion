import pygame

class Alien:
    '''A class to manage the ship.'''
    
    def __init__(self, alien_game):
        '''Intialize the alien to the center position'''
        self.screen = alien_game.screen
        self.screen_rect = alien_game.screen.get_rect()

        # Load the ship and get its rect.
        self.image = pygame.image.load('/Users/nehemiahchandler/Downloads/alien_blue/blue__0000_idle_1.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)

        
    