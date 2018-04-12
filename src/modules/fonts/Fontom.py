

# By Jdraiv.

import pygame


class Fontom:
    def __init__(self, screen):
        self.screen = screen

    def horizontal_center(self, text):
        c_font = pygame.font.SysFont('Comic Sans MS', 30)

        text_object = c_font.render(text, False, (0, 0, 0))

        self.screen.blit(text_object, (100, 100))

    def vertical_center(self, h):
        pass





