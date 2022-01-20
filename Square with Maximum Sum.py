# import sys
# from io import StringIO
#
# input_1 = """3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
# """
# input_2 = """2, 4
# 10, 11, 12, 13
# 14, 15, 16, 17
# """
#
# sys.stdin = StringIO(input_2)

rows, cols = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for x in range(rows)]

squares = {}

for i in range(rows - 1):
    for j in range(cols - 1):
        current_square = [matrix[i][j], matrix[i][j + 1], matrix[i + 1][j], matrix[i + 1][j + 1]]
        if sum(current_square) not in squares:
            squares[sum(current_square)] = current_square

max_sum = max(squares.keys())
my_square = [str(x) for x in squares[max_sum]]
left_part = ' '.join(my_square[:2])
right_part = ' '.join(my_square[2:])
print(left_part)
print(right_part)
print(max_sum)

