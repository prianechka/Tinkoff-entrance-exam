from GameHelper import GameHelper
from GameManager import GameManager

class GameAdmin():

    def __init__(self):
        self.helper = GameHelper()
        self.havemanager = 0
    
    def start_game(self):
        mode = self.helper.get_mode()
        self.manager = GameManager(mode)
        self.havemanager = 1
        if (mode == 1):
            N, M, amount_of_bombs = self.helper.params_mode()
        else:
            N, M, amount_of_bombs = 5, 5, None
        self.manager.create_game(N, N, amount_of_bombs)
        amount_of_bombs = self.manager.get_amount_of_bombs()
        self.helper.start_game(N, M, amount_of_bombs)
        self.play()
    
    def play(self):
        total = self.manager.get_total()
        amount_of_bombs = self.manager.get_amount_of_bombs()
        self.helper.show_total(total, amount_of_bombs)
        x, y, action = self.helper.get_cell()
        if (action == 0):
            result = self.manager.player_set_cell(x, y)
            if (result == 0):
                self.manager.show_game()
                self.play()
            else:
                self.helper.finish_game()
                self.manager = None
                self.havemanager = 0
                self.start_game()
        elif (action == 1):
            self.manager.player_set_flag(x, y)
            self.play()