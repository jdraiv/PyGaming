

# By Jdraiv.

import pygame
import sys

import setup_vars


class Eventoral:
    def exit(self, event):
        if event.type == pygame.QUIT:
            print("Goodbye")
            sys.exit()

    def pause(self, event, pause_letter):
        if event.type == pygame.KEYDOWN:
            if chr(event.key) == pause_letter:
                if not setup_vars.pause:
                    setup_vars.pause = True
                else:
                    setup_vars.pause = False