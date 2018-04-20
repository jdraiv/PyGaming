
import json
import os
import pygame
import sys


# Font Module
from modules.fonts.Fontom import Fontom
# Events modules
from modules.events.Eventoral import Eventoral

import setup_vars


# This class helps the user select the game the user wants to play
class App:
    def __init__(self, screen):
        self.screen = screen
        self.games = self.get_games()
        self.fontom = Fontom(self.screen)
        self.current_game_num = 0

    def show_menu(self):
        self.screen.fill([55, 56, 68])

        self.fontom.draw_text('PyEngine', font_size=80, pos_y=50, hor_center=True)

        self.fontom.draw_text('Select Game', font_size=50, pos_y=340, hor_center=True)

        self.fontom.draw_text("< %s >" % self.games[self.current_game_num], font_size=30, pos_y=400, hor_center=True)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == 97 or event.key == 276:
                    self.current_game_num -= 1
                elif event.key == 100 or event.key == 275:
                    self.current_game_num += 1
                elif event.key == 32:
                    setup_vars.current_game = self.games[self.current_game_num]
                    print("Play")

                # Update current_game index value
                self.validate_game_num()

            Eventoral().exit(event)

    def validate_game_num(self):
        if self.current_game_num == len(self.games):
            self.current_game_num = 0
        elif self.current_game_num < 0:
            self.current_game_num = len(self.games) - 1

    def get_games(self):
        location = "%s/games/games.json" % os.getcwd()
        games = json.load(open(location, 'r'))

        return [dic['name'] for dic in games['games']]

    def container(self):
        self.show_menu()
        self.events()
