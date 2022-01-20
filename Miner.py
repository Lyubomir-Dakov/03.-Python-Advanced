from collections import deque

# import sys
# from io import StringIO
#
# input_1 = """5
# up right right up right
# * * * c *
# * * * e *
# * * c * *
# s * * c *
# * * c * *
# """
#
# input_2 = """4
# up right right right down
# * * * e
# * * c *
# * s * c
# * * * *
# """
#
# input_3 = """6
# left left down right up left left down down down
# * * * * * *
# e * * * c *
# * * c s * *
# * * * * * *
# c * * * c *
# * * c * * *
# """
#
# sys.stdin = StringIO(input_2)


def find_all_coals(the_matrix: list, the_size):
    coals = 0
    for row in range(the_size):
        for col in range(the_size):
            if the_matrix[row][col] == 'c':
                coals += 1
    return coals


def find_current_position(the_matrix: list, the_size):
    for row in range(the_size):
        for col in range(the_size):
            if the_matrix[row][col] == 's':
                return [row, col]


def up_command(the_matrix: list, position: list):
    if position[0] - 1 >= 0:
        new_position = [position[0] - 1, position[1]]
        the_matrix[position[0]][position[1]] = '*'
        return the_matrix, new_position
    else:
        return the_matrix, position


def down_command(the_matrix: list, position: list, the_size: int):
    if position[0] + 1 < the_size:
        new_position = [position[0] + 1, position[1]]
        the_matrix[position[0]][position[1]] = '*'
        return the_matrix, new_position
    else:
        return the_matrix, position


def left_command(the_matrix: list, position: list):
    if position[1] - 1 >= 0:
        new_position = [position[0], position[1] - 1]
        the_matrix[position[0]][position[1]] = '*'
        return the_matrix, new_position
    else:
        return the_matrix, position


def right_command(the_matrix: list, position: list, the_size: int):
    if position[1] + 1 < the_size:
        new_position = [position[0], position[1] + 1]
        the_matrix[position[0]][position[1]] = '*'
        return the_matrix, new_position
    else:
        return the_matrix, position


def check_new_position(the_matrix: list, position: list, coals: int, game_state: bool):
    r, c = position
    if the_matrix[r][c] == 'e':
        print(f"Game over! ({r}, {c})")
        game_state = True
    elif the_matrix[r][c] == 'c':
        matrix[r][c] = 's'
        coals -= 1
        if coals == 0:
            print(f"You collected all coal! ({r}, {c})")
            game_state = True
    elif the_matrix[r][c] == '*':
        matrix[r][c] = 's'
    return the_matrix, coals, game_state


size = int(input())
commands = deque(input().split())
matrix = [[x for x in input().split()] for row in range(size)]
current_position = find_current_position(matrix, size)
end_game = False
all_coals = find_all_coals(matrix, size)

while commands:
    if end_game:
        break
    current_command = commands.popleft()
    if current_command == 'up':
        matrix, current_position = up_command(matrix, current_position)
    elif current_command == 'down':
        matrix, current_position = down_command(matrix, current_position, size)
    elif current_command == 'left':
        matrix, current_position = left_command(matrix, current_position)
    elif current_command == 'right':
        matrix, current_position = right_command(matrix, current_position, size)

    matrix, all_coals, end_game = check_new_position(matrix, current_position, all_coals, end_game)

if not end_game:
    r, c = current_position
    print(f"{all_coals} pieces of coal left. ({r}, {c})")
