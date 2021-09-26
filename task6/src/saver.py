import pickle

class Saver():

    def __init__(self):
        pass

    def save(self, filename, N, M, matrix, total, amount):
        with open("savings/" + filename + '.pickle', 'wb') as f:
            data = {
                "total":total,
                "amount":amount,
                "N":N,
                "M":M,
                "matrix":matrix
            }
            pickle.dump(data, f)