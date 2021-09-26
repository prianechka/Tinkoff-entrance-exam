from defines import BOMB, NOT_SET, FLAG

class Solver():
    def __init__(self):
        pass

    def check_cell(value):
        if (value == BOMB):
            return 0
        elif (value == NOT_SET):
            return 1
        else:
            return -1