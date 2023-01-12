# import sys
# from io import StringIO
#
# input_1 = """10 30 B 4 20 24
# 7 8 27 23 11 19
# 13 3 14 B 17 В
# 12 5 21 22 9 6
# B 26 1 28 29 2
# 25 B 16 15 B 18
# (1, 1)
# (20, 15)
# (4, 0)
# """
#
# input_2 = """B 30 14 23 20 24
# 29 8 27 18 11 19
# 13 3 B B 17 6
# 28 5 21 22 9 B
# 10 B 26 12 B 2
# 25 1 16 15 7 4
# (0, 0)
# (2, 2)
# (2, 3)
# """
#
# sys.stdin = StringIO(input_1)

matrix = [[int(y) if y.isdigit() else y for y in input().split()] for x in range(6)]

collected_points = 0

for _ in range(3):
    rol, cow = [int(x) for x in input()[1:-1].split(', ')]

    if rol < 0 or rol > 5 or cow < 0 or cow > 5 or matrix[rol][cow] != 'B':
        continue

    matrix[rol][cow] = 0
    for num in range(6):
        collected_points += matrix[num][cow]

if collected_points < 100:
    needed_points = 100 - collected_points
    print(f"Sorry! You need {needed_points} points more to win a prize.")
elif 100 <= collected_points <= 199:
    print(f"Good job! You scored {collected_points} points, and you've won Football.")
elif 200 <= collected_points <= 299:
    print(f"Good job! You scored {collected_points} points, and you've won Teddy Bear.")
elif 300 <= collected_points:
    print(f"Good job! You scored {collected_points} points, and you've won Lego Construction Set.")
