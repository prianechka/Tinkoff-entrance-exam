import pickle

class Loader():

    def __init__(self):
        pass

    def load(self, filename):
        try:
            with open("savings/" + filename + '.pickle', 'rb') as f:
                data_new = pickle.load(f)
                total = data_new["total"]
                amount = data_new["amount"]
                N = data_new["N"]
                M = data_new["M"]
                matrix = data_new["matrix"]
            return N, M, matrix, total, amount
        except:
            return None, None, None, None, None
