from joshttt import *


def main():
    players = welcome_function()
    if players == '2':
        board = create_board()
        letter = pick_letter()
        if letter == 'X':
            letter2 = 'O'
        else:
            letter2 = 'X'
        win = 3
        full = False
        count = 0
        while (win == 3 or win == 0) and full == False:
            board = get_input(letter, board)
            count += 1
            print('Move:', count)
            print_board(board)
            win = check_win(board)
            full = board_full(board)
            if win == 1 or win == 2 or full == True:
                pass
            else:
                board = get_input(letter2, board)
                count += 1
                print('Move:', count)
                print_board(board)
                win = check_win(board)
                full = board_full(board)
        if check_win(board) == 1:
            print('Player "X" wins!')
        elif check_win(board) == 2:
            print('Player "O" wins!')
        else:
            print('The game is a draw!')
    else:
        board = create_board()
        letter = pick_letter()
        if letter == 'X':
            letter2 = 'O'
        else:
            letter2 = 'X'
        win = 3
        full = False
        count = 0
        while (win == 3 or win == 0) and full == False:
            board = get_input(letter, board)
            count += 1
            print('Move:', count)
            print_board(board)
            win = check_win(board)
            full = board_full(board)
            if win == 1 or win == 2 or full == True:
                pass
            else:
                board = get_random(letter2, board)
                count += 1
                print('Move:', count)
                print_board(board)
                win = check_win(board)
                full = board_full(board)
        if (check_win(board) == 1 and letter == 'X') or (check_win(board) == 2 and letter == 'O'):
            print('Player Wins!')
        elif check_win(board) == 0:
            print('The game is a draw!')
        else:
            print('Computer Wins!')


if __name__ == '__main__':
    main()
