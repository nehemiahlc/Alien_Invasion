import sys
import pygame
from rocket import Rocket

class RocketShip:
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Intialize the game, and create game resources.'''
        pygame.init()
        '''Set frame rate'''
        self.clock = pygame.time.Clock()

        '''Set screen size'''
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Rocket")

        self.bg_color = (255,255,255)
        
        self.rocket = Rocket(self)

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(60)
           

    def _check_events(self):
        '''Respond to keypresses and mouse events.'''      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    def _check_keydown_events(self, event):
        '''Respond to keypresses.'''
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
    def _check_keyup_events(self, event):
        '''Respond to keyreleases'''
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
        elif event.key == pygame.K_q: # Adding 'Pressing Q to quit'
            sys.exit()
    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen.'''
        self.screen.fill(self.bg_color)
        self.rocket.blitme()

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ro = RocketShip()
    ro.run_game()
