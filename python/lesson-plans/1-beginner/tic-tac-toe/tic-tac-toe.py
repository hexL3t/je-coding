# -------------------------------
# Tic-Tac-Toe Game in Python 🕹️
# -------------------------------

# Initialize an empty 3x3 board using a list of lists
# Each cell starts with a space character ' ' to show it's empty
board = [[' ' for _ in range(3)] for _ in range(3)]

# This function prints the current state of the game board
def print_board():
    for row in board:
        # Print each row, separating cells with |
        print(' | '.join(row))
        # Print a horizontal line after each row for clarity
        print('-' * 5)

# This function checks if there is a winner
def check_winner():
    # Check rows for 3 matching non-empty symbols
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True
    # Check columns for 3 matching non-empty symbols
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return True
    # Check top-left to bottom-right diagonal
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    # Check top-right to bottom-left diagonal
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True
    # No winner found
    return False

# This function runs the game for two human players
def game():
    player = 'X'  # Player X goes first
    for turn in range(9):  # Maximum of 9 moves in Tic-Tac-Toe
        print_board()  # Show the board before each move
        # Ask the player to enter a row and column number (0 to 2)
        row = int(input(f"Player {player}, enter row (0-2): "))
        col = int(input(f"Player {player}, enter col (0-2): "))
        # Check if the selected cell is empty
        if board[row][col] == ' ':
            board[row][col] = player  # Place the player's symbol
            # Check if the current move caused the player to win
            if check_winner():
                print_board()
                print(f"Player {player} wins! 🎉")
                return  # End the game
            # Switch to the other player
            player = 'O' if player == 'X' else 'X'
        else:
            print("Cell already occupied, try again.")
    print_board()
    print("It's a draw! ✨")

# Start the two-player game
game()
