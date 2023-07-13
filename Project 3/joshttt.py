from random import *


def welcome_function():
    print('Welcome to TicTacToe Game!')
    print('The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.')
    print('Once the game begins you will choose marks based on these locations:')
    print('1 | 2 | 3')
    print('---------')
    print('4 | 5 | 6')
    print('---------')
    print('7 | 8 | 9')
    players = input('Please return 1 for 1 player or 2 for 2 players: ')
    if players == '1' or players == '2':
        return players
    else:
        while players != '1' and players != '2':
            print('Error: please input valid player count')
            players = input('Return 1 for 1 player or 2 for 2 players: ')


# 2) create_board function
def create_board() -> list:
    board = []
    for num in range(9):
        board.append(num + 1)
    return board


# 3) print_board function
def print_board(current_board: list):
    printed_board = []
    for idx in range(9):
        printed_board.append(' ')
    for idx in range(9):
        if current_board[idx] == 'X':
            printed_board[idx] = 'X'
        elif current_board[idx] == 'O':
            printed_board[idx] = 'O'
        else:
            printed_board[idx] = ' '
    print(printed_board[0], '|', printed_board[1], '|', printed_board[2])
    print('---------')
    print(printed_board[3], '|', printed_board[4], '|', printed_board[5])
    print('---------')
    print(printed_board[6], '|', printed_board[7], '|', printed_board[8])


# 4) pick_letter function
def pick_letter():
    letter = input('Please choose either X or O: ')
    letter = letter.upper()
    if letter == 'X' or letter == 'O':
        return letter
    else:
        while letter != 'X' and letter != 'O':
            print('Error: please input valid letter')
            letter = input('Please choose either X or O: ')


# 5) get_input function
def get_input(letter: str, board: list) -> list:
    updated_board = board
    position = int(input('Please choose location of your move (1-9): '))
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if position in numbers and (board[position - 1] != 'X' and board[position - 1] != 'O'):
        updated_board[position - 1] = letter
        return updated_board
    else:
        while position not in numbers or board[position - 1] == 'X' or board[position - 1] == 'O':
            position = int(input('Invalid Move! Location is already taken or not in range. Please try again. '))
        updated_board[position - 1] = letter
        return updated_board


# 6) check_rows function
def check_rows(board: list) -> int:
    if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or (
            board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or (
            board[6] == 'X' and board[7] == 'X' and board[8] == 'X'):
        return 1
    elif (board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or (
            board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or (
            board[6] == 'O' and board[7] == 'O' and board[8] == 'O'):
        return 2
    else:
        return 0


# 7) check_cols function
def check_cols(board: list) -> int:
    if (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or (
            board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or (
            board[2] == 'X' and board[5] == 'X' and board[8] == 'X'):
        return 1
    elif (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or (
            board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or (
            board[2] == 'O' and board[5] == 'O' and board[8] == 'O'):
        return 2
    else:
        return 0


# 8) check_diags function
def check_diags(board: list) -> int:
    if (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or (
            board[2] == 'X' and board[4] == 'X' and board[6] == 'X'):
        return 1
    elif (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or (
            board[2] == 'O' and board[4] == 'O' and board[6] == 'O'):
        return 2
    else:
        return 0


# 9) check_win function
def check_win(board: list) -> str:
    rows = check_rows(board)
    cols = check_cols(board)
    diags = check_diags(board)
    if rows == 1 or cols == 1 or diags == 1:
        return 1
    elif rows == 2 or cols == 2 or diags == 2:
        return 2
    else:
        return 0


# 10) board_full function
def board_full(board: list) -> bool:
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for idx in range(9):
        if board[idx] not in numbers:
            pass
        else:
            return False
    return True


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
