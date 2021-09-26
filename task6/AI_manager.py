from group import Group
from cell import Cell

class AImanager():

    def __init__(self, N, M, matrix):
        self.N = N
        self.M = M
        self.matrix = matrix
        self.list_of_groups = []
        self.list_shape = 0
        self.prob_matrix = []
    
    def set_N(self, N):
        self.N = N
    
    def set_M(self, M):
        self.M = M

    def set_matrix(self, matrix):
        self.matrix = matrix
    
    def set_list_shape(self, number):
        self.list_shape = number

    def check_cell(self, i, j):
        return self.matrix[i][j]
    
    def check_bottom_cell(self, i, j, group):
        val = self.check_cell(i + 1, j)
        if (val == 'X'):
            cell = Cell((i + 1) * self.M + j)
            group.append(cell)
        elif (val == 'F'):
            group.set_bombs(group.get_bombs() - 1)
        return group
    
    def check_up_cell(self, i, j, group):
        val = self.check_cell(i - 1, j)
        if (val == 'X'):
            cell = Cell((i - 1) * self.M + j)
            group.append(cell)
        elif (val == 'F'):
            group.set_bombs(group.get_bombs() - 1)
        return group
    def check_left_cell(self, i, j, group):
        val = self.check_cell(i, j - 1)
        if (val == 'X'):
            cell = Cell(i * self.M + (j - 1))
            group.append(cell)
        elif (val == 'F'):
            group.set_bombs(group.get_bombs() - 1)
        return group
    
    def check_right_cell(self, i, j, group):
        val = self.check_cell(i, j + 1)
        if (val == 'X'):
            cell = Cell(i * self.M + (j + 1))
            group.append(cell)
        elif (val == 'F'):
            group.set_bombs(group.get_bombs() - 1)
        return group
    
    def check_up_right_cell(self, i, j, group):
        val = self.check_cell(i - 1, j + 1)
        if (val == 'X'):
            cell = Cell((i - 1) * self.M + (j + 1))
            group.append(cell)
        elif (val == 'F'):
            group.set_bombs(group.get_bombs() - 1)
        return group
    
    def check_up_left_cell(self, i, j, group):
        val = self.check_cell(i - 1, j - 1)
        if (val == 'X'):
            cell = Cell((i - 1) * self.M + (j - 1))
            group.append(cell)
        elif (val == 'F'):
            group.set_bombs(group.get_bombs() - 1)
        return group
    
    def check_bottom_left_cell(self, i, j, group):
        val = self.check_cell(i + 1, j - 1)
        if (val == 'X'):
            cell = Cell((i + 1) * self.M + (j - 1))
            group.append(cell)
        elif (val == 'F'):
            group.set_bombs(group.get_bombs() - 1)
        return group
    
    def check_bottom_right_cell(self, i, j, group):
        val = self.check_cell(i + 1, j + 1)
        if (val == 'X'):
            cell = Cell((i + 1) * self.M + (j + 1))
            group.append(cell)
        elif (val == 'F'):
            group.set_bombs(group.get_bombs() - 1)
        return group
     
    def create_group(self, matrix, i, j):
        group = Group(matrix[i][j])
        if (i == 0 and j == 0):
            group = self.check_bottom_cell(i, j, group)
            group = self.check_right_cell(i, j, group)
            group = self.check_bottom_right_cell(i, j, group)
        elif ((i == 0) and (j > 0) and (j + 1 < self.M)):
            group = self.check_bottom_cell(i, j, group)
            group = self.check_right_cell(i, j, group)
            group = self.check_bottom_right_cell(i, j, group)
            group = self.check_bottom_left_cell(i, j, group)
            group = self.check_left_cell(i, j, group)
        elif (i == 0 and (j + 1 == self.M)):
            group = self.check_bottom_cell(i, j, group)
            group = self.check_bottom_left_cell(i, j, group)
            group = self.check_left_cell(i, j, group)
        elif ((i > 0) and (i + 1 < self.N) and (j + 1 == self.M)):
            group = self.check_bottom_cell(i, j, group)
            group = self.check_bottom_left_cell(i, j, group)
            group = self.check_left_cell(i, j, group)
            group = self.check_up_left_cell(i, j, group)
            group = self.check_up_cell(i, j, group)
        elif ((i > 0) and (i + 1 < self.N) and (j == 0)):
            group = self.check_bottom_cell(i, j, group)
            group = self.check_bottom_right_cell(i, j, group)
            group = self.check_right_cell(i, j, group)
            group = self.check_up_right_cell(i, j, group)
            group = self.check_up_cell(i, j, group)
        elif (((i + 1) == self.N) and j == 0):
            group = self.check_up_cell(i, j, group)
            group = self.check_right_cell(i, j, group)
            group = self.check_up_right_cell(i, j, group)
        elif (((i + 1) == self.N) and (j > 0) and ((j + 1) < (self.M))):
            group = self.check_up_cell(i, j, group)
            group = self.check_right_cell(i, j, group)
            group = self.check_up_right_cell(i, j, group)
            group = self.check_up_left_cell(i, j, group)
            group = self.check_left_cell(i, j, group)
        elif (((i + 1) == self.N) and (j + 1 == self.M)):
            group = self.check_up_cell(i, j, group)
            group = self.check_up_left_cell(i, j, group)
            group = self.check_left_cell(i, j, group)
        else:
            group = self.check_bottom_cell(i, j, group)
            group = self.check_bottom_right_cell(i, j, group)
            group = self.check_bottom_left_cell(i, j, group)

            group = self.check_up_cell(i, j, group)
            group = self.check_up_right_cell(i, j, group)
            group = self.check_up_left_cell(i, j, group)

            group = self.check_left_cell(i, j, group)
            group = self.check_right_cell(i, j, group)
        return group
    
    def create_list(self):
        for i in range(self.N):
            for j in range(self.M):
                if (self.matrix[i][j] != 'X') and (self.matrix[i][j] != 'F'):
                    self.list_of_groups.append(self.create_group(self.matrix, i, j))
        self.set_list_shape(len(self.list_of_groups))
    
    def change_list(self):
        result = 0
        i = 0
        while i < self.list_shape - 1:
            j = i + 1
            while j < self.list_shape:
                group1, group2 = self.list_of_groups[i], self.list_of_groups[j]
                if (group1.check_equal(group2) == True):
                    self.list_of_groups.pop(j)
                    self.list_shape -= 1
                elif (group1.check_in(group2) == True):
                    group1.substract_group(group2)
                elif (group2.check_in(group1) == True):
                    group2.substract_group(group1)
                elif (group1.check_intersect(group2) == True):
                    res, group_1, group_2, group_3 = group1.change_group(group2)
                    if (res == True):
                        result += 1
                        self.list_of_groups[i] = group_1
                        self.list_of_groups[j] = group_2
                        self.list_of_groups.append(group_3)
                        self.list_shape += 1
                j += 1
            i += 1
        return result
    
    def find_groups(self):
        result = self.change_list()
        while (result > 0):
            result = self.change_list()
            print(result)
    
    def make_right_decision(self):
        for i in range(self.list_shape):
            group = self.list_of_groups[i]
            if (group.get_bombs() == 0):
                if (len(group) > 0):
                    return "Open", group.get_list()[0].get_id()
            elif (group.get_bombs() == len(group.get_list())):
                if (len(group) > 0):
                    return "Flag", group.get_list()[0].get_id()
        return "None", -1

    def make_matrix_probability(self):
        self.prob_matrix = [[0] * self.M for i in range(self.N)]
        for i in range(self.N):
            for j in range(self.M):
                self.prob_matrix[i][j] = list()
        self.create_list()
        for i in range(self.list_shape):
            group = self.list_of_groups[i].get_list()
            if (len(group) > 0):
                koeff = self.list_of_groups[i].get_bombs() / len(group)
                for j in range(len(group)):
                    cell = group[j].get_id()
                    x, y = cell // self.M, cell % self.M
                    self.prob_matrix[x][y].append(koeff)
        
        for i in range(self.N):
            for j in range(self.M):
                arr = self.prob_matrix[i][j]
                pr = 1
                for t in range(len(arr)):
                    pr *= (1 - arr[t])
                if (pr < 1):
                    self.prob_matrix[i][j] = 1 - pr
                else:
                    self.prob_matrix[i][j] = 1
                
    def correct_probs(self):
        corr = 0
        for i in range(self.list_shape):
            group = self.list_of_groups[i].get_list()
            bomb = self.list_of_groups[i].get_bombs()
            sum_prob = 0
            for j in range(len(group)):
                cell = group[j].get_id()
                x, y = cell // self.M, cell % self.M
                val = self.prob_matrix[x][y]
                sum_prob += val
            if (sum_prob > 0):
                koef = bomb / sum_prob
                corr += (1 - koef)
                for j in range(len(group)):
                    cell = group[j].get_id()
                    x, y = cell // self.M, cell % self.M
                    self.prob_matrix[x][y] *= koef
        
        return corr
    
    def change_probs(self):
        corr = 1
        while (corr >= 0.05):
            corr = self.correct_probs()
    
    def make_prob_decision(self):
        min_val = 1
        min_i, min_j = 0, 0
        for i in range(self.N):
            for j in range(self.M):
                val = self.prob_matrix[i][j]
                if (val < min_val):
                    min_val = val 
                    min_i, min_j = i, j
        return min_i * self.M + min_j


N = 4
M = 3
matrix = [['X', 'X', 'X'], 
          ['X',  4,  'X'], 
          ['X',  2,  'X'],
          ['X', 'X', 'X']]

AI = AImanager(N, M, matrix)
AI.make_matrix_probability()
AI.change_probs()
print(AI.make_prob_decision())
'''
AI.create_list()
for i in range(AI.list_shape):
    for j in range(len(AI.list_of_groups[i])):
        print(AI.list_of_groups[i].get_list()[j].get_id(), end = ', ')
    print(":", AI.list_of_groups[i].get_bombs())
print("------------------")

AI.find_groups()
for i in range(AI.list_shape):
    for j in range(len(AI.list_of_groups[i])):
        print(AI.list_of_groups[i].get_list()[j].get_id(), end = ', ')
    print(":", AI.list_of_groups[i].get_bombs())
print(AI.make_right_decision())

matr = [[[]] * M for i in range(N)]
print(matr)
'''