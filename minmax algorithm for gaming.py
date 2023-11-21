def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def is_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def evaluate(board):
    # Evaluate the board: +1 for X win, -1 for O win, 0 for tie
    if is_winner(board, "X"):
        return 1
    elif is_winner(board, "O"):
        return -1
    elif is_board_full(board):
        return 0
    else:
        return None

def minimax(board, depth, maximizing_player):
    score = evaluate(board)

    if score is not None:
        return score

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

def best_move(board):
    best_val = float('-inf')
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = minimax(board, 0, False)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        print_board(board)

        # Player's move
        row = int(input("Enter row (0, 1, or 2) for player X: "))
        col = int(input("Enter column (0, 1, or 2) for player X: "))
        if board[row][col] == " ":
            board[row][col] = "X"
        else:
            print("Cell already occupied. Try again.")
            continue

        # Check for a win or tie
        if is_winner(board, "X"):
            print_board(board)
            print("Player X wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Computer's move using Minimax
        print("Computer's move (O):")
        comp_row, comp_col = best_move(board)
        board[comp_row][comp_col] = "O"

        # Check for a win or tie after computer's move
        if is_winner(board, "O"):
            print_board(board)
            print("Computer (O) wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
