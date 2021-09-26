from AI_manager import AImanager

class AI():
    
    def __init__(self):
        pass

    def predict(self, N, M, matrix):
        self.manager = AImanager(N, M, matrix)
        self.manager.create_list()
        self.manager.find_groups()
        action, id = self.manager.make_right_decision()
        if (action == "None"):
            action = "Open"
            self.manager.create_list()
            self.manager.make_matrix_probability()
            print(self.manager.prob_matrix)
            self.manager.change_probs()
            id = self.manager.make_prob_decision()
        
        return action, id