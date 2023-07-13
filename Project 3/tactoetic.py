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
    # while mode == 1 or 2:
    #    print('Must choose between (1)computer, or with (2)Players.')
    #    input('Do you wish to play against a (1)computer, or with (2)Players? ')


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
    #    print(''' main_list[0]  |  num2  |  num3 \n
    #    --------------- \n
    #    num4  |  num5  |  num6 \n
    #    --------------- \n
    #    num7  |  num8  |  num9 ''')
    # main_list.append()
    # print(main_list[0])

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
        # this is where you ask player
    return letter.upper()


# 5) get_input function
def get_input(letter, main_list):
    for i in range(10):
        print_board(main_list)
        print('It is player ' + letter + "'s turn.")
        number = int(input('Where do you like to place your letter (pick in range of 1-9): '))
        if number not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or main_list[number] != ' ':
            print('Invalid move! Location is already taken. Please try again.')
        elif main_list[number] == ' ':
            main_list[number] = letter
            # count += 1
            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'
        else:
            print('Invalid move! Location is already taken. Please try again.')
    return


# 6) check_rows function
def check_rows(main_list):
    #print(main_list)
    if 'X' == main_list[1] and 'X' == main_list[2] and 'X' == main_list[3]:
        return True and 'X'
    if 'X' == main_list[4] and 'X' == main_list[5] and 'X' == main_list[6]:
        return True and 'X'
    if 'X' == main_list[7] and 'X' == main_list[8] and 'X' == main_list[9]:
        return True and 'X'
    if 'O' == main_list[1] and 'O' == main_list[2] and 'O' == main_list[3]:
        return True and 'O'
    if 'O' == main_list[4] and 'O' == main_list[5] and 'O' == main_list[6]:
        return True and 'O'
    if 'O' == main_list[7] and 'O' == main_list[8] and 'O' == main_list[9]:
        return True and 'O'


# 7) check_cols function
def check_cols(main_list):
    if 'X' == main_list[1] and 'X' == main_list[4] and 'X' == main_list[7]:
        return True and 'X'
    if 'X' == main_list[2] and 'X' == main_list[5] and 'X' == main_list[8]:
        return True and 'X'
    if 'X' == main_list[3] and 'X' == main_list[6] and 'X' == main_list[9]:
        return True and 'X'
    if 'O' == main_list[1] and 'O' == main_list[4] and 'O' == main_list[7]:
        return True and 'O'
    if 'O' == main_list[2] and 'O' == main_list[5] and 'O' == main_list[8]:
        return True and 'O'
    if 'O' == main_list[3] and 'O' == main_list[6] and 'O' == main_list[9]:
        return True and 'O'


# 8) check_diags function
def check_diags(main_list):
    if 'X' == main_list[1] and 'X' == main_list[5] and 'X' == main_list[9]:
        return True and 'X'
    if 'X' == main_list[3] and 'X' == main_list[5] and 'X' == main_list[7]:
        return True and 'X'
    if 'O' == main_list[1] and 'O' == main_list[5] and 'O' == main_list[9]:
        return True and 'O'
    if 'O' == main_list[3] and 'O' == main_list[5] and 'O' == main_list[7]:
        return True and 'O'


# 9) board_full function
def board_full(main_list):
    if 'X' == (main_list[1] and main_list[2] and main_list[3] and main_list[4] and main_list[5] and main_list[6] and
               main_list[7] and main_list[8] and main_list[9]):
        return True
    if 'O' == (main_list[1] and main_list[2] and main_list[3] and main_list[4] and main_list[5] and main_list[6] and
               main_list[7] and main_list[8] and main_list[9]):
        return True


def check_win(main_list):
    if check_rows(main_list) or check_diags(main_list) or check_cols(main_list) == True and 'X':
        print("X is the winner!!!!!")
    if check_rows(main_list) or check_diags(main_list) or check_cols(main_list) == True and 'O':
        print("O is the Winner!!!!!!")
    if board_full(main_list) == True and 'O':
        "Draw! Do better next time"
    if board_full(main_list) == True and 'X':
        "Draw! Do better next time"



