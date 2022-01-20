from collections import deque

# import sys
# from io import StringIO
#
# input_1 = """5 6
# SoftUni
# """
# input_2 = """1 4
# Python
# """
#
# sys.stdin = StringIO(input_2)

rows, cols = [int(x) for x in input().split()]
matrix = [['' for y in range(cols)] for x in range(rows)]
data = deque([x for x in input()])

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = data[0]
        data.append(data.popleft())

for num in range(rows):
    if num % 2 == 0:
        print(''.join(matrix[num]))
    else:
        print(''.join(matrix[num][::-1]))
