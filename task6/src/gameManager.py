from numpy import matrix
from gameKeeper import GameKeeper
from solver import Solver

class GameManager():
    def __init__(self, mode):
        self.mode = mode
        self.keeper = GameKeeper()
    
    def create_game(self, N = 5, M = 5, amounts_of_bombs = None):
        self.keeper.set_N(N)
        self.keeper.set_M(M)
        if (self.mode == 1):
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
    
    def check_win(self):
        amount = self.get_amount_of_bombs()
        total = self.get_total()
        N, M = self.keeper.get_M(), self.keeper.get_N()
        if (amount == 0) or (N * M - total - amount == 0):
            return True
        else:
            return False
    
    def get_sizes(self):
        return self.keeper.get_N(), self.keeper.get_M()
    
    def get_matrix(self):
        return self.keeper.get_matrix()
    
    def create_matrix_for_AI(self):
        matrix = self.keeper.get_matrix()
    
    def load_game(self, n, m, matrix, total, amount):
        self.keeper.load_game(n, m, matrix, total, amount)
        self.keeper.show_table()