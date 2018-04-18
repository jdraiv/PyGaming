
import json
import os
import pygame
import sys


# Font Module
from modules.fonts.Fontom import Fontom
# Events modules
from modules.events.Eventoral import Eventoral


# This class helps the user select the game the user wants to play
class App:
    def __init__(self, screen):
        self.screen = screen
        self.games = self.get_games()
        self.fontom = Fontom(self.screen)
        self.events = Eventoral()
        self.current_game_num = 0

    def show_menu(self):
        self.screen.fill([55, 56, 68])

        self.fontom.draw_text('PyEngine', font_size=80, pos_y=50, hor_center=True)

        self.fontom.draw_text('Select Game', font_size=50, pos_y=340, hor_center=True)

        self.fontom.draw_text("< %s >" % self.games[self.current_game_num], font_size=30, pos_y=400, hor_center=True)

    def controller(self):
        for event in pygame.event.get():
            self.events.exit(event)

    def change_game(self):
        if self.current_game_num <= len(self.games):
            self.current_game_num = 0
        else:
            self.current_game_num += 1

    def get_games(self):
        location = "%s/games/games.json" % os.getcwd()
        games = json.load(open(location, 'r'))

        return [dic['name'] for dic in games['games']]

    def container(self):
        self.show_menu()
        self.controller()
