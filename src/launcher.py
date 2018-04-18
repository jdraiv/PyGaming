

import os
import sys
import pygame



"""
The Launcher class. The big boss. This class returns the initial screen in which a game is going to be rendered.
This class also contains some functions that affect the game rendering process, like FPS.
"""


"""
In order for a game to be read correctly by the launcher, the game needs to be on his own folder.
The folder needs to contain a file called "main". The launcher is going to take the "main" file as the main/important 
file like his namesake. The game needs to be inside a class called 'App'. You need to bundle all the application code
inside a function called "container".
"""


class Launcher:
    def __init__(self):
        self.window = pygame.display.set_mode([500, 500])
        self.current_app = 'menu'
        self.game = self.read_app().App(self.window)

    def set_caption(self):
        pygame.display.set_caption(self.current_app.capitalize())

    # This function imports and return the file as an object that can be called
    def read_app(self):
        module = __import__('games.%s.main' % self.current_app, globals(), locals(), ['App'], 0)
        return module

    def start(self):
        # Initialize fonts
        pygame.font.init()

        while True:

            self.set_caption()
            self.game.container()

            pygame.display.update()


Launcher().start()
