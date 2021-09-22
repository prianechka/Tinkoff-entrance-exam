from GameKeeper import GameKeeper
from Solver import Solver

class GameManager():
    def __init__(self, mode):
        self.mode = mode
        self.keeper = GameKeeper()
    
    def create_game(self, N = 5, M = 5, amounts_of_bombs = None):
        self.keeper.set_N(N)
        self.keeper.set_M(M)
        if (self.mode == 0):
            self.keeper.choose_amount_bombs(2, 5)
        else:
            self.keeper.set_amount_bombs(amounts_of_bombs)
        self.keeper.create_game()
        self.keeper.start_game()
    
    def show_game(self):
        self.keeper.show_table()
    
    def player_set_flag(self, i, j):
        self.keeper.set_table_flag(i, j)
    
    def player_set_cell(self, i, j):
        result = 0
        if (Solver.check_cell(self.keeper.check_cell(i, j))):
            self.keeper.set_table_shooted(i, j)
        else:
            self.keeper.finish_game()
            result = 1
        return result
    
    def get_total(self):
        return self.keeper.get_total()
    
    def get_amount_of_bombs(self):
        return self.keeper.get_amount_bombs()