from collections import deque

# import sys
# from io import StringIO
#
# input_1 = """4
# 8 3 2 5
# 6 4 7 9
# 9 9 3 6
# 6 8 1 2
# 1,2 2,1 2,0
# """
#
# input_2 = """3
# 7 8 4
# 3 1 5
# 6 4 9
# 0,2 1,0 2,2
# """
#
# sys.stdin = StringIO(input_2)


def bomb_explode(the_matrix: list, the_bomb: list, all_bombs: deque):
    row, col = the_bomb
    if the_matrix[row][col] <= 0:
        return the_matrix
    damage, the_matrix[row][col] = the_matrix[row][col], 0
    try:
        if matrix[row - 1][col - 1] > 0 and row - 1 >= 0 and col - 1 >= 0:
            matrix[row - 1][col - 1] -= damage
    except:
        pass
    try:
        if matrix[row - 1][col] > 0 and row - 1 >= 0 and col >= 0:
            matrix[row - 1][col] -= damage
    except:
        pass
    try:
        if matrix[row - 1][col + 1] > 0 and row - 1 >= 0 and col + 1 >= 0:
            matrix[row - 1][col + 1] -= damage
    except:
        pass
    try:
        if matrix[row][col - 1] > 0 and row >= 0 and col - 1 >= 0:
            matrix[row][col - 1] -= damage
    except:
        pass
    try:
        if matrix[row][col + 1] > 0 and row >= 0 and col + 1 >= 0:
            matrix[row][col + 1] -= damage
    except:
        pass
    try:
        if matrix[row + 1][col - 1] > 0 and row + 1 >= 0 and col - 1 >= 0:
            matrix[row + 1][col - 1] -= damage
    except:
        pass
    try:
        if matrix[row + 1][col] > 0 and row + 1 >= 0 and col >= 0:
            matrix[row + 1][col] -= damage
    except:
        pass
    try:
        if matrix[row + 1][col + 1] > 0 and row + 1 >= 0 and col + 1 >= 0:
            matrix[row + 1][col + 1] -= damage
    except:
        pass
    return the_matrix


size = int(input())
matrix = [[int(x) for x in input().split()] for x in range(size)]
bombs = deque([int(y) for y in x.split(',')] for x in input().split())
while bombs:
    current_bomb = bombs.popleft()
    bomb_explode(matrix, current_bomb, bombs)

alive_cells = []
for r in range(size):
    for c in range(size):
        if matrix[r][c] > 0:
            alive_cells.append(matrix[r][c])

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
for row in matrix:
    row = ' '.join([str(x) for x in row])
    print(row)

