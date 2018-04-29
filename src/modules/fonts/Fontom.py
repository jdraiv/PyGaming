

# By Jdraiv.

import pygame


class Fontom(object):
    def __init__(self, window, font_family='Lorem Ipsum'):
        self.window = window
        self.font_family = font_family

    def draw_text(self, text, color=[255, 255, 255], pos_x=0, pos_y=0, font_size=30, hor_center=False, ver_center=False):
        # This function checks if an object needs to be centered, if not, returns the normal position.
        def should_center(pos, w_size, bool):
            if bool:
                return w_size / 2
            else:
                return pos

        font = pygame.font.SysFont(self.font_family, font_size, True)
        text_obj = font.render(text, True, color)
        window_size = pygame.display.get_surface().get_size()

        # Set text element.
        text_rect = text_obj.get_rect(center=(
            should_center(pos_x, window_size[0], hor_center),
            should_center(pos_y, window_size[1], ver_center)))

        # Draw text
        self.window.blit(text_obj, text_rect)





