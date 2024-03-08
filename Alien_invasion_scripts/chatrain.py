import pygame
import sys
from pygame.sprite import Sprite

class Raindrop(Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/raindrop.bmp')
        self.image = pygame.transform.scale(self.image, (30, 30))  # Resize the image
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def update(self):
        self.rect.y += 1

class RainyDay:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Rainy Day")
        self.raindrops = pygame.sprite.Group()
        self._create_raindrops()

    def _create_raindrops(self):
        raindrop = Raindrop(self.screen)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.screen_width - (2 * raindrop_width)
        number_raindrops_x = available_space_x // (2 * raindrop_width)
        available_space_y = self.screen_height - (2 * raindrop_height)
        number_rows = available_space_y // (2 * raindrop_height)

        for row_number in range(number_rows):
            for raindrop_number in range(number_raindrops_x):
                self._create_raindrop(raindrop_number, row_number)

    def _create_raindrop(self, raindrop_number, row_number):
        raindrop = Raindrop(self.screen)
        raindrop_width, raindrop_height = raindrop.rect.size
        raindrop.x = raindrop_width + 2 * raindrop_width * raindrop_number
        raindrop.rect.x = raindrop.x
        raindrop.rect.y = raindrop.rect.height + 2 * raindrop.rect.height * row_number
        self.raindrops.add(raindrop)

    def run_game(self):
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_raindrops(self):
        self.raindrops.update()
        for raindrop in self.raindrops.copy():
            if raindrop.rect.top >= self.screen_height:
                self.raindrops.remove(raindrop)
                self._create_new_row()
    
    def _create_new_row(self):
        raindrop = Raindrop(self.screen)
        raindrop_width, raindrop_height = raindrop.rect.size
        available_space_x = self.screen_width - (2 * raindrop_width)
        number_raindrops_x = available_space_x // (2 * raindrop_width)

        for raindrop_number in range(number_raindrops_x):
            self._create_raindrop(raindrop_number, 0)

    def _update_screen(self):
        self.screen.fill((255, 255, 255))
        self.raindrops.draw(self.screen)
        pygame.display.flip()

if __name__ == '__main__':
    rd = RainyDay()
    rd.run_game()
