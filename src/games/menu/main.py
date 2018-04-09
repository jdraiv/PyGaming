
import re
import os
from glob import glob


# This class helps the user select the game the user wants to play
class App:
    def __init__(self, screen):
        self.screen = screen
        self.games_list = self.get_games()

    def show_menu(self):
        self.screen.fill([150, 150, 150])

    def get_games(self):
        # Return the name of app
        def get_f_name(s, exp):
            return filter(None, re.split("[%s]+" % exp, s))[-1]

        dir = "%s/games/" % os.getcwd()
        data = glob("%s*/" % dir)

        result = [get_f_name(folder, "/") for folder in data]
        return result

    def container(self):
        print(self.games_list)
        self.show_menu()


test = "hai"
