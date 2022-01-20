# import sys
# from io import StringIO
#
# input_1 = """4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4
# """
# input_2 = """5 6
# 1 0 4 3 1 1
# 1 3 1 3 0 4
# 6 4 1 2 5 6
# 2 2 1 5 4 1
# 3 3 3 6 0 5
# """
#
# sys.stdin = StringIO(input_2)

rows, cols = [int(x) for x in input().split()]
m = [[int(x) for x in input().split()] for x in range(rows)]
squares = {}
for i in range(rows - 2):
    for j in range(cols - 2):
        square = [
            m[i][j], m[i][j+1], m[i][j+2],
            m[i+1][j], m[i+1][j+1], m[i+1][j+2],
            m[i+2][j], m[i+2][j+1], m[i+2][j+2]
        ]
        squares[sum(square)] = square

max_sum = max(squares.keys())
the_square = [str(x) for x in squares[max_sum]]
line_1, line_2, line_3 = the_square[:3], the_square[3: 6], the_square[6:]

print(f"Sum = {max_sum}")
print(' '.join(line_1))
print(' '.join(line_2))
print(' '.join(line_3))
