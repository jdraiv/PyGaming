

from modules.fonts.Fontom import Fontom
from .game_vars import vars


class UI:
    def __init__(self, window):
        self.window = window
        self.fontom_class = Fontom(self.window)

    def pause_menu(self):
        self.fontom_class.draw_text(text='Game paused.', color=vars['main_blue'], font_size=50, hor_center=True, ver_center=True)