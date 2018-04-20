

import pygame
import random


class Apple:
    def __init__(self, window):
        self.window = window

    def random_pos(self):
        pass

    def draw_apple(self):
        self.window.draw.rect(self.window, [250, 250, 2500], [100, 100, 20, 20])
        return

