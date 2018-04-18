

# By Jdraiv.

import pygame
import sys


class Eventoral:
    def exit(self, event):
        if event.type == pygame.QUIT:
            print("Goodbye")
            sys.exit()

    