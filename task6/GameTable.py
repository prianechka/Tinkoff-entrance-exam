from numpy import matrix
from defines import BOMB, FLAG, NOT_SET

class GameTable():
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.matrix = [[NOT_SET] * self.N for i in range(self.M)]
    
    def set_bomb(self, i, j):
        self.matrix[i][j] = BOMB
    
    def set_flag(self, i, j):
        self.matrix[i][j] = FLAG

    def set_shooted(self, i, j, N):
        self.matrix[i][j] = N
    
    def set_matrix(self, matrix):
        self.matrix = matrix
    
    def get_matrix(self):
        return self.matrix
    
    def get_sizes(self):
        return self.N, self.M
    
    def get_cell(self, i, j):
        return self.matrix[i][j]
