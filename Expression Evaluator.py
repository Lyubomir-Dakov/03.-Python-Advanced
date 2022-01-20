from collections import deque
from math import floor
# import sys
# from io import StringIO
#
# input_1 = """6 3 - 2 1 * 5 /
# """
# input_2 = """2 2 - 1 *
# """
# input_3 = """10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *
# """
#
# sys.stdin = StringIO(input_1)


def add_operator(sequence: deque):
    result = sequence.popleft()
    while sequence:
        result += sequence.popleft()
    return sequence.append(result)


def minus_operator(sequence: deque):
    result = sequence.popleft()
    while sequence:
        result -= sequence.popleft()
    return sequence.append(result)


def multiply_operator(sequence: deque):
    result = sequence.popleft()
    while sequence:
        result *= sequence.popleft()
    return sequence.append(result)


def divide_operator(sequence: deque):
    result = sequence.popleft()
    while sequence:
        result = floor(result / sequence.popleft())
    return sequence.append(result)


data = deque(input().split())
my_stack = deque()

while data:
    if data[0] in '+-*/':
        operator = data.popleft()
        if operator == '+':
            add_operator(my_stack)
        elif operator == '-':
            minus_operator(my_stack)
        elif operator == '*':
            multiply_operator(my_stack)
        elif operator == '/':
            divide_operator(my_stack)
    else:
        my_stack.append(int(data.popleft()))

print(my_stack[0])
