# import sys
# from io import StringIO
#
# input_1 = """1 2 3 |4 5 6 |  7               88"""
# input_2 = """7 | 4  5|1 0| 2 5 |3"""
# input_3 = """1| 4 5 6 7  |  8 9"""
#
# sys.stdin = StringIO(input_1)

result = []
data = [[y for y in x.split()] for x in input().split('|')]
data = data[::-1]
for x in data:
    result += x

print(' '.join(result))


