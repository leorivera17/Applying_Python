# Project 3 - Tic-Tac-Toe Simulator
#
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 3

from random import *
import random


# 1) welcome function
def welcome():
    print('Welcome to Tic-Tac-Toe Simulator')
    print('Your goal is to line up 3 of your tics in either a line or a diagonal. ')
    print('You will pick either X or O. X will go first.')
    mode = input('Do you wish to play against a (1)computer, or with (2)Players? ')
    while mode not in ('1', '2'):
        print('Must choose between (1)computer, or with (2)Players.')
        mode = input('Do you wish to play against a (1)computer, or with (2)Players? ')


# 2) create_board function
def create_board():
    main_list = [None, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    print('''
 1  |  2  |  3
---------------
 4  |  5  |  6
---------------
 7  |  8  |  9 ''')
    return main_list


# 3) print_board function
def print_board(main_list):
    print('', main_list[1], '|', main_list[2], '|', main_list[3])
    print('------------')
    print('', main_list[4], '|', main_list[5], '|', main_list[6])
    print('------------')
    print('', main_list[7], '|', main_list[8], '|', main_list[9])


# 4) pick_letter function
def pick_letter():
    letter = input('Choose X or O: ')
    while letter not in ['x', 'o', 'X', 'O']:
        print("Can you please try again?")
        letter = input('Choose X or O: ')
    return letter.upper()


# 5) get_input function
def get_input(letter, main_list):
    print('It is player ' + letter + "'s turn.")
    number = int(input('Where do you like to place your letter (pick in range of 1-9): '))
    if main_list[number] == ' ':
        main_list[number] = letter
        return main_list
    else:
        while number not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or main_list[number] != ' ':
            print('Must be between 1-9 or spot is already taken! ')
            number = int(input('Where do you like to place your letter (pick in range of 1-9): '))
            main_list[number] = letter
        return main_list


# 6) check_rows function
def check_rows(main_list):

    if ('X' == main_list[1] and 'X' == main_list[2] and 'X' == main_list[3]) or \
            ('X' == main_list[4] and 'X' == main_list[5] and 'X' == main_list[6]) or \
            ('X' == main_list[7] and 'X' == main_list[8] and 'X' == main_list[9]):
        return 1
    elif (main_list[1] == 'O' and main_list[2] == 'O' and main_list[3] == 'O') or (
            main_list[4] == 'O' and main_list[5] == 'O' and main_list[6] == 'O') or (
            main_list[7] == 'O' and main_list[8] == 'O' and main_list[9] == 'O'):
        return 2
    else:
        return 0


# 7) check_cols function
def check_cols(main_list):
    if (main_list[1] == 'X' and main_list[4] == 'X' and main_list[7] == 'X') or (
            main_list[2] == 'X' and main_list[5] == 'X' and main_list[8] == 'X') or (
            main_list[3] == 'X' and main_list[6] == 'X' and main_list[9] == 'X'):
        return 1
    elif (main_list[1] == 'O' and main_list[4] == 'O' and main_list[7] == 'O') or (
            main_list[2] == 'O' and main_list[5] == 'O' and main_list[8] == 'O') or (
            main_list[3] == 'O' and main_list[6] == 'O' and main_list[9] == 'O'):
        return 2
    else:
        return 0


# 8) check_diags function
def check_diags(main_list):
    if (main_list[3] == 'X' and main_list[5] == 'X' and main_list[7] == 'X') or (
            main_list[1] == 'X' and main_list[5] == 'X' and main_list[9] == 'X'):
        return 1
    elif (main_list[1] == 'O' and main_list[5] == 'O' and main_list[9] == 'O') or (
            main_list[3] == 'O' and main_list[5] == 'O' and main_list[7] == 'O'):
        return 2
    else:
        return 0


# 9) board_full function
def board_full(main_list):
    for i in range(9):
        if main_list[i] not in main_list:
            pass
        else:
            return False
    return True


def check_win(main_list):
    rows = check_rows(main_list)
    cols = check_cols(main_list)
    diags = check_diags(main_list)
    if rows == 1 or cols == 1 or diags == 1:
        return 1
    elif rows == 2 or cols == 2 or diags == 2:
        return 2
    else:
        return 0


# 11) get_random function
def get_random(letter: str, board: list) -> list:
    updated_board = board
    position = randint(1, 10)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if position in numbers and (board[position - 1] != 'X' and board[position - 1] != 'O'):
        updated_board[position - 1] = letter
        return updated_board
    else:
        while position not in numbers or board[position - 1] == 'X' or board[position - 1] == 'O':
            position = randint(1, 10)
        updated_board[position - 1] = letter
        return updated_board