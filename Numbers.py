line_1 = [int(x) for x in input().split(' ')]
line_2 = [int(x) for x in input().split(' ')]
num = int(input())

for _ in range(num):
    data = input()
    if data == 'Check Subset':
        set_1 = set(line_1)
        set_2 = set(line_2)
        if set_1.issubset(set_2) or set_2.issubset(set_1):
            print(True)
        else:
            print(False)
    else:
        word_1, word_2, numbers = data.split(' ', 2)
        command = word_1 + ' ' + word_2
        numbers = [int(x) for x in numbers.split()]
        if command == 'Add First':
            line_1.extend(numbers)
            a = 5
        elif command == 'Add Second':
            line_2.extend(numbers)
        elif command == 'Remove First':
            for num in numbers:
                while num in line_1:
                    line_1.remove(num)
        elif command == 'Remove Second':
            for num in numbers:
                while num in line_2:
                    line_2.remove(num)

line_1 = list(set(line_1))
line_2 = list(set(line_2))
sorted_line_1 = [str(x) for x in sorted(line_1)]
sorted_line_2 = [str(x) for x in sorted(line_2)]

print(', '.join(sorted_line_1))
print(', '.join(sorted_line_2))
