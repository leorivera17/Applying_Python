# Project 3 - Tic-Tac-Toe Simulator
#
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 3
from tactoetic import *


def main():
    welcome()
    main_list = create_board()
    letter = pick_letter()
    get_input(letter, main_list)
    board_full(main_list)
    check_win(main_list)


if __name__ == '__main__':
    main()
