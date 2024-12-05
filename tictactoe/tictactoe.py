import game_util
import random

game_greeting = '''\
Welcome to the Tic-Tac-Toe game. 
Here are the rules:
  1. A square, 3 x 3 sized board contains empty cells, every cell has its coordinates as depicted below:
  
               X = 1    X = 2    X = 3
                 |        |        |
      Y = 1 - (1, 1) | (2, 1) | (3, 1)
      Y = 2 - (1, 2) | (2, 2) | (3, 2)
      Y = 3 - (1, 3) | (2, 3) | (3, 3)
      
  2. Each player puts 0 or X on its turn entering cell coordinates. The cell must be unoccupied.
  3. If there are three of a kind (zeroes or crosses) in a row, column, or diagonal, the corresponding player wins. Otherwise, if there are no more empty cells, it is a draw.
'''

# start a game
print(game_greeting)
is_over = False
while not is_over:
    current_game_is_over = False
    print('A new game has started.')
    game_board = game_util.init_game_field()
    current_player = ['O', 'X'][random.randrange(0, 2)]
    while not current_game_is_over:
        are_valid_coordinates = False
        x, y = 0, 0
        while not are_valid_coordinates:
            y, x = game_util.ask_player(current_player)
            are_valid_coordinates = game_util.check_cell_is_empty(x, y, game_board)
        game_board[x - 1][y - 1] = current_player
        game_util.draw_board_colored(game_board)
        if game_util.check_if_player_wins(game_board):
            print(f'Player {current_player} wins the game.')
            current_game_is_over = True
        elif game_util.check_if_board_is_full(game_board):
            print(f'The board has no more empty cells. It is a draw!')
            current_game_is_over = True
        current_player = game_util.swap_player(current_player)
    is_over = not input('Would you like to play one more time? y/n/any: ') == 'y'
print('Thanks for playing!')
