import pygame

class Ship:
    '''A class to manage the ship.'''
    
    def __init__(self, ss_game):
        '''Intialize the ship and set its starting position'''
        self.screen = ss_game.screen
        self.screen_rect = ss_game.screen.get_rect()
        self.settings = ss_game.settings

        # Load the ship and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Rotate the ship image 90 degrees clockwise
        self.image = pygame.transform.rotate(self.image, -90)

        # Start each new ship at the bottom center of the screen.
        self.rect.midleft = self.screen.get_rect().midleft
        # Store a float for the ship's exact horizontal position.
        self.y = float(self.rect.y)
        
        # Movement flags; start with a ship that's not moving.
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        '''Update the ship's position based on movement flags.'''
        # Update the ship's x value, not the rect
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update the rect object from self.x.
        self.rect.y = self.y

    def blitme(self):
        '''Draw the ship at its current location.'''
        self.screen.blit(self.image, self.rect)
    
   
