import random


def display_board(board: list[list[str]]) -> str:
    board_str = ''
    for row in board:
        board_str += "|".join(row) + "\n"
        board_str += "-" * 5 + "\n"
    return board_str


def check_rows(board: list[list[str]]) -> str | None:
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    return None


def check_columns(board: list[list[str]]) -> str | None:
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]
    return None


def check_diagonals(board: list[list[str]]) -> str | None:
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None


def check_tie(board: list[list[str]]) -> str | None:
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        return "It's a tie!"
    return None


def check_win(board: list[list[str]]) -> str | None:

    row_win = check_rows(board)
    if row_win:
        return row_win

    column_win = check_columns(board)
    if column_win:
        return column_win

    diagonal_win = check_diagonals(board)
    if diagonal_win:
        return diagonal_win
    return None


def new_board():
    board = [[' '] * 3 for _ in range(3)]
    return board


def main():
    board = new_board()
    players = ['X', 'O']
    turn = 0

    print("Welcome to Tic-Tac-Toe!")
    print(display_board(board))

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
            print(display_board(board))
            winner = check_win(board)
            if winner:
                print(f"Player {winner} wins!")
                break
            if check_tie == "It's a tie!":
                print("It's a tie!")
                break
            turn += 1
        else:
            print("That position is already taken. Try again.")


if __name__ == "__main__":
    main()
