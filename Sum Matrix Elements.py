# import sys
# from io import StringIO
#
# input_1 = """3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
# """
#
# sys.stdin = StringIO(input_1)

rows, cows = [int(x) for x in input().split(', ')]
matrix = []
total_sum = 0

for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)
    total_sum += sum(row)

print(total_sum)
print(matrix)
