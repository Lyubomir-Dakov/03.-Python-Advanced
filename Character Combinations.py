# import sys
# from io import StringIO
#
# input_1 = """abc"""
# input_2 = """12"""
#
# sys.stdin = StringIO(input_1)

my_data = list(input())


def permutations(index, data):
    if index == len(data):
        print(''.join(data))
        return
    for i in range(index, len(data)):
        data[i], data[index] = data[index], data[i]
        permutations(index + 1, data)
        data[i], data[index] = data[index], data[i]


permutations(0, my_data)
