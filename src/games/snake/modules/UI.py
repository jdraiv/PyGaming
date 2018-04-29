

from modules.fonts.Fontom import Fontom
from ..game_vars import vars


class UI:
    def __init__(self, window):
        self.window = window
        self.fontom = Fontom(self.window)

    def pause_menu(self):
        self.fontom.draw_text(
            text='Game paused',
            font_size=50,
            color=vars['main_blue'],
            hor_center=True,
            ver_center=True,
            )

    def game_over(self):
        self.fontom.draw_text(
            text='GAME OVER',
            font_size=70,
            color=vars['main_red'],
            hor_center=True,
            ver_center=True
        )