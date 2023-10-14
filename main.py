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
    def __init__(self, hidden, length):
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


class Player:
    def __init__(self, own_board, enemy_board):
        self.own_boars = own_board
        self.enemy_board = enemy_board

    def ask(self):
        pass

    def move(self):
        pass

class User(Player):
    pass

class AI(Player):
    pass


class Game:
    def __int__(self, player, player_board, enemy, enemy_board):
        self.player = player
        self.player_board = player_board
        self.enemy = enemy
        self.enemy_board = enemy_board

    def random_board(self):
        pass

    def greet(self):
        pass

    def loop(self):
        pass

    def start(self):
        pass

