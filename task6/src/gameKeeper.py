from defines import BOMB, FLAG, NOT_SET
import numpy as np
from gameTable import GameTable
from shower import Shower

class GameKeeper():
    
    def __init__(self, N = 0, M = 0, amount_of_bombs = 0):
        self.N = N
        self.M = M
        self.amount_of_bombs = amount_of_bombs
        self.count_celles = 0
        self.play = 0
    
    def set_amount_bombs(self, amount_of_bombs):
        self.amount_of_bombs = amount_of_bombs
    
    def get_amount_bombs(self):
        return self.amount_of_bombs
    
    def set_N(self, N):
        self.N = N
    
    def set_M(self, M):
        self.M = M
    
    def get_N(self):
        return self.N
    
    def get_M(self):
        return self.M
    
    def choose_amount_bombs(self, A, B):
        self.amount_of_bombs = int(np.random.randint(A, B + 1, 1))
    
    def set_bombs(self):
        array = [i for i in range(self.M * self.N)]
        choice = np.random.choice(array, size = self.amount_of_bombs, replace=False)
        for i in range(self.amount_of_bombs):
            self.game.set_bomb(choice[i] // self.M, choice[i] % self.M)
 
    def create_game(self):
        self.game = GameTable(self.N, self.M)
        self.set_bombs()
        self.count_celles = 0
    
    def start_game(self):
        self.play = 1

    def check_cell(self, i, j):
        if (self.play == 1):
            return self.game.get_cell(i, j)
    
    def check_bottom_cell(self, i, j):
        if (self.game.get_cell(i + 1, j) == BOMB):
            return 1
        else:
            return 0
    
    def check_up_cell(self, i, j):
        if (self.game.get_cell(i - 1, j) == BOMB):
            return 1
        else:
            return 0
    
    def check_left_cell(self, i, j):
        if (self.game.get_cell(i, j - 1) == BOMB):
            return 1
        else:
            return 0
    
    def check_right_cell(self, i, j):
        if (self.game.get_cell(i, j + 1) == BOMB):
            return 1
        else:
            return 0
    
    def check_up_right_cell(self, i, j):
        if (self.game.get_cell(i - 1, j + 1) == BOMB):
            return 1
        else:
            return 0
    
    def check_up_left_cell(self, i, j):
        if (self.game.get_cell(i - 1, j - 1) == BOMB):
            return 1
        else:
            return 0
    
    def check_bottom_left_cell(self, i, j):
        if (self.game.get_cell(i + 1, j - 1) == BOMB):
            return 1
        else:
            return 0
    
    def check_bottom_right_cell(self, i, j):
        if (self.game.get_cell(i + 1, j + 1) == BOMB):
            return 1
        else:
            return 0
    
    def count_bombs_around(self, i, j):
        if (self.play == 1):
            result = 0
            if (i == 0 and j == 0):
                result += self.check_bottom_cell(i, j)
                result += self.check_right_cell(i, j)
                result += self.check_bottom_right_cell(i, j)
            elif ((i == 0) and (j > 0) and (j + 1 < self.M)):
                result += self.check_bottom_cell(i, j)
                result += self.check_right_cell(i, j)
                result += self.check_bottom_right_cell(i, j)
                result += self.check_bottom_left_cell(i, j)
                result += self.check_left_cell(i, j)
            elif (i == 0 and (j + 1 == self.M)):
                result += self.check_bottom_cell(i, j)
                result += self.check_bottom_left_cell(i, j)
                result += self.check_left_cell(i, j)
            elif ((i > 0) and (i + 1 < self.N) and (j + 1 == self.M)):
                result += self.check_bottom_cell(i, j)
                result += self.check_bottom_left_cell(i, j)
                result += self.check_left_cell(i, j)
                result += self.check_up_left_cell(i, j)
                result += self.check_up_cell(i, j)
            elif ((i > 0) and (i + 1 < self.N) and (j == 0)):
                result += self.check_bottom_cell(i, j)
                result += self.check_bottom_right_cell(i, j)
                result += self.check_right_cell(i, j)
                result += self.check_up_right_cell(i, j)
                result += self.check_up_cell(i, j)
            elif (((i + 1) == self.N) and j == 0):
                result += self.check_up_cell(i, j)
                result += self.check_right_cell(i, j)
                result += self.check_up_right_cell(i, j)
            elif (((i + 1) == self.N) and (j > 0) and ((j + 1) < (self.M))):
                result += self.check_up_cell(i, j)
                result += self.check_right_cell(i, j)
                result += self.check_up_right_cell(i, j)
                result += self.check_up_left_cell(i, j)
                result += self.check_left_cell(i, j)
            elif (((i + 1) == self.N) and (j + 1 == self.M)):
                result += self.check_up_cell(i, j)
                result += self.check_up_left_cell(i, j)
                result += self.check_left_cell(i, j)
            else:
                result += self.check_bottom_cell(i, j)
                result += self.check_bottom_right_cell(i, j)
                result += self.check_bottom_left_cell(i, j)

                result += self.check_up_cell(i, j)
                result += self.check_up_right_cell(i, j)
                result += self.check_up_left_cell(i, j)

                result += self.check_left_cell(i, j)
                result += self.check_right_cell(i, j)
            return result
    
    def set_table_shooted(self, i, j):
        if self.play:
            value = self.game.get_cell(i, j)
            if (value == NOT_SET) or (value == FLAG):
                self.count_celles += 1
            amount_bombs_around = self.count_bombs_around(i, j)
            self.game.set_shooted(i, j, amount_bombs_around)
    
    def set_table_flag(self, i, j):
        if self.play:
            value = self.game.get_cell(i, j)
            if (value == NOT_SET or value == BOMB):
                self.game.set_flag(i, j)
    
    def show_table(self):
        if self.play:
            Shower().show_matrix(self.game.get_matrix())
    
    def get_total(self):
        return self.count_celles
    
    def get_matrix(self):
        return self.game.get_matrix()
    
    def finish_game(self):
        self.game = None
        self.play = 0
    
    def load_game(self, N, M, matrix, total, amount):
        self.set_N(N)
        self.set_M(M)
        self.set_amount_bombs(amount)
        self.count_celles = total
        self.game = GameTable(self.N, self.M)
        self.game.set_matrix(matrix)
        self.play = 1