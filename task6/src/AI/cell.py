class Cell():
    def __init__(self, id, probabilty = 0):
        self.id = id
        self.probability = probabilty
    
    def set_id(self, id):
        self.id = id
    
    def set_probability(self, probabilty):
        self.probability = probabilty
    
    def get_id(self):
        return self.id

    def get_probabilty(self):
        return self.probability
    
    def get_list_prob(self):
        return self.list_prob
    
    def __eq__(self, other):
        result = False
        if (self.get_id() == other.get_id()):
            result = True
        return result
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __hash__(self):
        return hash(self.id)