from defines import BOMB, FLAG, NOT_SET

class Shower():
    def __init__(self):
        pass
    
    def create_matrix(self, matrix):
        N, M = len(matrix), len(matrix[0])
        new_matr = [[0] * M for i in range(N)]
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == FLAG:
                    new_matr[i][j] = 'F'
                elif matrix[i][j] == NOT_SET or matrix[i][j] == BOMB:
                    new_matr[i][j] = 'X'
                else:
                    new_matr[i][j] = matrix[i][j]
        return new_matr
    
    def show_matrix(self, old_matrix):
        matrix = self.create_matrix(old_matrix)
        print("\nТекущая карта:")
        N, M = len(matrix), len(matrix[0])
        print("   ", end = '')
        for i in range(1, M + 1):
            print(" {} ".format(i), end = '')
        print("\n" + "---" * (M + 1))
        for i in range(N):
            print("{} |".format(i + 1), end = '')
            for j in range(M):
                    print(" {} ".format(matrix[i][j]), end ='')
            print("|")
        print()