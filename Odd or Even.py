# import sys
# from io import StringIO
#
# input_1 = """Odd
# 1 3 5 34 7 9 12 11 13 10
# """
#
# input_2 = """Even
# 1 3 5 7 9 13
# """
#
# sys.stdin = StringIO(input_2)


def split_numbers(*args):
    odd_nums = []
    even_nums = []
    for x in args:
        if x % 2 == 0:
            even_nums.append(x)
        else:
            odd_nums.append(x)

    return sum(even_nums), sum(odd_nums)


command = input()
numbers = [int(x) for x in input().split()]
even_sum, odd_sum = split_numbers(*numbers)

if command == 'Odd':
    result = odd_sum * len(numbers)
    print(result)
elif command == 'Even':
    result = even_sum * len(numbers)
    print(result)
