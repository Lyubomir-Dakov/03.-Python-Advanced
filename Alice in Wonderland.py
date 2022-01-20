# import sys
# from io import StringIO
#
# input_1 = """5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# right
# left
# down
# up
# left
# """
#
# input_2 = """7
# . A . 1 1 . .
# 9 . . . 6 . 5
# . 6 . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
# left
# down
# down
# right
# """
#
# sys.stdin = StringIO(input_2)


class Alice:
    def __init__(self):
        self.tea = 0


def find_alice_and_rabit_locations(the_matrix: list, the_size: int):
    alice_location = None
    rabbit_location = None
    for r in range(the_size):
        for c in range(the_size):
            if the_matrix[r][c] == 'A':
                alice_location = [r, c]
            elif the_matrix[r][c] == 'R':
                rabbit_location = [r, c]
            if alice_location and rabbit_location:
                break
    return alice_location, rabbit_location


def up_command(the_matrix: list, a_position: list, r_position: list, end_game: bool, the_tea):
    x, y = r_position
    r, c = a_position
    if r - 1 >= 0:
        if r - 1 == x and c == y:
            the_matrix[r - 1][c] = '*'
            end_game = True
        else:
            if the_matrix[r - 1][c].isdigit():
                the_tea += int(the_matrix[r - 1][c])
            the_matrix[r - 1][c] = 'A'
            a_position = [r - 1, c]
    else:
        end_game = True
    the_matrix[r][c] = '*'
    return the_matrix, a_position, end_game, the_tea


def down_command(the_matrix: list, the_size: int, a_position: list, r_position: list, end_game: bool, the_tea):
    x, y = r_position
    r, c = a_position
    if r + 1 < the_size:
        if r + 1 == x and c == y:
            the_matrix[r + 1][c] = '*'
            end_game = True
        else:
            if the_matrix[r + 1][c].isdigit():
                the_tea += int(the_matrix[r + 1][c])
            the_matrix[r + 1][c] = 'A'
            a_position = [r + 1, c]
    else:
        end_game = True
    the_matrix[r][c] = '*'
    return the_matrix, a_position, end_game, the_tea


def left_command(the_matrix: list, a_position: list, r_position: list, end_game: bool, the_tea):
    x, y = r_position
    r, c = a_position
    if c - 1 >= 0:
        if r == x and c - 1 == y:
            the_matrix[r][c - 1] = '*'
            end_game = True
        else:
            if the_matrix[r][c - 1].isdigit():
                the_tea += int(the_matrix[r][c - 1])
            the_matrix[r][c - 1] = 'A'
            a_position = [r, c - 1]
    else:
        end_game = True
    the_matrix[r][c] = '*'
    return the_matrix, a_position, end_game, the_tea


def right_command(the_matrix: list, the_size: int, a_position: list, r_position: list, end_game: bool, the_tea):
    x, y = r_position
    r, c = a_position
    if c + 1 < the_size:
        if r == x and c + 1 == y:
            the_matrix[r][c + 1] = '*'
            end_game = True
        else:
            if the_matrix[r][c + 1].isdigit():
                the_tea += int(the_matrix[r][c + 1])
            the_matrix[r][c + 1] = 'A'
            a_position = [r, c + 1]
    else:
        end_game = True
    the_matrix[r][c] = '*'
    return the_matrix, a_position, end_game, the_tea


size = int(input())
matrix = [[y for y in input().split()] for x in range(size)]
alice_loc, rabbit = find_alice_and_rabit_locations(matrix, size)
alice = Alice()
game_ends = False

while True:
    if alice.tea >= 10:
        print("She did it! She went to the party.")
        matrix[alice_loc[0]][alice_loc[1]] = '*'
        break
    if game_ends:
        print("Alice didn't make it to the tea party.")
        break
    command = input()
    if command == 'up':
        matrix, alice_loc, game_ends, alice.tea = up_command(matrix, alice_loc, rabbit, game_ends, alice.tea)
    elif command == 'down':
        matrix, alice_loc, game_ends, alice.tea = down_command(matrix, size, alice_loc, rabbit, game_ends, alice.tea)
    elif command == 'left':
        matrix, alice_loc, game_ends, alice.tea = left_command(matrix, alice_loc, rabbit, game_ends, alice.tea)
    elif command == 'right':
        matrix, alice_loc, game_ends, alice.tea = right_command(matrix, size, alice_loc, rabbit, game_ends, alice.tea)

for x in matrix:
    print(' '.join(x))
