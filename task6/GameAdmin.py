from numpy import matrix
from GameHelper import GameHelper
from GameManager import GameManager
from loader import Loader
from saver import Saver
from Shower import Shower
from GameAI import AI
import os

class GameAdmin():

    def __init__(self):
        self.helper = GameHelper()
        self.havemanager = 0
    
    def start_game(self):
        mode = self.helper.get_mode()
        if (mode == 0):
            exit()
        elif (mode == 1 or mode == 2):
            self.manager = GameManager(mode)
            self.havemanager = 1
            if (mode == 2):
                N, M, amount_of_bombs = self.helper.params_mode()
            else:
                N, M, amount_of_bombs = 5, 5, None
            self.manager.create_game(N, M, amount_of_bombs)
            amount_of_bombs = self.manager.get_amount_of_bombs()
            self.helper.start_game(N, M, amount_of_bombs)
            self.manager.show_game()
            self.play()
        elif (mode == 3):
            filename = self.helper.get_filename()
            N, M, matrix, total, amount = Loader().load(filename)
            if (N is None):
                self.helper.bad_filename()
            else:
                self.manager = GameManager(mode = 2)
                self.havemanager = 1
                self.manager.load_game(N, M, matrix, total, amount)
                self.play()
    
    def play(self):
        res = self.manager.check_win()
        if (res == True):
            total = self.manager.get_total()
            self.helper.win_game(total)
            self.finish()
        else:
            total = self.manager.get_total()
            amount_of_bombs = self.manager.get_amount_of_bombs()
            self.helper.show_total(total, amount_of_bombs)
            N, M = self.manager.get_sizes()
            action = self.helper.get_action()
            if (action == "Save"):
                filename = self.helper.get_filename()
                N, M = self.manager.get_sizes()
                matrix = self.manager.get_matrix()
                total = self.manager.get_total()
                amount = self.manager.get_amount_of_bombs()
                Saver().save(filename, N, M, matrix, total, amount)
                self.play()
            elif (action == "Exit"):
                self.start_game()
            elif (action == "AI"):
                N, M = self.manager.get_sizes()
                matrix = self.manager.get_matrix()
                new_matrix = Shower().create_matrix(matrix)
                action, id = AI().predict(N, M, new_matrix)
                self.helper.print_decision(action, id, M)
                self.play()
            else:
                x, y, = self.helper.get_cell(N, M)
                if (action == "Open"):
                    result = self.manager.player_set_cell(x, y)
                    if (result == 0):
                        self.manager.show_game()
                        self.play()
                    elif (result == -1):
                        self.play()
                    else:
                        self.helper.finish_game()
                        self.finish()
                elif (action == "Flag"):
                    self.manager.player_set_flag(x, y)
                    self.manager.show_game()
                    self.play()
        
    def finish(self):
        self.manager = None
        self.havemanager = 0
        self.start_game()