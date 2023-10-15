class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Ship:
    def __init__(self, length, bow, direction, lives):
        self.dots = []
        self.length = length
        self.bow = bow
        self.direction = direction
        self.lives = lives

    def add_dot(self, dot):
        self.dots.append(dot)

    def get_dots(self):
        return self.dots


class Board:
    def __init__(self, hidden, length=6):
        self.field = []
        self.ships = []
        self.hidden = hidden
        self.living_ships = []
        self.length = length

    def add_ship(self, ship):
        self.ships.append(ship)

    def contour(self): # Обводит корабль по контуру. Он будет полезен и в ходе самой игры, и в при расстановке кораблей (помечает соседние точки, где корабля по правилам быть не может).
        pass

    def print_to_consol(self): # выводит доску в консоль в зависимости от параметра hid.
        pass

    def is_dot_out(self, dot):
        if dot.x >= self.length or dot.y >= self.length or dot.x < 0 or dot.y < 0:
            return True
        return False

    def shoot(self, x, y):
        pass


class Player: # класс игрока
    def __init__(self):
        self.own_board = Board(False) # создания собственного поля
        self.enemy_board = Board(True) # создание вражеского поля

    def ask(self):
        pass

    def move(self):
        pass

class User(Player):
    def ask(self):
        pass

class AI(Player):
    def ask(self):
        pass


class Game:
    def __init__(self, first_player, second_player):
        self.first_player = first_player
        #self.first_player_board = first_player_board
        self.second_player = second_player
        #self.second_player_board = second_player_board

    def random_board(self):
        pass

    def greet(self):
        greeting = 'Морской бой'
        greeting += '\nПравила: ...\n'
        return greeting # возвращаем строку приветствия

    def loop(self): # игровой цикл
        pass

    def start(self): # запуск игры
        print(self.greet()) # приветствуем игрока

        self.loop()


first_player = User()
second_player = AI()

game = Game(first_player, second_player)

game.start()

