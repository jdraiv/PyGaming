
from setup_vars import setup_vars


class Controller:
    def set_window(self, width=500, height=500):
        setup_vars['window_width'], setup_vars['window_height'] = width, height

    def restart_game(self):
        # If the game is already in restart mode, then proceed to deactivate that mode
        if setup_vars['restart']:
            setup_vars['restart'] = False
        else:
            setup_vars['restart'] = True

