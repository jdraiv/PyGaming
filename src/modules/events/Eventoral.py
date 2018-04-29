

# By Jdraiv.

import pygame
import sys

from setup_vars import setup_vars


class Eventoral:
    def exit(self, event):
        if event.type == pygame.QUIT:
            print("Goodbye")
            sys.exit()

    def pause(self, event, pause_letter):
        if event.type == pygame.KEYDOWN:
            if chr(event.key) == pause_letter:
                if not setup_vars['pause']:
                    setup_vars['pause'] = True
                else:
                    setup_vars['pause'] = False

    def restart(self, event, restart_letter):
        if event.type == pygame.KEYDOWN:
            if chr(event.key) == restart_letter:
                setup_vars['pause'] = False
                setup_vars['game_over'] = False

                # Restart app
                setup_vars['restart'] = True
