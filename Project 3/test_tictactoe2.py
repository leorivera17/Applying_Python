from tictactoe2Funcs import *


def main():
    players = welcome()
    if players == '2':
        main_list = create_board()
        letter = pick_letter()
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
            print('Move:', count)
            print_board(main_list)
            win = check_win(main_list)
            full = board_full(main_list)
            if win == 1 or win == 2 or full == True:
                pass
            else:
                main_list = get_input(letter2, main_list)
                count += 1
                print('Move:', count)
                print_board(main_list)
                win = check_win(main_list)
                full = board_full(main_list)
        if check_win(main_list) == 1:
            print('Player "X" wins!')
        elif check_win(main_list) == 2:
            print('Player "O" wins!')
        else:
            print('The game is a draw!')
    else:
        main_list = create_board()
        letter = pick_letter()
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
            print('Move:', count)
            print_board(main_list)
            win = check_win(main_list)
            full = board_full(main_list)
            if win == 1 or win == 2 or full == True:
                pass
            else:
                main_list = get_random(letter2, main_list)
                count += 1
                print('Move:', count)
                print_board(main_list)
                win = check_win(main_list)
                full = board_full(main_list)
        if (check_win(main_list) == 1 and letter == 'X') or (check_win(main_list) == 2 and letter == 'O'):
            print('Player Wins!')
        elif check_win(main_list) == 0:
            print('The game is a draw!')
        else:
            print('Computer Wins!')


if __name__ == '__main__':
    main()
