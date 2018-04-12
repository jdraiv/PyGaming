
import json
import os

# Font Module
from modules.fonts.Fontom import Fontom


# This class helps the user select the game the user wants to play
class App:
    def __init__(self, screen):
        self.screen = screen
        self.games = self.get_games()

    def show_menu(self):
        self.screen.fill([150, 150, 150])
        Fontom(self.screen).horizontal_center('Testing')

    def get_games(self):
        location = "%s/games/games.json" % os.getcwd()
        games = json.load(open(location, 'r'))

        return [dic['name'] for dic in games['games']]

    def container(self):
        self.show_menu()
