# import sys
# from io import StringIO
#
# input_1 = """2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END
# """
#
# input_2 = """1 2
# Hello World
# 0 0 0 1
# swap 0 0 0 1
# swap 0 1 0 0
# END
# """
#
# sys.stdin = StringIO(input_1)


def print_the_matrix(my_matrix: list):
    for row in my_matrix:
        print(' '.join(row))


rows, cols = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for x in range(rows)]

while True:
    new_line = input()
    if new_line == 'END':
        break
    data = new_line.split()
    if not data[0] == 'swap':
        print('Invalid input!')
        continue
    try:
        r_1, c_1, r_2, c_2 = [int(x) for x in data[1:]]
        matrix[r_1][c_1], matrix[r_2][c_2] = matrix[r_2][c_2], matrix[r_1][c_1]
        print_the_matrix(matrix)
    except:
        print('Invalid input!')
