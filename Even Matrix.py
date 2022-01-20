# import sys
# from io import StringIO
#
# input_1 = """2
# 1, 2, 3
# 4, 5, 6
# """
# input_2 = """4
# 10, 33, 24, 5, 1
# 67, 34, 11, 110, 3
# 4, 12, 33, 63, 21
# 557, 45, 23, 55, 67
# """
#
# sys.stdin = StringIO(input_2)

result = [[x for x in [int(x) for x in input().split(', ')] if x % 2 == 0] for x in range(int(input()))]
print(result)