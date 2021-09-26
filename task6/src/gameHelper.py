from defines import N_LIMIT, M_LIMIT, BOMB_LIMIT, MENU_LIMIT

# Класс объекта, который общается с игроком и возвращает введённые им данные.
class GameHelper():
   
    def __init__(self):
        pass
    
    def get_mode(self):
        print("Привет! Выберите режим игры: ")
        print("1 - простой режим (поле 5x5), бомб от 2 до 5")
        print("2 - пользовательский режим: самостоятельный выбор количества бомб и размера таблицы")
        print("3 - загрузить игру")
        print("0 - выход из игры")

        result = False
        while (result == False):
            choose = input("Выберите поле: ")
            result = self.check_mode(choose, MENU_LIMIT)
        choose = int(choose)
        return choose

    def check_mode(self, X, LIMIT):
        try:
            X = int(X)
            if (X > LIMIT) or (X < 0):
                print("Некорректный ввод!\nПопробуйте заново!")
                return False
            return True
        except:
            print("Некорректный ввод!\nПопробуйте заново!")
            return False
    
    def check_params(self, X, LIMIT):
        try:
            X = int(X)
            if (X < LIMIT):
                print("Некорректный ввод!\nПопробуйте заново!")
                return False
            return True
        except:
            print("Некорректный ввод!\nПопробуйте заново!")
            return False

    def params_mode(self):
        print("\n")
        result = False
        while (result != True):
            N = input("\nВведите количество строк поля (не меньше 5): ")
            result = self.check_params(N, N_LIMIT)
        N = int(N)

        result = False
        while (result != True):
            M = input('Введите количество столбцов поля(не меньше 5): ')
            result = self.check_params(M, M_LIMIT)
        M = int(M)
       
        result = False
        while (result != True):
            amount_of_bombs = input("Введите количество бомб: (не менее 2): ")
            result = self.check_params(amount_of_bombs, BOMB_LIMIT)
        amount_of_bombs = int(amount_of_bombs)
        return N, M, amount_of_bombs
    
    def start_game(self, N, M, amount_of_bombs):
        print("Игра началась! Поле размером {}x{}, заложено {} бомб".format(N, M, amount_of_bombs))
    
    def get_action(self):
        print("\n\nВведите действие: \n")
        print("Open - открыть ячейку")
        print("Flag - поставить флаг в ячейке")
        print("AI - получить ход от ИИ")
        print("Save - сохранить игру")
        print("Exit - выйти в меню")
        string = input("\nВведите одно из действий: ")
        while (string not in ["Open", "Flag", "Save", "Exit", "AI"]):
            print("Введены некорректные данные! Попробуйте заново")
            string = input("\nВведите одно из действий: ")
        return string

    def check_numbers(self, X, Y, N, M):
        try:
            X = int(X)
            Y = int(Y)
            if (X > N) or (Y > M) or (X <= 0) or (Y <= 0):
                print("Координаты введены некорректно!\nПопробуйте заново!")
                return False
            return True
        except:
            print("Координаты введены некорректно!\nПопробуйте заново!")
            return False

    def get_cell(self, N, M):
        result = False
        while (result == False):
            try:
                X, Y = input("Введите через пробел: X, Y: ").split()
                result = self.check_numbers(X, Y, N, M)
            except:
                print("Координаты введены некорректно!\nПопробуйте заново!")
                result = False
        X, Y = int(X), int(Y)
        X -= 1
        Y -= 1
        return X, Y
    
    def print_decision(self, action, id, M):
        print("\nРешение от AI - {}, клетка - {}, {}!\n".format(action, id // M + 1, id % M + 1))
    
    def get_filename(self):
        string = input("Введите название файла (без расширения): ")
        return string
    
    def bad_filename(self):
        print("Не удалось открыть такой файл. Возможно, название указано неверно.")
    
    def show_total(self, total, amount_of_bombs):
        print("Ваш счёт {}; осталось бомб - {}".format(total, amount_of_bombs))

    def finish_game(self):
        print("К сожалению вы подорвались на бомбе. Gameover.")
        input("Введите что-нибудь, чтобы продолжить игру")
    
    def win_game(self, total):
        print("Поздравляю, вы выиграли! Ваш счёт - {} очков\n".format(total))
        input("Введите что-нибудь, чтобы продолжить игру")

    def congratulations(self):
        print("Поздравляю! Вы - выиграли!\n")
        input("Введите что-нибудь, чтобы продолжить игру")
