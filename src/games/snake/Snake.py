
import pygame
from .game_vars import vars


class Snake:
    def __init__(self, window, apple_pos):
        self.window = window
        self.apple_pos = apple_pos
        self.segment_size = vars['segment_size']
        self.snake_body = [[480, 480], [0, 0]]
        self.current_direction = 'left'

    def draw_snake(self):
        self.window.fill((0, 0, 0))

        for sub_list in self.snake_body:
            pygame.draw.rect(self.window, [250, 250, 250], [sub_list[0], sub_list[1], self.segment_size, self.segment_size])

    def snake_controller(self, event):
        def valid_direction(current_direction, new_direction):
            result = False
            x, y = ['left', 'right'], ['up', 'down']

            if new_direction == 'left' or new_direction == 'right':
                if current_direction not in x:
                    result = True
            else:
                if current_direction not in y:
                    result = True

            return result

        values = {'a': 'left', 'd': 'right', 'w': 'up', 's': 'down'}

        if event.type == pygame.KEYDOWN:
            current_value = chr(event.key)

            if current_value in values and current_value != self.current_direction:
                if valid_direction(self.current_direction, values[current_value]):
                    self.current_direction = values[current_value]

    def apple_collision(self):
        if self.snake_body[0][0] == self.apple_pos[0] and self.snake_body[0][1] == self.apple_pos[1]:
            self.snake_body.append([0, 0])
            return True

    def tail_collision(self):
        if self.snake_body[0] in self.snake_body[1:]:
            print("Collision")

    def border_collision(self):
        w, h = pygame.display.get_surface().get_size()

        head_pos = self.snake_body[0]

        if head_pos[0] > w:
            self.snake_body[0][0] = 0
        elif head_pos[0] < 0:
            self.snake_body[0][0] = w
        elif head_pos[1] > h:
            self.snake_body[0][1] = 0
        elif head_pos[1] < 0:
            self.snake_body[0][1] = h

    def snake_movement(self):
        # Update head position.
        def head_update(direction, positions_list, seg_size):
            neg_movement = ['left', 'up']
            pos_movement = ['right', 'down']

            # Creating new list to avoid variable mutation
            new_list = positions_list[:]

            if direction in neg_movement:
                new_list[neg_movement.index(direction)] -= seg_size
            else:
                new_list[pos_movement.index(direction)] += seg_size
            return new_list

        def tail_movement(positions_list):
            # Start with the value of the first element in the list
            segment_old_pos = positions_list[0]

            for list_index, sub_list in enumerate(positions_list):
                if list_index > 0:
                    # Set value of the left neighbor segment
                    positions_list[list_index] = segment_old_pos
                    # Store old value of the segment
                    segment_old_pos = sub_list

            return positions_list

        # Update snake body using the old head position.
        tail_movement(self.snake_body)

        # Set the new head position.
        self.snake_body[0] = head_update(self.current_direction, self.snake_body[0], self.segment_size)

        self.tail_collision()
        self.border_collision()