from collections import deque
import operator

import sys
from io import StringIO

input_1 = """5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0
"""

input_2 = """8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22
"""

sys.stdin = StringIO(input_2)


class PossibleWay:
    def __init__(self, name):
        self.name = name
        self.eggs = 0
        self.steps = None


def find_bunny_location(the_matrix: list, the_size: int):
    for r in range(the_size):
        for c in range(the_size):
            if the_matrix[r][c] == 'B':
                return [r, c]


def up_way(the_matrix: list, position: list):
    r, c = position
    the_collected_eggs = 0
    each_step_up_direction = []
    count = 1
    while r - count >= 0:
        next_step = the_matrix[r - count][c]
        if next_step == 'X':
            break
        the_collected_eggs += next_step
        each_step_up_direction.append([r - count, c])
        count += 1
    return the_collected_eggs, each_step_up_direction


def down_way(the_matrix: list, position: list, the_size: int):
    r, c = position
    the_collected_eggs = 0
    each_step_up_direction = []
    count = 1
    while r + count < the_size:
        next_step = the_matrix[r + count][c]
        if next_step == 'X':
            break
        the_collected_eggs += next_step
        each_step_up_direction.append([r + count, c])
        count += 1
    return the_collected_eggs, each_step_up_direction


def left_way(the_matrix: list, position: list):
    r, c = position
    the_collected_eggs = 0
    each_step_up_direction = []
    count = 1
    while c - count >= 0:
        next_step = the_matrix[r][c - count]
        if next_step == 'X':
            break
        the_collected_eggs += next_step
        each_step_up_direction.append([r, c - count])
        count += 1
    return the_collected_eggs, each_step_up_direction


def right_way(the_matrix: list, position: list, the_size: int):
    r, c = position
    the_collected_eggs = 0
    each_step_up_direction = []
    count = 1
    while c + count < the_size:
        next_step = the_matrix[r][c + count]
        if next_step == 'X':
            break
        the_collected_eggs += next_step
        each_step_up_direction.append([r, c + count])
        count += 1
    return the_collected_eggs, each_step_up_direction


size = int(input())
matrix = [[int(y) if y.isdigit() else y for y in input().split()] for x in range(size)]
location = find_bunny_location(matrix, size)
possible_directions = ['up', 'down', 'left', 'right']
result = deque()

for command in possible_directions:
    if command == 'up':
        way_up = PossibleWay('up')
        way_up.eggs, way_up.steps = up_way(matrix, location)
        result.append(way_up)
    elif command == 'down':
        way_down = PossibleWay('down')
        way_down.eggs, way_down.steps = down_way(matrix, location, size)
        result.append(way_down)
    elif command == 'left':
        way_left = PossibleWay('left')
        way_left.eggs, way_left.steps = left_way(matrix, location)
        result.append(way_left)
    elif command == 'right':
        way_right = PossibleWay('right')
        way_right.eggs, way_right.steps = right_way(matrix, location, size)
        result.append(way_right)

sorted_result = deque(sorted(result, key=operator.attrgetter('eggs')))

last_result = sorted_result.pop()
print(last_result.name)
for x in last_result.steps:
    print(x)
print(last_result.eggs)


