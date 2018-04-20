
import pygame
from modules.events.Eventoral import Eventoral

"""
The body of the snake is implemented as a list. The segments are implemented as a sub_list inside the body list
The sub_list needs to contain the X and Y position
of the snake segment. Example: [x_pos, y_pos]
"""


class App:
    def __init__(self, window):
        self.window = window
        self.snake_body = [[480, 480]]
        self.snake_size = 20
        self.events_class = Eventoral()

    def draw_snake(self):
        pygame.draw.rect(self.window, [250, 250, 250], [480, 480, 20, 20])

    def events(self):
        for event in pygame.event.get():
            self.events_class.exit(event)

    def snake_movement(self):
        pass

    def container(self):
        self.draw_snake()
        self.events()

