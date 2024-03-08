import sys
import pygame
from settings2 import Settings
from ship2 import Ship
from bullet2 import Bullet
from ss_alien import Alien

class SidewayShooter:
    '''Overall class to manage game assets and behavior.'''

    def __init__(self):
        '''Intialize the game, and create game resources.'''
        pygame.init()
        '''Set frame rate'''
        self.clock = pygame.time.Clock()
        '''Makes an instance of Settings in the project.'''
        self.settings = Settings()

        '''Set screen size'''
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideway Shooter")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        self.aliens = pygame.sprite.Group()  # Create a group for aliens

        self._create_fleet()  # Call the method to create the alien fleet

    def run_game(self):
        '''Start the main loop for the game.'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
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
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

    def _check_keyup_events(self, event):
        '''Respond to keyreleases'''
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _fire_bullet(self):
        '''Create a new bullet and add it to the bullets group.'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    def _update_bullets(self):
        '''Update position of bullets and get rid of old bullets.'''
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared. 
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.settings.screen_width:
                self.bullets.remove(bullet)
            
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        '''Repsond to bullet-alien collisions.'''
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)
        if not self.aliens:
            # Destroy exisiting bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
    def _update_aliens(self):
        '''Check if the fleet is at an edge, then update positions.'''
        self._check_fleet_edges()
        self.aliens.update()

    def _create_fleet(self):
        '''Create the fleet of aliens.'''
        # Create an alien and keep adding aliens until there's no room left. 
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien.rect.size
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row; reset x value, and increment y value. 
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        '''Create an alien and place it in the fleet.'''
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
    
    def _check_fleet_edges(self):
        '''Respond appropriately if any aliens have reached an edge.'''
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        '''Drop the entire fleet and change the fleet's direction.'''
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
               
    def _update_screen(self):
        '''Update images on the screen, and flip to the new screen.'''
        self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ss = SidewayShooter()
    ss.run_game()