# import sys
# from io import StringIO
#
# input_1 = """3
# ABC
# DEF
# X!@
# !
# """
# input_2 = """4
# asdd
# xczc
# qwee
# qefw
# 4
# """
#
# sys.stdin = StringIO(input_2)

square_size = int(input())
matrix = []

for _ in range(square_size):
    row = input()
    matrix.append(row)

symbol = input()
found_symbol = False

row = 0
for i in matrix:
    col = 0
    for j in i:
        if matrix[row][col] == symbol:
            print(f"({row}, {col})")
            found_symbol = True
        col += 1
    if found_symbol:
        break
    row += 1

if not found_symbol:
    print(f"{symbol} does not occur in the matrix")
