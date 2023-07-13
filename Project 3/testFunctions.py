# Project 3 - Tic-Tac-Toe Simulator
#
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 3
# Functions definitions comes here

import unittest
from tictactoeFuncs import *


class TestCases(unittest.TestCase):
    def test_create_board(self):
        self.assertEqual(create_board(), [None, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])

    def test_check_rows(self):
        main_list = [None, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        self.assertEqual(check_rows(main_list), 1)
        main_list = [None, 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        self.assertEqual(check_rows(main_list), 2)
        main_list = [None, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(check_rows(main_list), 0)

    def test_check_cols(self):
        main_list = [None, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        self.assertEqual(check_cols(main_list), 1)
        main_list = [None, 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        self.assertEqual(check_cols(main_list), 2)
        main_list = [None, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(check_cols(main_list), 0)

    def test_check_diags(self):
        main_list = [None, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        self.assertEqual(check_diags(main_list), 1)
        main_list = [None, 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        self.assertEqual(check_diags(main_list), 2)
        main_list = [None, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(check_diags(main_list), 0)

    def test_check_win(self):
        main_list = [None, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(check_win(main_list), 0)
        main_list = [None, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        self.assertEqual(check_win(main_list), 1)
        main_list = [None, 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        self.assertEqual(check_win(main_list), 2)

    def test_board_full(self):
        main_list = [None, 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
        self.assertEqual(board_full(main_list), False)
        main_list = [None, 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']
        self.assertEqual(board_full(main_list), False)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
