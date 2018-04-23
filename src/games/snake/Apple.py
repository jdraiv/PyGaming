

import pygame
import random
from .game_vars import vars


class Apple:
    def __init__(self, window):
        self.window = window
        self.apple_size = vars['segment_size']
        self.apple_pos = self.random_pos()

    def random_pos(self):
        positions = []

        for c in range(2):
            positions.append(vars['segment_size'] * (random.randint(0, vars['segment_size'])))

        return positions

    def set_position(self):
        self.apple_pos = self.random_pos()

    def draw_apple(self):
        pygame.draw.rect(self.window, [239, 62, 62], [self.apple_pos[0], self.apple_pos[1], 20, 20])
