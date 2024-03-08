import sys
import pygame
from pygame.sprite import Sprite

class Settings:
    """A class to store all settings for the game."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.target_color = (255, 0, 0)
        self.target_width = 20
        self.target_height = 100
        self.target_speed = 1

        self.ship_speed = 1.5
        self.ship_width = 20
        self.ship_height = 50
        self.ship_color = (0, 0, 255)

        self.bullet_speed = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        self.play_button_color = (0, 255, 0)
        self.play_button_width = 100
        self.play_button_height = 50

class Target(Sprite):
    """A class to represent the target."""

    def __init__(self, ai_game):
        """Initialize the target and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Create a target rectangle at the right edge of the screen.
        self.rect = pygame.Rect(0, 0, self.settings.target_width, self.settings.target_height)
        self.rect.midright = self.screen.get_rect().midright

        # Store the target's vertical position.
        self.y = float(self.rect.y)

    def update(self):
        """Move the target up and down."""
        self.y += self.settings.target_speed
        self.rect.y = self.y

        # Reverse the direction when the target reaches the top or bottom.
        if self.rect.top <= 0 or self.rect.bottom >= self.screen.get_rect().bottom:
            self.settings.target_speed *= -1

    def draw(self):
        """Draw the target to the screen."""
        pygame.draw.rect(self.screen, self.settings.target_color, self.rect)

class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Create a ship rectangle on the left side of the screen.
        self.rect = pygame.Rect(0, 0, self.settings.ship_width, self.settings.ship_height)
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the ship's vertical position.
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship's position based on movement flags."""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Update rect object from self.y.
        self.rect.y = self.y

    def draw(self):
        """Draw the ship to the screen."""
        pygame.draw.rect(self.screen, self.settings.ship_color, self.rect)

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Create a bullet rectangle at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midright = ai_game.ship.rect.midright

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet across the screen."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)

class PlayButton:
    """A class to manage the play button."""

    def __init__(self, ai_game, msg):
        """Initialize the play button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = ai_game.settings.play_button_width, ai_game.settings.play_button_height
        self.button_color = ai_game.settings.play_button_color
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

class Game:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        # Set up the screen.
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Target Practice")

        # Create an instance of the target, ship, bullets, and play button.
        self.target = Target(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.play_button = PlayButton(self, "Play")

        # Flag to track whether the game is active.
        self.game_active = False
        self.miss_count = 0

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self.target.update()

            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            if not self.game_active:
                self._start_game()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        if not self.game_active:
            button_clicked = self.play_button.rect.collidepoint(mouse_pos)
            if button_clicked:
                self._start_game()

    def _start_game(self):
        """Start the game."""
        # Reset the game statistics.
        self.miss_count = 0
        self.game_active = True

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.bullets.remove(bullet)
                self.miss_count += 1
                if self.miss_count >= 3:
                    self.game_active = False
                    self.miss_count = 0
                    pygame.mouse.set_visible(True)

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.target.draw()
        self.ship.draw()
        for bullet in self.bullets.sprites():
            bullet.draw()

        # Draw the play button if the game is inactive.
        if not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    # Create a game instance and run the game.
    game = Game()
    game.run_game()
