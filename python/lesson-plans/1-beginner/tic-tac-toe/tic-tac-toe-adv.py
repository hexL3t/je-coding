import math

# ----------------------
# Setup and Game Helpers
# ----------------------

# Creates a new, empty 3x3 game board
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Prints the current board layout in a user-friendly format
def print_board(board):
    for row in board:
        print(' | '.join(row))  # Show each cell in the row separated by "|"
        print('-' * 5)          # Add a line under each row for clarity

# Checks if someone has won the game
def check_winner(board):
    # Check all rows for a win
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    # Check all columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    # Check both diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    # No winner yet
    return None

# Checks if the board is full and no winner — a draw
def is_draw(board):
    return all(cell != ' ' for row in board for cell in row)

# Returns a list of all available (empty) cells
def available_moves(board):
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ' ']

# ----------------------
# Minimax AI Logic
# ----------------------

# The minimax function simulates every possible game state recursively
# It tries to find the best possible move for the computer
def minimax(board, depth, is_maximizing, ai_symbol, player_symbol):
    # Base case: Check for a winner or a draw
    winner = check_winner(board)
    if winner == ai_symbol:
        return 10 - depth  # Fewer moves to win = better
    elif winner == player_symbol:
        return depth - 10  # More moves = worse
    elif is_draw(board):
        return 0  # Draw is neutral

    # If it's the AI's turn to maximize the score
    if is_maximizing:
        best_score = -math.inf  # Start with the lowest possible score
        for r, c in available_moves(board):
            board[r][c] = ai_symbol
            score = minimax(board, depth + 1, False, ai_symbol, player_symbol)
            board[r][c] = ' '  # Undo move (backtrack)
            best_score = max(score, best_score)
        return best_score
    else:
        # Player is minimizing the AI's score
        best_score = math.inf
        for r, c in available_moves(board):
            board[r][c] = player_symbol
            score = minimax(board, depth + 1, True, ai_symbol, player_symbol)
            board[r][c] = ' '
            best_score = min(score, best_score)
        return best_score

# Finds the best move by evaluating all possible moves with minimax
def best_move(board, ai_symbol, player_symbol):
    best_score = -math.inf
    move = None
    for r, c in available_moves(board):
        board[r][c] = ai_symbol
        score = minimax(board, 0, False, ai_symbol, player_symbol)
        board[r][c] = ' '  # Undo the move
        if score > best_score:
            best_score = score
            move = (r, c)
    return move

# ----------------------
# Full Game with Options
# ----------------------

# The main game loop
def advanced_game():
    scores = {'Player': 0, 'Computer': 0}  # Keep track of wins
    print("Welcome to Advanced Tic-Tac-Toe! 🧠")
    
    while True:
        board = create_board()
        print("\nNew Game Started!\n")
        
        # Let player choose their symbol
        player_symbol = ''
        while player_symbol not in ['X', 'O']:
            player_symbol = input("Choose your symbol (X/O): ").upper()

        ai_symbol = 'O' if player_symbol == 'X' else 'X'
        player_turn = player_symbol == 'X'  # X always starts

        # Main gameplay loop
        while True:
            print_board(board)

            if player_turn:
                # Get player's move and validate input
                try:
                    row = int(input("Enter row (0-2): "))
                    col = int(input("Enter col (0-2): "))
                    if (0 <= row < 3 and 0 <= col < 3) and board[row][col] == ' ':
                        board[row][col] = player_symbol
                        if check_winner(board) == player_symbol:
                            print_board(board)
                            print("🎉 You win!")
                            scores['Player'] += 1
                            break
                        elif is_draw(board):
                            print_board(board)
                            print("It's a draw!")
                            break
                        player_turn = False  # Switch to computer's turn
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Please enter numbers only.")
            else:
                # Computer's move using minimax
                print("Computer is thinking... 🤖")
                r, c = best_move(board, ai_symbol, player_symbol)
                board[r][c] = ai_symbol
                if check_winner(board) == ai_symbol:
                    print_board(board)
                    print("💻 Computer wins!")
                    scores['Computer'] += 1
                    break
                elif is_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                player_turn = True  # Switch back to player

        # Show updated scores
        print(f"\n🏅 Score -> You: {scores['Player']} | Computer: {scores['Computer']}\n")

        # Ask player if they want to play again
        again = input("Play again? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing! 👋")
            break

# Start the game
advanced_game()