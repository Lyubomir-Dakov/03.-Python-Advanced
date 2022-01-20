# import sys
# from io import StringIO
#
# input_1 = """3
# 11 2 4
# 4 5 6
# 10 8 -12
# """
# input_2 = """3
# 1 2 3
# 4 5 6
# 7 8 9
# """
#
# sys.stdin = StringIO(input_2)

size = int(input())
diagonal_sum = 0

for ind in range(size):
    row = [int(x) for x in input().split()]
    diagonal_sum += row[ind]

print(diagonal_sum)
