import pygame
import sys
from raindrop import Raindrop


class RainyDay:
    '''Overall class to manange the game assets'''
    def __init__(self):
        '''Initialize the rainyday'''
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        self.display.set_caption("Rainy Day")

    def run_game(self):
        """Start the main loop of the game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
    
    def check_events():
        for event in pygame.event():
            if pygame.event == pygame.QUIT:
                sys.exit()

if __name__ == '__main__':
    rd = RainyDay()
    rd.run_game
