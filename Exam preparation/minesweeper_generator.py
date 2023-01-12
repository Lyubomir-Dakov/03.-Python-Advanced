def count_mines_in_range(the_matrix, r, c, the_size):
    mines_in_range = 0
    if r - 1 >= 0 and c - 1 >= 0 and the_matrix[r - 1][c - 1] == '*':
        mines_in_range += 1
    if r - 1 >= 0 and the_matrix[r - 1][c] == '*':
        mines_in_range += 1
    if r - 1 >= 0 and c + 1 < the_size and the_matrix[r - 1][c + 1] == '*':
        mines_in_range += 1
    if c - 1 >= 0 and the_matrix[r][c - 1] == '*':
        mines_in_range += 1
    if c + 1 < the_size and the_matrix[r][c + 1] == '*':
        mines_in_range += 1
    if r + 1 < the_size and c - 1 >= 0 and the_matrix[r + 1][c - 1] == '*':
        mines_in_range += 1
    if r + 1 < the_size and the_matrix[r + 1][c] == '*':
        mines_in_range += 1
    if r + 1 < the_size and c + 1 < the_size and the_matrix[r + 1][c + 1] == '*':
        mines_in_range += 1
    the_matrix[r][c] = mines_in_range
    return the_matrix


size = int(input())
num_bombs = int(input())

matrix = [[None for y in range(size)] for x in range(size)]

for _ in range(num_bombs):
    row, col = [int(x) for x in input()[1: -1].split(', ')]
    matrix[row][col] = '*'

for r in range(size):
    for c in range(size):
        if matrix[r][c] == '*':
            continue

        count_mines_in_range(matrix, r, c, size)

for line in matrix:
    print(' '.join(str(x) for x in line))

