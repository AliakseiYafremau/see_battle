class Dot:
    def __init__(self, is_missed=False, does_have_ship=False):
        self.is_missed = is_missed
        self.does_have_ship = does_have_ship

    def lives_of_ship(self):
        if self.does_have_ship:
            return self.does_have_ship.lives
        return 0


class Ship:
    def __init__(self, length, coordinates):
        self.length = length
        self.coordinates = coordinates
        self.lives = length


class Board:
    def __init__(self, length=6):
        self.length = length
        self.field = []
        for i in range(length):
            self.field.append([])
            for j in range(length):
                self.field[i].append(Dot())
        self.living_ships = []

    def can_be_stayed_ship(self, row, column):
        if not self.does_dot_exist(row, column):
            return False
        if self.is_dot_occupied(row, column):
            return False
        return True

    def create_random_board(self):
        pass

    def is_all_ships_destroyed(self):
        pass

    def is_dot_occupied(self, row, column):
        if not self.field[row][column].does_have_ship:
            return True
        return False

    def does_dot_exist(self, row, column):
        if row < 0 or row >= self.length or column < 0 or column >= self.length:
            return False
        return True


class Player:
    def __init__(self):
        self.board = Board()

    def ask(self):
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
        self.second_player = second_player

    @staticmethod
    def greet():
        greeting = "Морской бой\n"
        greeting += "Правила игры:\n"
        greeting += "Игрок должен уничтожить все корабли соперника, раньше его\n"

    def loop(self):
        pass

    def start(self):
        self.greet()

        self.loop()


f_p = User()
s_p = AI()
game = Game(f_p, s_p)

game.start()