# import sys
# from io import StringIO
#
# input_1 = """2
# 1, 2, 3
# 4, 5, 6
# """
# input_2 = """3
# 10, 2, 21, 4
# 5, 20, 41, 9
# 6, 2, 4, 99
# """
#
# sys.stdin = StringIO(input_2)

rows = int(input())
result = []

for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    result += row

print(result)
