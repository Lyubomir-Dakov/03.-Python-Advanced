# import sys
# from io import StringIO
#
# input_1 = """3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0
# """
# input_2 = """3, 3
# 1 2 3
# 4 5 6
# 7 8 9
# """
#
# sys.stdin = StringIO(input_2)

rows, cols = [int(x) for x in input().split(', ')]
result = [0]*cols

for _ in range(rows):
    row = [int(x) for x in input().split()]
    count = 0
    for num in row:
        result[count] += num
        count += 1

[print(x) for x in result]
