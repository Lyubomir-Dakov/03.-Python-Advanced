import sys
from io import StringIO

input_1 = """Peter, George, Amy
2
"""

input_2 = """Mariya, Emilly, Tom, Bob
1
"""

sys.stdin = StringIO(input_1)

names = input().split(', ')
chairs = int(input())


def combination(data: list, index: int, count: int, result: list):
    if len(result) == count:
        print(result)
        return

    for i in range(index, len(data)):
        result.append(data[i])
        combination(data, i + 1, count, result)
        result.pop()


combination(names, 0, 2, [])
