
import pygame
from modules.events.Eventoral import Eventoral

from .Snake import Snake
from .Apple import Apple
from .UI import UI
import setup_vars

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
            self.snake_class.snake_controller(event)

            # Exit window event
            self.events_class.exit(event)
            self.events_class.pause(event, 'p')

    def set_vars(self):
        setup_vars.time = 25

    def container(self):
        self.set_vars()
        self.events()

        if not setup_vars.pause:
            self.snake_class.snake_movement()
            self.snake_class.draw_snake()

            # Check if the apple is eaten
            if self.snake_class.apple_collision():
                # Set new apple position
                self.apple_class.set_position()
                self.snake_class.apple_pos = self.apple_class.apple_pos

            self.apple_class.draw_apple()
        else:
            self.ui_class.pause_menu()

