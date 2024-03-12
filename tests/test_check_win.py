from main import check_win, check_tie


def test__check_row_win():
    board = [
        ['X', 'X', 'X'],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    assert check_win(board) == 'X'


def test_column_win():
    board = [
        ['X', ' ', ' '],
        ['X', ' ', ' '],
        ['X', ' ', ' ']
    ]
    assert check_win(board) == 'X'


def test_diagonal_win():
    board = [
        ['X', ' ', ' '],
        [' ', 'X', ' '],
        [' ', ' ', 'X']
    ]
    assert check_win(board) == 'X'


def test_no_win():
    board = [
        ['X', 'O', 'X'],
        ['X', 'O', ' '],
        ['O', 'X', ' ']
    ]
    assert check_win(board) is None


def test_draw():
    board = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['O', 'X', 'X']
    ]
    assert check_win(board) is None


def test_tie():
    board = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['O', 'X', 'X']
    ]
    assert check_tie(board) == "It's a tie!"


def test_tie_if_there_is_empty_field():
    board = [
        ['X', ' ', 'X'],
        ['X', 'O', 'O'],
        ['O', 'X', 'X']
    ]
    assert check_tie(board) is None
