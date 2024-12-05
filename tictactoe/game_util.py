from colorama import Fore

winner_line_zeroes = ['O'] * 3
winner_line_crosses = ['X'] * 3
winning_lines = [
    [(0, 0), (0, 1), (0, 2)],  # row 1
    [(1, 0), (1, 1), (1, 2)],  # row 2
    [(2, 0), (2, 1), (2, 2)],  # row 3
    [(0, 0), (1, 0), (2, 0)],  # column 1
    [(0, 1), (1, 1), (2, 1)],  # column 2
    [(0, 2), (1, 2), (2, 2)],  # column 3
    [(0, 0), (1, 1), (2, 2)],  # diagonal 1
    [(0, 2), (1, 1), (2, 0)],  # diagonal 2
]


def init_game_field():
    return [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_'],
    ]


def draw_board(field):
    for line in field:
        colored_line = []
        for symbol in line:
            colored_line.append(symbol)
        print(' | '.join(line))


def draw_board_colored(board):
    indexes = [0, 1, 2]
    for line in board:
        for index, sign in zip(indexes, line):
            if sign == 'O':
                print(Fore.BLUE + sign, end='')
            elif sign == 'X':
                print(Fore.RED + sign, end='')
            else:
                print(Fore.RESET + sign, end='')
            if index < 2:
                print(Fore.RESET + ' | ', end='')
        print(Fore.RESET + '')

def swap_player(player):
    return 'O' if player == 'X' else 'X'


def ask_player(player):
    print(f'Player {player} makes a turn. Enter cell coordinates...')
    coordinate_x, coordinate_y = -1, -1
    while coordinate_x < 0:
        coordinate_x = ask_coordinate('X')
    while coordinate_y < 0:
        coordinate_y = ask_coordinate('Y')
    return coordinate_x, coordinate_y


def ask_coordinate(coordinate_name):
    coordinate = input(f'{coordinate_name}: ')
    if not coordinate.isdigit():
        print('Entered line is not a digit. Try again')
        return -1
    int_coordinate = int(coordinate)
    if not 1 <= int_coordinate <= 3:
        print('A coordinate must be in range of 1-3. Try again')
        return -1
    return int_coordinate


def check_cell_is_empty(coord_x, coord_y, field):
    is_empty = field[coord_x - 1][coord_y - 1] == '_'
    if not is_empty:
        print('The cell is not empty. Try again')
    return is_empty


def check_if_player_wins(field):
    crosses, zeroes = winner_line_crosses, winner_line_zeroes
    for line in winning_lines:
        result = []
        for coordinate_tuple in line:
            result.append(field[coordinate_tuple[0]][coordinate_tuple[1]])
        print(result)
        if result == crosses or result == zeroes:
            return True
    return False


def check_if_board_is_full(field):
    for line in field:
        if line.count('_') > 0:
            return False
    return True
