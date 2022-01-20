# import sys
# from io import StringIO
#
# input_1 = """4 6"""
# input_2 = """3 2"""
#
# sys.stdin = StringIO(input_2)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

row, col = [int(x) for x in input().split()]
matrix = []

for i in range(row):
    for j in range(col):
        matrix.append(f"{alphabet[i]}{alphabet[i + j]}{alphabet[i]}")

count = 0
for word in matrix:
    print(word, end=' ')
    count += 1
    if count == col:
        count = 0
        print()
