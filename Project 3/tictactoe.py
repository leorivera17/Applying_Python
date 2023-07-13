# Project 3 - Tic-Tac-Toe Simulator
#
# Name: Leo Rivera
# Instructor: S. Einakian
# Section: 3
from tictactoeFuncs import *


def main():
    players = welcome()
    if players == '2':
        main_list = create_board()
        letter = pick_letter()
        board()
        if letter == 'X':
            letter2 = 'O'
        else:
            letter2 = 'X'
        win = 3
        full = False
        while (win == 3 or win == 0) and full == False:
            main_list = get_input(letter, main_list)
            print_board(main_list)
            win = check_win(main_list)
            full = board_full(main_list)
            if win == 1 or win == 2 or full == True:
                pass
            else:
                main_list = get_input(letter2, main_list)
                print_board(main_list)
                win = check_win(main_list)
                full = board_full(main_list)
        if check_win(main_list) == 1:
            print('PLAYER "X" WINS!')
        elif check_win(main_list) == 2:
            print('PLAYER "O" WINS!')
        else:
            print('DRAW!')
    else:
        main_list = create_board()
        letter = pick_letter()
        board()
        if letter == 'X':
            letter2 = 'O'
        else:
            letter2 = 'X'
        win = 3
        full = False
        count = 0
        while (win == 3 or win == 0) and full == False:
            main_list = get_input(letter, main_list)
            count += 1
            print('Turn:', count)
            print_board(main_list)
            win = check_win(main_list)
            full = board_full(main_list)
            if win == 1 or win == 2 or full == True:
                pass
            else:
                main_list = get_random(letter2, main_list)
                count += 1
                print('Turn:', count)
                print_board(main_list)
                win = check_win(main_list)
                full = board_full(main_list)
        if (check_win(main_list) == 1 and letter == 'X') or (check_win(main_list) == 2 and letter == 'O'):
            print('PLAYER WINS')
        elif check_win(main_list) == 0:
            print('The game is a draw! ')
        else:
            print('COMPUTER Wins! ')


if __name__ == '__main__':
    main()
