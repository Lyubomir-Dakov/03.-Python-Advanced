# import sys
# from io import StringIO
#
# input_1 = """3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
# """
#
# sys.stdin = StringIO(input_1)

matrix = [[int(x) for x in input().split(', ')] for x in range(int(input()))]
primary_diagonal = []
secondary_diagonal = []

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if row == col:
            primary_diagonal.append(matrix[row][col])
        if row + col == len(matrix) - 1:
            secondary_diagonal.append(matrix[row][col])

primary_sum = sum(primary_diagonal)
secondary_sum = sum(secondary_diagonal)
primary_diagonal = ', '.join(str(x) for x in primary_diagonal)
secondary_diagonal = ', '.join(str(x) for x in secondary_diagonal)
print(f"Primary diagonal: {primary_diagonal}. Sum: {primary_sum}")
print(f"Secondary diagonal: {secondary_diagonal}. Sum: {secondary_sum}")
