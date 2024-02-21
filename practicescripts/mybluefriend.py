import sys
import pygame
from alien_friend import Alien

class Blue_guy:
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Intialize the game, and create game resources.'''
        pygame.init()
        '''Set frame rate'''
        self.clock = pygame.time.Clock()
    
        '''Set screen size'''

        # set the background color
        self.bg_color = (64,64,64)

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Little Blue Alien")
        self.alien_friend = Alien(self)

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self.clock.tick(60)
            '''Respond to keypresses and mouse events.'''
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
       
            
  
            '''Update images on the screen, and flip to the new screen.'''
            self.screen.fill(self.bg_color)
            self.alien_friend.blitme()

            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    alien = Blue_guy()
    alien.run_game()
