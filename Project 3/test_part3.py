# Project 3 - Tic-Tac-Toe Simulator
#
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 3
from part_3_of_TTT import *


def main():
    user_input = 'y'
    while user_input == 'y':
        welcome()
        main_list = create_board()
        letter = pick_letter()
        print_board(main_list)
        get_input(letter, main_list)
        check_rows(main_list)
        check_cols(main_list)
        check_diags(main_list)
        board_full(main_list)
        check_win(main_list)



        user_input = input('Would you like to play again (y/n)? ')


if __name__ == '__main__':
    main()


