import random


def print_board(board: str):
    for row in board:
        print("|".join(row))
        print("-" * 5)


def check_win(board: str) -> str | None:
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]  # Row win
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]  # Column win
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]  # Diagonal win
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]  # Diagonal win
    return None


def main():
    board = [[' ']*3 for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player = players[turn % 2]
        print(f"Player {player}'s turn.")

        if player == 'X':
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
        else:
            empty_fields = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
            row, col = random.choice(empty_fields)

        if board[row][col] == ' ':
            board[row][col] = player
            print_board(board)
            winner = check_win(board)
            if winner:
                print(f"Player {winner} wins!")
                break
            if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                print("It's a tie!")
                break
            turn += 1
        else:
            print("That position is already taken. Try again.")


if __name__ == "__main__":
    main()
