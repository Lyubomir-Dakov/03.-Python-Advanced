from collections import deque

# import sys
# from io import StringIO
#
# input_1 = """5 6
# .....P
# ......
# ...B..
# ......
# ......
# ULDDDR
# """
#
# input_2 = """4 5
# .....
# .....
# .B...
# ...P.
# LLLLLLLL
# """
#
# input_3 = """5 8
# .......B
# ...B....
# ....B..B
# ........
# ..P.....
# ULLL
# """
#
# sys.stdin = StringIO(input_2)


def find_current_location(the_matrix: list, the_rows: int, the_cols: int):
    for r in range(the_rows):
        for c in range(the_cols):
            if the_matrix[r][c] == 'P':
                return [r, c]


def check_current_position(the_matrix: list, the_position: list, if_lose: bool, if_win: bool):
    r, c = the_position
    if the_matrix[r][c] == 'B':
        if_lose = True
    else:
        the_matrix[r][c] = 'P'
    return the_matrix, if_lose


def spread_rabbits(the_matrix: list, player_position: list, the_rows: int, the_cols: int, if_lose: bool):
    new_bunnies = set()
    for r in range(the_rows):
        for c in range(the_cols):
            if the_matrix[r][c] == 'B':
                # add bunny top
                if r - 1 >= 0:
                    new_bunnies.add((r - 1, c))
                # add bunny down
                if r + 1 < the_rows:
                    new_bunnies.add((r + 1, c))
                # add bunny left
                if c - 1 >= 0:
                    new_bunnies.add((r, c - 1))
                # add bunny right
                if c + 1 < the_cols:
                    new_bunnies.add((r, c + 1))
    player_r, player_c = player_position
    if (player_r, player_c) in new_bunnies:
        if_lose = True
    for cords in new_bunnies:
        r, c = cords
        the_matrix[r][c] = 'B'
    return the_matrix, if_lose


def left_command(the_matrix: list, the_position: list, if_win: bool):
    r, c = the_position
    if c - 1 >= 0:
        the_position = [r, c - 1]
    else:
        if_win = True
    the_matrix[r][c] = '.'
    return the_matrix, the_position, if_win


def right_command(the_matrix: list, the_position: list, the_col_size: int, if_win: bool):
    r, c = the_position
    if c + 1 < the_col_size:
        the_position = [r, c + 1]
    else:
        if_win = True
    the_matrix[r][c] = '.'
    return the_matrix, the_position, if_win


def up_command(the_matrix: list, the_position: list, if_win: bool):
    r, c = the_position
    if r - 1 >= 0:
        the_position = [r - 1, c]
    else:
        if_win = True
    the_matrix[r][c] = '.'
    return the_matrix, the_position, if_win


def down_command(the_matrix: list, the_position: list, the_row_count: int, if_win: bool):
    r, c = the_position
    if r + 1 < the_row_count:
        the_position = [r + 1, c]
    else:
        if_win = True
    the_matrix[r][c] = '.'
    return the_matrix, the_position, if_win


rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input()] for x in range(rows)]
commands = deque(x for x in input())
current_location = find_current_location(matrix, rows, cols)
played_turns = 0
win_game = False
lose_game = False

while commands:
    if win_game or lose_game:
        break
    current_command = commands.popleft()
    # The player makes a move
    if current_command == 'L':
        matrix, current_location, win_game = left_command(matrix, current_location, win_game)
    elif current_command == 'R':
        matrix, current_location, win_game = right_command(matrix, current_location, cols, win_game)
    elif current_command == 'U':
        matrix, current_location, win_game = up_command(matrix, current_location, win_game)
    elif current_command == 'D':
        matrix, current_location, win_game = down_command(matrix, current_location, rows, win_game)
    # check if player went out of the field (win_game) or step on rabbit (lose_game)
    if not win_game:
        matrix, lose_game = check_current_position(matrix, current_location, lose_game, win_game)
    # spread the rabbits and check if rabbit steps on the player
    matrix, lose_game = spread_rabbits(matrix, current_location, rows, cols, lose_game)

for row in matrix:
    row = ''.join(row)
    print(row)
row, col = current_location
if win_game:
    print(f"won: {row} {col}")
if lose_game:
    print(f"dead: {row} {col}")
