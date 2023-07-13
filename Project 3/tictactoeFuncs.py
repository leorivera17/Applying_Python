# Project 3 - Tic-Tac-Toe Simulator
#
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 3

from random import *
import random


# signature: none -> string
# purpose: tells user the rules
# 1) welcome function
def welcome():
    print('Welcome to Tic-Tac-Toe Simulator')
    print('Your goal is to line up 3 of your tics in either a line or a diagonal. ')
    print('You will pick either X or O. X will go first.')
    mode = input('Please return 1 for 1 player or 2 for 2 players: ')
    if mode == '1' or mode == '2':
        return mode
    else:
        while mode != '1' and mode != '2':
            print('Error: please input valid player count')
            mode = input('Return 1 for 1 player or 2 for 2 players: ')


# signature: none -> list
# purpose: where the board is created for the game
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


# signature: list -> list
# purpose: get the string to form it to look like a board
# 3) print_board function
def print_board(main_list):
    print('', main_list[1], '|', main_list[2], '|', main_list[3])
    print('------------')
    print('', main_list[4], '|', main_list[5], '|', main_list[6])
    print('------------')
    print('', main_list[7], '|', main_list[8], '|', main_list[9])


# signature: none -> list
# purpose: user inputs a string to save for later
# 4) pick_letter function
def pick_letter():
    letter = input('Choose X or O: ')
    while letter not in ['x', 'o', 'X', 'O']:
        print("Can you please try again?")
        letter = input('Choose X or O: ')
    return letter.upper()


def board():
    print('''
   |   |   
------------
   |   |   
------------
   |   |    ''')


# signature: input(integer) -> list
# purpose: asks user to place their number on the board
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


# signature: list -> bool
# purpose: get the string and goes true or false
# 6) check_rows function
def check_rows(main_list):
    if ('X' == main_list[1] and 'X' == main_list[2] and 'X' == main_list[3]) or (
            'X' == main_list[4] and 'X' == main_list[5] and 'X' == main_list[6]) or (
            'X' == main_list[7] and 'X' == main_list[8] and 'X' == main_list[9]):
        return 1
    elif (main_list[1] == 'O' and main_list[2] == 'O' and main_list[3] == 'O') or (
            main_list[4] == 'O' and main_list[5] == 'O' and main_list[6] == 'O') or (
            main_list[7] == 'O' and main_list[8] == 'O' and main_list[9] == 'O'):
        return 2
    else:
        return 0


# signature: list -> bool
# purpose: get the string and goes true or false
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


# signature: list -> bool
# purpose: get the string and goes true or false
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


# signature: list -> bool
# purpose: get the string and goes true or false
# 9) board_full function
def board_full(main_list):
    for idx in range(9):
        if main_list[idx] not in main_list:
            pass
        else:
            return False
    return True


# signature: list -> bool
# purpose: get the string and goes true or false to check and print the winner
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


# signature: random -> list
# purpose: this is where you play an 'AI', where player vs random
# 11) get_random function
def get_random(letter, main_list):
    new_board = main_list
    spot = random.randint(1, 10)
    if spot in [1, 2, 3, 4, 5, 6, 7, 8, 9] and (main_list[spot] != 'X' and main_list[spot] != 'O'):
        new_board[spot] = letter
        return new_board
    else:
        while spot not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or main_list[spot] == 'X' or main_list[spot] == 'O':
            spot = random.randint(1, 10)
        new_board[spot] = letter
        return new_board
