n, m = [int(x) for x in input().split(' ')]
set_1 = {int(input()) for x in range(n)}
set_2 = {int(input()) for x in range(m)}
[print(x) for x in set_1.intersection(set_2)]
