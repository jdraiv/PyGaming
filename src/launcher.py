

import sys, pygame


"""
The Launcher class. The big boss. This class returns the initial screen in which a game is going to be rendered.
This class also contains some functions that affect the game rendering process, like FPS.
"""


"""
In order for a game to be read correctly by the launcher, the game needs to be on his own folder.
The folder needs to contain a file called "main". The launcher is going to take the "main" file as the main/important 
file like his namesake.
"""


class Launcher:
    def __init__(self):
        self.screen = pygame.display.set_mode([200, 200])
        self.current_app = 'menu'

    def set_caption(self):
        pygame.display.set_caption(self.current_app)

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Goodbye")
                    sys.exit()

            self.set_caption()
            self.screen.fill([20,20,20])
            pygame.display.update()


Launcher().start()
