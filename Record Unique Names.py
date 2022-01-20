names = int(input())
all_names = []

for num in range(names):
    name = input()
    if name not in all_names:
        all_names.append(name)

for name in all_names:
    print(name)
