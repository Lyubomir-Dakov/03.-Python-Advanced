data = input()
my_dict = {}

for ch in data:
    if ch not in my_dict:
        my_dict[ch] = 0
    my_dict[ch] += 1

sorted_dict = sorted(my_dict.items(), key=lambda kvp: kvp[0])
[print(f"{x}: {y} time/s") for x, y in sorted_dict]
