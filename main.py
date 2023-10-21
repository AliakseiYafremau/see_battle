from random import choice, shuffle

# ship - O
# misflit - x
#
# 1 - OOO
# 2 - OO
# 4 - O
#
#     0 1 2 3 4 5
#   + - - - - - - +
# 0 | O         O |
# 1 | O     O     |
# 2 | O           |
# 3 |       O   O |
# 4 |             |
# 5 | O O   O O   |
#   + - - - - - - +


class Dot:
    def __init__(self, is_missed=False, does_have_ship=False):
        self.is_missed = is_missed
        self.does_have_ship = does_have_ship

    def lives_of_ship(self):
        if self.does_have_ship:
            return self.does_have_ship.lives
        return 0


class Ship:
    def __init__(self, length, coordinates=[]):
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

    def clear(self):
        self.field = []
        for i in range(self.length):
            self.field.append([])
            for j in range(self.length):
                self.field[i].append(Dot())

    def output(self):
        row = 0
        res =  '     0 1 2 3 4 5   \n'
        res += '   + - - - - - - + \n'
        res += ' 0 | {} {} {} {} {} {} | \n'.format(*map(self.translater, self.field[row]))
        row += 1
        res += ' 1 | {} {} {} {} {} {} | \n'.format(*map(self.translater, self.field[row]))
        row += 1
        res += ' 2 | {} {} {} {} {} {} | \n'.format(*map(self.translater, self.field[row]))
        row += 1
        res += ' 3 | {} {} {} {} {} {} | \n'.format(*map(self.translater, self.field[row]))
        row += 1
        res += ' 4 | {} {} {} {} {} {} | \n'.format(*map(self.translater, self.field[row]))
        row += 1
        res += ' 5 | {} {} {} {} {} {} | \n'.format(*map(self.translater, self.field[row]))
        res += '   + - - - - - - + \n'
        return res

    @staticmethod
    def translater(el):
        if el.is_missed:
            return 'X'
        if el.does_have_ship:
            return 'O'
        else:
            return ' '

    def can_be_stayed_ship(self, row, column):
        if not self.does_dot_exist(row, column):
            return False
        if self.is_dot_occupied(row, column):
            return False
        if self.is_something_near(row, column):
            return False
        return True

    def create_random_board(self):
        for el in self.create_ships(1, 3):
            self.living_ships.append(el)
        for el in self.create_ships(2, 2):
            self.living_ships.append(el)
        for el in self.create_ships(4, 1):
            self.living_ships.append(el)
        while True:
            out = self.put_all_ships()
            if out:
                break
            else:
                self.clear()

    def put_all_ships(self):
        is_filled = True
        for i in range(len(self.living_ships)):
            if not self.does_exist_not_occupied_dot():
                is_filled = False
                break
            vacant_dots = self.give_list_of_not_occupied_dot()
            while vacant_dots:
                dot = choice(vacant_dots)
                if self.living_ships[i].length == 1:
                    self.living_ships[i].coordinates = [dot]
                    self.put_ship([[dot[0], dot[1]]], self.living_ships[i])
                    break
                if self.living_ships[i].length > 1:
                    interval = self.living_ships[i].length - 1
                    possible_directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
                    shuffle(possible_directions)
                    direction = possible_directions.pop() # [-1, 0]
                    coordinates = [[dot[0] + direction[0]*l, dot[1] + direction[1]*l] for l in range(1, interval+1)]
                    coordinates.append([dot[0], dot[1]])
                    self.living_ships[i].coordinates.append(coordinates)
                    if all([self.can_be_stayed_ship(dot[0] + direction[0]*l, dot[1] + direction[1]*l) for l in range(1, interval+1)]):
                        self.put_ship(coordinates, self.living_ships[i])
                        break
        return is_filled

    def put_ship(self, dots, ship): # dots - двойной список с row и column
        for dot in dots:
            self.field[dot[0]][dot[1]].does_have_ship = ship

    def give_list_of_not_occupied_dot(self):
        result = []
        for row in range(len(self.field)):
            for col in range(len(self.field[row])):
                if self.can_be_stayed_ship(row, col):
                    result.append([row, col])
        return result

    @staticmethod
    def create_ships(count, length):
        ships = [Ship(length) for i in range(count)]
        return ships

    def does_exist_not_occupied_dot(self):
        for row in range(len(self.field)):
            for col in range(len(self.field[row])):
                if self.can_be_stayed_ship(row, col):
                    return True
        return False

    def is_all_ships_destroyed(self):
        pass

    def is_dot_occupied(self, row, column):
        if not self.field[row][column].does_have_ship:
            return False
        return True

    def does_dot_exist(self, row, column):
        if row < 0 or row >= self.length or column < 0 or column >= self.length:
            return False
        return True

    def is_something_near(self, row, column):

        #         +---------+-----+---------+
        #         | col - 1 |  col | col + 1 |
        # row - 1 |         |      |         |
        # row     |         | ship |         |
        # row + 1 |         |      |         |
        #         +---------+-----+---------+

        for near_row in range(row - 1, row + 2):
            for near_col in range(column - 1, column + 2):
                if near_row == row and near_col == column:
                    continue
                if self.does_dot_exist(near_row, near_col):
                    if self.is_dot_occupied(near_row, near_col):
                        return True
        return False


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
        self.first_player.board.create_random_board()
        self.second_player.board.create_random_board()
        print(self.first_player.board.output())
        print(self.second_player.board.output())

    def start(self):
        self.greet()

        self.loop()


f_p = User()
s_p = AI()
game = Game(f_p, s_p)

game.start()
