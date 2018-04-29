
import pygame
from modules.events.Eventoral import Eventoral

from .modules.Snake import Snake
from .modules.Apple import Apple
from .modules.UI import UI
from setup_vars import setup_vars
from .game_vars import vars

"""
The body of the snake is implemented as a list. The segments are implemented as a sub_list inside the body list
The sub_list needs to contain the X and Y position
of the snake segment. Example: [x_pos, y_pos]
"""


class App:
    def __init__(self, window):
        self.window = window
        self.apple_class = Apple(self.window)
        self.snake_class = Snake(self.window, self.apple_class.apple_pos)
        self.ui_class = UI(self.window)
        self.events_class = Eventoral()

    def events(self):
        for event in pygame.event.get():
            # Listen to events in the snake module
            self.snake_class.snake_controller(event)

            # Exit window event
            self.events_class.exit(event)
            # Pause event
            self.events_class.pause(event, 'p')
            # Restart event
            self.events_class.restart(event, 'r')

    def set_vars(self):
        setup_vars['time'] = 25

    def container(self):
        self.set_vars()
        self.events()

        if not setup_vars['pause']:
            self.snake_class.snake_movement()
            self.snake_class.draw_snake()

            self.ui_class.draw_score()

            # Check if the apple is eaten
            if self.snake_class.apple_collision():
                # Set new apple position
                self.apple_class.set_position()
                self.snake_class.apple_pos = self.apple_class.apple_pos

                # Add point to score
                vars['score'] += 1

            # Check snake collision
            if self.snake_class.tail_collision():
                setup_vars['pause'] = True
                setup_vars['game_over'] = True

            self.apple_class.draw_apple()
        elif setup_vars['game_over']:
            self.ui_class.game_over()
        else:
            self.ui_class.pause_menu()

