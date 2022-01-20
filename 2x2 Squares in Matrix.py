# import sys
# from io import StringIO
#
# input_1 = """3 4
# A B B D
# E B B B
# I J B B
# """
# input_2 = """2 2
# a b
# c d
# """
# input_3 = """5 4
# A A B D
# A A B B
# I J B B
# C C C G
# C C K P
# """
#
# sys.stdin = StringIO(input_3)

rows, cols = [int(x) for x in input().split()]
matrix = [[x for x in input().split()] for x in range(rows)]
count = 0

for i in range(rows - 1):
    for j in range(cols - 1):
        if matrix[i][j] == matrix[i + 1][j] == matrix[i][j + 1] == matrix[i + 1][j + 1]:
            count += 1
print(count)

