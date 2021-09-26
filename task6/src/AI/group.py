from cell import Cell

class Group():

    def __init__(self, bombs):
        self.list = []
        self.bombs = bombs
    
    def __len__(self):
        return len(self.get_list())
    
    def get_bombs(self):
        return self.bombs
    
    def get_list(self):
        return self.list
    
    def set_list(self, list):
        self.list = list
    
    def set_bombs(self, bombs):
        self.bombs = bombs

    def append(self, cell):
        self.list.append(cell)
    
    def check_equal(self, another_group):
        result = True
        list1, list2 = self.get_list(), another_group.get_list()
        if (len(list1) != len(list2)):
            result = False
        else: 
            for i in range(len(list1)):
                if (list1[i] not in list2):
                    result = False
                    break
        return result
    
    def check_in(self, another_group):
        result = True
        list1, list2 = self.get_list(), another_group.get_list()
        if (len(list2) > len(list1)):
            result = False
        else:
            for i in range(len(list2)):
                if (list2[i] not in list1):
                    result = False
                    break
        return result
    
    def check_intersect(self, another_group):
        result = False
        list1, list2 = self.get_list(), another_group.get_list()
        for i in range(len(list2)):
            if (list2[i] in list1):
                result = True
                break
        return result
    
    def substract_group(self, another_group):
        self.bombs -= another_group.get_bombs()
        self.list = list(set(self.get_list()) - set(another_group.get_list()))
    
    def change_group(self, another_group):
        list1, list2 = self.get_list(), another_group.get_list()
        bomb1, bomb2 = self.get_bombs(), another_group.get_bombs()
        list_of_new_group = list(set(list1).union(set(list2)))
        new_bombs = 0
        if (bomb1 >= bomb2):
            new_bombs = bomb1 - (len(list2) - len(list_of_new_group))
        else:
            new_bombs = bomb2 - (len(list1) - len(list_of_new_group))
        
        if (new_bombs != min(bomb1, bomb2)):
            return False, self, another_group, None
        else:
            new_group = Group(new_bombs)
            new_group.set_list(list_of_new_group)
            self.substract_group(new_group)
            another_group.substract_group(new_group)
            return True, self, another_group, new_group