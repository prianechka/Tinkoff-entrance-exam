
# Класс объекта, который общается с игроком и возвращает введённые им данные.
class GameHelper():
   
    def __init__(self):
        pass
    
    def get_mode(self):
        print("Привет! Выберите режим игры: ")
        print("1 - простой режим (поле 5x5), бомб от 2 до 5")
        print("2 - пользовательский режим: самостоятельный выбор количества бомб и размера таблицы")
        choose = int(input("Выберите поле: ")) - 1 # Пока без исключений и проверок ввода
        return choose
    
    def params_mode(self):
        print("\n")
        N = int(input("Введите количество строк поля (не меньше 5): "))
        M = int(input('Введите количество столбцов поля(не меньше 5): '))
        amount_of_bombs = int(input("Введите количество бомб: (не менее 2): "))
        return N, M, amount_of_bombs
    
    def start_game(self, N, M, amount_of_bombs):
        print("Игра началась! Поле размером {}x{}, заложено {} бомб".format(N, M, amount_of_bombs))

    def get_cell(self):
        print("Введите через пробел: X, Y, Action (0 - открыть, 1 - поставить флаг)")
        X, Y, Action = map(int, input().split())
        return X, Y, Action
    
    def show_total(self, total, amount_of_bombs):
        print("Ваш счёт {}; осталось бомб - {}".format(total, amount_of_bombs))

    def finish_game(self):
        print("К сожалению вы подорвались на бомбе. Gameover.")
        input("Введите что-нибудь, чтобы продолжить игру")

    def congratulations(self):
        print("Поздравляю! Вы - выиграли!")
        input("Введите что-нибудь, чтобы продолжить игру")
