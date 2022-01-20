# import sys
# from io import  StringIO
#
# input_1 = """1 2 -3 -4 65 -98 12 57 -84"""
# input_2 = """1 2 3"""
#
# sys.stdin = StringIO(input_2)


def split_numbers(*args):
    positive_nums = []
    negative_nums = []
    for x in args:
        if x <= 0:
            negative_nums.append(x)
        else:
            positive_nums.append(x)

    return positive_nums, negative_nums


data = [int(x) for x in input().split()]

positive, negative = split_numbers(*data)
negative_sum, positive_sum = sum(negative), sum(positive)
print(negative_sum)
print(positive_sum)
if abs(negative_sum) > abs(positive_sum):
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")

