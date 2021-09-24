from defines import BOMB, FLAG, NOT_SET

class Shower():
    def __init__(self):
        pass

    def show_matrix(self, matrix):
        print("\nТекущая карта:")
        N, M = len(matrix), len(matrix[0])
        print("   ", end = '')
        for i in range(1, M + 1):
            print(" {} ".format(i), end = '')
        print("\n" + "---" * (M + 1))
        for i in range(N):
            print("{} |".format(i + 1), end = '')
            for j in range(M):
                if matrix[i][j] == FLAG:
                    print(" F ", end ='')
                elif matrix[i][j] == NOT_SET or matrix[i][j] == BOMB:
                    print(" X ", end = '')
                else:
                    print(" " + str(matrix[i][j]) + " ", end = '')
            print("|")
        print()