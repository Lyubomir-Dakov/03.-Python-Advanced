line_8 = ['a1', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1']
line_7 = ['a2', 'b2', 'c2', 'd2', 'e2', 'f2', 'g2', 'h2']
line_6 = ['a3', 'b3', 'c3', 'd3', 'e3', 'f3', 'g3', 'h3']
line_5 = ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'h4']
line_4 = ['a5', 'b5', 'c5', 'd5', 'e5', 'f5', 'g5', 'h5']
line_3 = ['a6', 'b6', 'c6', 'd6', 'e6', 'f6', 'g6', 'h6']
line_2 = ['a7', 'b7', 'c7', 'd7', 'e7', 'f7', 'g7', 'h7']
line_1 = ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']
matrix_2 = [line_1] + [line_2] + [line_3] + [line_4] + [line_5] + [line_6] + [line_7] + [line_8]

matrix = [[y for y in input().split()]for x in range(8)]

white_r, white_c = None, None
black_r, black_c = None, None

for r in range(8):
    for c in range(8):
        if matrix[r][c] == 'w':
            white_r, white_c = r, c
        if matrix[r][c] == 'b':
            black_r, black_c = r, c

white_won = False
black_won = False


while True:
    if white_r == 0:
        print(f"Game over! White pawn is promoted to a queen at {matrix_2[white_r][white_c]}.")
        white_won = True
        break

    if white_c - 1 >= 0 and matrix[white_r -1][white_c - 1] == 'b':
        print(f"Game over! White win, capture on {matrix_2[white_r - 1][white_c -1]}.")
        white_won = True
        break

    if white_c + 1 < 8 and matrix[white_r - 1][white_c + 1] == 'b':
        print(f"Game over! White win, capture on {matrix_2[white_r - 1][white_c + 1]}.")
        white_won = True
        break

    matrix[white_r][white_c] = '-'
    white_r, white_c = white_r - 1, white_c
    matrix[white_r][white_c] = 'w'

    if black_r == 7:
        print(f"Game over! Black pawn is promoted to a queen at {matrix_2[black_r][black_c]}.")
        black_won = True
        break

    if black_c - 1 >= 0 and matrix[black_r + 1][black_c - 1] == 'w':
        print(f"Game over! Black win, capture on {matrix_2[black_r + 1][black_c - 1]}.")
        black_won = True
        break

    if black_c + 1 < 7 and matrix[black_r + 1][black_c + 1] == 'w':
        print(f"Game over! Black win, capture on {matrix_2[black_r + 1][black_c + 1]}.")
        black_won = True

    matrix[black_r][black_c] = '-'
    black_r, black_c = black_r + 1, black_c
    matrix[black_r][black_c] = 'b'





