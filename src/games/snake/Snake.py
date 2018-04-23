
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
        if event.type == pygame.KEYDOWN:
            if event.key == 97:
                self.current_direction = 'left'
            elif event.key == 100:
                self.current_direction = 'right'
            elif event.key == 119:
                self.current_direction = 'up'
            elif event.key == 115:
                self.current_direction = 'down'

    def apple_collision(self):
        if self.snake_body[0][0] == self.apple_pos[0] and self.snake_body[0][1] == self.apple_pos[1]:
            self.snake_body.append([0, 0])
            return True

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