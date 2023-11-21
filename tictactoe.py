def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        # Get player move
        row = int(input(f"Enter row (0, 1, or 2) for player {current_player}: "))
        col = int(input(f"Enter column (0, 1, or 2) for player {current_player}: "))

        # Check if the chosen cell is empty
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Cell already occupied. Try again.")
            continue

        # Check for a win
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    play_tic_tac_toe()
