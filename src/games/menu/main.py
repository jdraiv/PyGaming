
import os
from glob import glob


# This class helps the user select the game the user wants to play
class App:
    def __init__(self, screen):
        self.screen = screen

    def show_menu(self):
        self.screen.fill([150, 150, 150])

    def get_games(self):
        cwd = "%s/games/" % os.getcwd()
        data = glob("%s*/" % cwd)
        print(data)

    def container(self):
        self.get_games()
        self.show_menu()


test = "hai"
