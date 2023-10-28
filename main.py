from random import choice, shuffle
from time import sleep

# ship - O
# misfit - T
# destroyed part of ship - X
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
        self.is_destroyed_part = False
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
        self.destroyed_ships = []

    def shoot(self, row, column):
        if self.field[row][column].does_have_ship and not self.field[row][column].is_destroyed_part:
            self.field[row][column].does_have_ship.lives -= 1
            self.field[row][column].is_destroyed_part = True
        else:
            self.field[row][column].is_missed = True


    def clear(self):
        self.field = []
        for i in range(self.length):
            self.field.append([])
            for j in range(self.length):
                self.field[i].append(Dot())

    def output(self, hide=False):
        row = 0
        res =  '     0 1 2 3 4 5   \n'
        res += '   + - - - - - - + \n'
        res += ' 0 | {} {} {} {} {} {} | \n'.format(*map(self.translater, self.field[row], [hide for i in range(6)]))
        row += 1
        res += ' 1 | {} {} {} {} {} {} | \n'.format(*map(self.translater, self.field[row], [hide for i in range(6)]))
        row += 1
        res += ' 2 | {} {} {} {} {} {} | \n'.format(*map(self.translater, self.field[row], [hide for i in range(6)]))
        row += 1
        res += ' 3 | {} {} {} {} {} {} | \n'.format(*map(self.translater, self.field[row], [hide for i in range(6)]))
        row += 1
        res += ' 4 | {} {} {} {} {} {} | \n'.format(*map(self.translater, self.field[row], [hide for i in range(6)]))
        row += 1
        res += ' 5 | {} {} {} {} {} {} | \n'.format(*map(self.translater, self.field[row], [hide for i in range(6)]))
        res += '   + - - - - - - + '
        return res

    @staticmethod
    def translater(el, hidden=False):
        if el.is_missed:
            return 'T'
        if el.is_destroyed_part:
            return 'X'
        if el.does_have_ship and not hidden:
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
            shuffle(vacant_dots)
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

    def give_list_of_dot_for_player(self):
        result = []
        for row in range(len(self.field)):
            for col in range(len(self.field[row])):
                if self.can_be_shooted_by_player(row, col):
                    result.append([row, col])
        return result

    def can_be_shooted_by_player(self, row, column):
        for near_row in range(row - 1, row + 2):
            for near_col in range(column - 1, column + 2):
                if near_row == row and near_col == column:
                    if self.field[near_row][near_col].is_missed or self.field[near_row][near_col].is_destroyed_part:
                        return False
                elif self.does_dot_exist(near_row, near_col):
                    if self.field[near_row][near_col].does_have_ship:
                        if not self.field[near_row][near_col].lives_of_ship():
                            return False
        return True

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
        if not self.living_ships:
            return True
        return False

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
        self.enemy = False


class User(Player):
    def ask(self):
        print('Ваш ход.')
        print('Ваша доска: ')
        print(self.board.output())
        print('Доска врага: ')
        print(self.enemy.board.output(True))
        move = input('Введите два числа через пробел: ').strip().split(' ')

        while True:
            if len(move) == 2 and move[0].isnumeric() and move[1].isnumeric():
                move = [int(move[0]), int(move[1])]
                if self.board.does_dot_exist(move[0], move[1]) \
                        and move in self.board.give_list_of_dot_for_player():
                    break
            move = input('Ошибка. Повторите ввод: ').strip().split(' ')

        self.enemy.board.shoot(*move)

    def is_form_of_move_correct(self, move):
        if len(move) == 2 and move[0].isnumeric and move[1].isnumeric:
            if self.board.does_dot_exist(move[0], move[1]) \
                    and self.board.field[move[0]][move[1]] in self.board.give_list_of_for_player():
                return True
        return False


class AI(Player):
    def ask(self):
        print('ХОД AI: ')
        ch = choice(self.enemy.board.give_list_of_dot_for_player())
        print(f'Ход на поле: {ch[0], ch[1]}')
        self.enemy.board.shoot(ch[0], ch[1])
        print()


class Game:
    def __init__(self, first_player, second_player):
        self.first_player = first_player
        self.second_player = second_player
        self.current_player = self.first_player

    @staticmethod
    def greet():
        greeting = "Морской бой\n"
        greeting += "Правила игры:\n"
        greeting += "Игрок должен уничтожить все корабли соперника, раньше его\n"
        greeting += "Ход пишется двумя цифрами через пробел. Цифры могут быть от 1 до размера доски, концы включая.\n"

    def loop(self):
        while not self.does_winner_exist():
            self.current_player.ask()
            self.change_current_player()

    def start(self):
        self.greet()

        self.first_player.board.create_random_board()
        self.second_player.board.create_random_board()

        self.first_player.enemy = self.second_player
        self.second_player.enemy = self.first_player

        self.loop()

    def does_winner_exist(self):
        if self.first_player.board.is_all_ships_destroyed():
            return self.second_player
        if self.second_player.board.is_all_ships_destroyed():
            return self.first_player
        else:
            return False

    def change_current_player(self):
        if self.current_player == self.first_player:
            self.current_player = self.second_player
            self.enemy_of_current_player = self.first_player
        else:
            self.current_player = self.first_player
            self.enemy_of_current_player = self.second_player

f_p = User()
s_p = AI()
game = Game(f_p, s_p)

game.start()
