import math

# Initialize the board
board = [' ' for _ in range(9)]  # 3x3 board

# Function to print the board
def print_board():
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

# Function to check if there is a winner
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Function to check if the board is full (a tie)
def is_board_full(board):
    return ' ' not in board

# Minimax function to evaluate the best move
def minimax(board, depth, is_maximizing):
    if check_winner(board, 'O'):  # AI wins
        return 1
    elif check_winner(board, 'X'):  # Human wins
        return -1
    elif is_board_full(board):  # Tie
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'  # AI move
                score = minimax(board, depth + 1, False)
                board[i] = ' '  # Undo the move
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'  # Human move
                score = minimax(board, depth + 1, True)
                board[i] = ' '  # Undo the move
                best_score = min(score, best_score)
        return best_score

# Function for the AI to make its move
def ai_move():
    best_score = -math.inf
    best_move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'  # AI move
            score = minimax(board, 0, False)
            board[i] = ' '  # Undo the move
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = 'O'

# Function to get the human player's move
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == ' ':
                board[move] = 'X'
                break
            else:
                print("This spot is already taken!")
        except (ValueError, IndexError):
            print("Invalid move. Please enter a number between 1 and 9.")

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    
    while True:
        player_move()
        print_board()
        if check_winner(board, 'X'):
            print("Congratulations, you win!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        ai_move()
        print("AI makes its move:")
        print_board()
        if check_winner(board, 'O'):
            print("AI wins! Better luck next time.")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
