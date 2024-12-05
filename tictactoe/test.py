import game_util


def test_first_row_zeroes_wins():
    board = [['O', 'O', 'O'], ['_', '_', '_'], ['_', '_', '_']]
    assert game_util.check_if_player_wins(board)


def test_second_row_zeroes_wins():
    board = [['_', '_', '_'], ['O', 'O', 'O'], ['_', '_', '_']]
    assert game_util.check_if_player_wins(board)


def test_third_row_zeroes_wins():
    board = [['_', '_', '_'], ['_', '_', '_'], ['O', 'O', 'O']]
    assert game_util.check_if_player_wins(board)


def test_first_row_crosses_wins():
    board = [['X', 'X', 'X'], ['_', '_', '_'], ['_', '_', '_']]
    assert game_util.check_if_player_wins(board)


def test_second_row_crosses_wins():
    board = [['_', '_', '_'], ['X', 'X', 'X'], ['_', '_', '_']]
    assert game_util.check_if_player_wins(board)


def test_third_row_crosses_wins():
    board = [['_', '_', '_'], ['_', '_', '_'], ['X', 'X', 'X']]
    assert game_util.check_if_player_wins(board)


def test_first_column_zeroes_wins():
    board = [['O', '_', '_'], ['O', '_', '_'], ['O', '_', '_']]
    assert game_util.check_if_player_wins(board)


def test_second_column_zeroes_wins():
    board = [['_', 'O', '_'], ['_', 'O', '_'], ['_', 'O', '_']]
    assert game_util.check_if_player_wins(board)


def test_third_column_zeroes_wins():
    board = [['_', '_', 'O'], ['_', '_', 'O'], ['_', '_', 'O']]
    assert game_util.check_if_player_wins(board)


def test_first_column_crosses_wins():
    board = [['X', '_', '_'], ['X', '_', '_'], ['X', '_', '_']]
    assert game_util.check_if_player_wins(board)


def test_second_column_crosses_wins():
    board = [['_', 'X', '_'], ['_', 'X', '_'], ['_', 'X', '_']]
    assert game_util.check_if_player_wins(board)


def test_third_column_crosses_wins():
    board = [['_', '_', 'X'], ['_', '_', 'X'], ['_', '_', 'X']]
    assert game_util.check_if_player_wins(board)


def test_first_diagonal_zeroes_wins():
    board = [['O', '_', '_'], ['_', 'O', '_'], ['_', '_', 'O']]
    assert game_util.check_if_player_wins(board)


def test_second_diagonal_zeroes_wins():
    board = [['_', '_', 'O'], ['_', 'O', '_'], ['O', '_', '_']]
    assert game_util.check_if_player_wins(board)


def test_first_diagonal_crosses_wins():
    board = [['X', '_', '_'], ['_', 'X', '_'], ['_', '_', 'X']]
    assert game_util.check_if_player_wins(board)


def test_second_diagonal_crosses_wins():
    board = [['_', '_', 'X'], ['_', 'X', '_'], ['X', '_', '_']]
    assert game_util.check_if_player_wins(board)
