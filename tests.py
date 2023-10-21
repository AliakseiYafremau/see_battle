import unittest
from main import Board, Dot, Ship


class TestGame(unittest.TestCase):
    def setUp(self):
        self.board_1 = Board(6)
        self.board_1.field[0][0].does_have_ship = Ship(1, [[0], [0]])
        self.board_1.field[1][5].does_have_ship = Ship(1, [[1], [5]])
        self.board_1.field[2][2].does_have_ship = Ship(1, [[2], [2]])
        self.board_1.field[3][0].does_have_ship = Ship(1, [[3], [0]])
        self.board_1.field[3][4].does_have_ship = Ship(1, [[3], [4]])
        self.board_1.field[4][2].does_have_ship = Ship(1, [[4], [2]])
        self.board_1.field[5][5].does_have_ship = Ship(1, [[5], [5]])

        self.empty_board = Board(6)

        # ship - o
        # misfit - x
        #
        #     0 1 2 3 4 5
        #   + - - - - - - +
        # 0 | O           |
        # 1 |           O |
        # 2 |     O       |
        # 3 | O       O   |
        # 4 |     O       |
        # 5 |           O |
        #   + - - - - - - +

    def test_existing_of_dot(self):

        self.assertTrue(self.board_1.does_dot_exist(3, 4))
        self.assertTrue(self.board_1.does_dot_exist(1, 0))
        self.assertTrue(self.board_1.does_dot_exist(4, 2))
        self.assertTrue(self.board_1.does_dot_exist(0, 5))

        self.assertFalse(self.board_1.does_dot_exist(1, 6))
        self.assertFalse(self.board_1.does_dot_exist(4, -1))
        self.assertFalse(self.board_1.does_dot_exist(0, 6))

    def test_can_be_stayed_ship(self):

        self.assertTrue(self.board_1.can_be_stayed_ship(5, 0))
        self.assertTrue(self.board_1.can_be_stayed_ship(0, 2))
        self.assertTrue(self.board_1.can_be_stayed_ship(0, 3))

        self.assertFalse(self.board_1.can_be_stayed_ship(1, 1))
        self.assertFalse(self.board_1.can_be_stayed_ship(3, 3))
        self.assertFalse(self.board_1.can_be_stayed_ship(5, 5))
        self.assertFalse(self.board_1.can_be_stayed_ship(0, 0))
        self.assertFalse(self.board_1.can_be_stayed_ship(0, 4))

    def test_creating_of_ships(self):

        result_1 = self.empty_board.create_ships(1, 3)
        result_2 = self.empty_board.create_ships(2, 2)
        result_3 = self.empty_board.create_ships(4, 1)

        self.assertEqual(len(result_1), 1)
        self.assertEqual(len(result_2), 2)
        self.assertEqual(len(result_3), 4)


