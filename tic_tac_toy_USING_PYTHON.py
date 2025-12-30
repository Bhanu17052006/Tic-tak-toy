# Tic Tac Toe Game in Python

board = [' '] * 10   # index 0 unused

def display_board():
    print()
    print(board[1], '|', board[2], '|', board[3])
    print('--+---+--')
    print(board[4], '|', board[5], '|', board[6])
    print('--+---+--')
    print(board[7], '|', board[8], '|', board[9])
    print()

def win_check(mark):
    return (
        (board[1] == board[2] == board[3] == mark) or
        (board[4] == board[5] == board[6] == mark) or
        (board[7] == board[8] == board[9] == mark) or
        (board[1] == board[4] == board[7] == mark) or
        (board[2] == board[5] == board[8] == mark) or
        (board[3] == board[6] == board[9] == mark) or
        (board[1] == board[5] == board[9] == mark) or
        (board[3] == board[5] == board[7] == mark)
    )

def space_free(pos):
    return board[pos] == ' '

def full_board():
    return board.count(' ') == 1

def player_move(mark):
    pos = int(input(f"Player {mark}, enter position (1-9): "))
    if space_free(pos):
        board[pos] = mark
    else:
        print("Position already taken!")
        player_move(mark)

# Main Game
print("🎮 TIC TAC TOE GAME 🎮")

while True:
    display_board()
    player_move('X')
    if win_check('X'):
        display_board()
        print("Player X Wins!")
        break
    if full_board():
        display_board()
        print("It's a Draw!")
        break

    display_board()
    player_move('O')
    if win_check('O'):
        display_board()
        print("Player O Wins!")
        break
