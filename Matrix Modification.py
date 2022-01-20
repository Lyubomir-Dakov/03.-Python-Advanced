# import sys
# from io import StringIO
#
# input_1 = """3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END
# """
#
# input_2 = """4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END
# """
#
# sys.stdin = StringIO(input_2)


def add_value(the_matrix: list, the_row: int, the_col: int, the_value: int):
    the_matrix[the_row][the_col] += the_value
    return the_matrix


def subtract_value(the_matrix: list, the_row: int, the_col: int, the_value: int):
    the_matrix[the_row][the_col] -= the_value
    return the_matrix


size = int(input())
matrix = [[int(y) for y in input().split()] for x in range(size)]

new_line = input()
while not new_line == 'END':
    data = new_line.split()
    command, row, col, value = data[0], int(data[1]), int(data[2]), int(data[3])
    if row not in range(size) or col not in range(size):
        print("Invalid coordinates")
        new_line = input()
        continue
    if command == 'Add':
        add_value(matrix, row, col, value)
    elif command == 'Subtract':
        subtract_value(matrix, row, col, value)
    new_line = input()

for row in matrix:
    print(' '.join([str(x) for x in row]))
