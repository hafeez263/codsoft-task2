import random

# Initialize board
board = [' ' for _ in range(9)]

def print_board():
    for i in range(3):
        print('|'.join(board[i*3:(i+1)*3]))
        if i < 2:
            print("-----")

def check_winner(b, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for condition in win_conditions:
        if all(b[i] == player for i in condition):
            return True
    return False

def is_draw(b):
    return ' ' not in b

def minimax(b, depth, is_maximizing):
    if check_winner(b, 'O'):
        return 1
    if check_winner(b, 'X'):
        return -1
    if is_draw(b):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score

def best_move():
    best_score = -float('inf')
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    return move

def player_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and 1 <= int(move) <= 9:
            move = int(move) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("That spot is already taken.")
        else:
            print("Invalid move. Try again.")

def play_game():
    print("Welcome to Tic-Tac-Toe! You are X, AI is O.")
    print_board()
    while True:
        player_move()
        print_board()
        if check_winner(board, 'X'):
            print("You win!")
            break
        if is_draw(board):
            print("It's a draw!")
            break
        ai_move = best_move()
        board[ai_move] = 'O'
        print("\nAI moved:")
        print_board()
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

play_game()
