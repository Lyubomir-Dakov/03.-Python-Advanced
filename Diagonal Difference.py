# import sys
# from io import StringIO
#
# input_1 = """3
# 11 2 4
# 4 5 6
# 10 8 -12
# """
# input_2 = """4
# -7 14 9 -20
# 3 4 9 21
# -14 6 8 44
# 30 9 7 -14
# """
#
# sys.stdin = StringIO(input_2)

matrix = [[int(x) for x in input().split(' ')] for x in range(int(input()))]
primary_diagonal = []
secondary_diagonal = []

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if row == col:
            primary_diagonal.append(matrix[row][col])
        if row + col == len(matrix) - 1:
            secondary_diagonal.append(matrix[row][col])

primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)
print(abs(primary_sum - secondary_sum))
