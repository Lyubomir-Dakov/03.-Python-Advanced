num = int(input())
chemicals = set()
for _ in range(num):
    data = set(input().split(' '))
    chemicals.update(data)

[print(x) for x in chemicals]