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
    # while mode == 1 or 2:
    #    print('Must choose between (1)computer, or with (2)Players.')
    #    input('Do you wish to play against a (1)computer, or with (2)Players? ')


# def board_create(boarded):
#    board = ''' 1  |  2  |  3
#    ---------------
#    4  |  5  |  6
#    ---------------
#     7  |  8  |  9 '''
#    for i in range(1, 10):
#        if boarded[i] == 'O' or boarded[i] == 'X':
#            board = board.replace(str(i), boarded[i])
#        else:
#            board = board.replace(str(i), ' ')
#    print(board)


# 2) create_board function
def create_board():
    main_list = [None, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    # main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # main_list = [[num1, num2, num3], [num4, num5, num6], [num7, num8, num9]]
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
    print('', main_list[1], '|', main_list[2], '|', main_list[3])
    print('------------')
    print('', main_list[4], '|', main_list[5], '|', main_list[6])
    print('------------')
    print('', main_list[7], '|', main_list[8], '|', main_list[9])


#    print(' {}  |  {}  | {}'.format(main_list[0], main_list[1], main_list[2]))
#    print('---------------')
#    print(' {}  |  {}  |  {}'.format(main_list[3], main_list[4], main_list[5]))
#    print('---------------')
#    print(' {}  |  {}  |  {}'.format(main_list[6], main_list[7], main_list[8]))


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
    # this is where you will append
    #    letter = 'X'
    #    count = 0
    #    if letter == 'X':
    #        print("It's Player 1's (X's) turn! ")
    #        count += 1
    #    if letter == 'O':
    #        print("It's Player 2's (O's) turn! ")
    #        count += 1
    #    if letter == 'X' or 'O':
    #        count += 1
    print_board(main_list)
    number = int(input('Where do you like to place your letter (pick in range of 1-9): '))
    while number not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or main_list[number] != ' ':
        # while number <= 9:
        print('Invalid move! Location is already taken. Please try again.')
        number = int(input('Where do you like to place your letter (pick in range of 1-9): '))
    #        if number == number:
    #            print('Invalid move! Location is already taken. Please try again.')
    #            number = int(input('Where do you like to place your letter (pick in range of 1-9): '))
    main_list[number] = letter
    if main_list[number] == ' ':
        main_list[number] = letter
    # count += 1
        if letter == 'X':
            letter = 'O'
    else:
        letter = 'X'

    #        if board[number] == ' ':
    #            board[number] = letter
    #            count += 1
    # while count != 10:
    # board[number] = main_list[i] - 1
    return main_list


# 6) check_rows function
def check_rows(main_list):
    if 'X' or 'O' == main_list[1] and main_list[2] and main_list[3]:
        return 'win'
    if 'X' or 'O' == main_list[4] and main_list[5] and main_list[6]:
        return 'win'
    if 'X' or 'O' == main_list[7] and main_list[8] and main_list[9]:
        return 'win'


# 7) check_cols function
def check_cols(main_list):
    if 'X' or 'O' == main_list[1] and main_list[4] and main_list[7]:
        return 'win'
    if 'X' or 'O' == main_list[2] and main_list[5] and main_list[8]:
        return 'win'
    if 'X' or 'O' == main_list[3] and main_list[6] and main_list[9]:
        return 'win'


# 8) check_diags function
def check_diags(main_list):
    if 'X' or 'O' == main_list[1] and main_list[5] and main_list[9]:
        return 'win'
    if 'X' or 'O' == main_list[3] and main_list[5] and main_list[7]:
        return 'win'


# 9) board_full function
def board_full(main_list):
    pass


# 10) check_win function
def check_win(main_list):
    if check_rows(main_list) == True:
        return 'WIN'
    if check_cols(main_list) == True:
        return 'WIN'
    if check_diags(main_list) == True:
        return 'WIN'
    else:
        return 'NO WINNER'
