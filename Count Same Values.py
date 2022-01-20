numbers = [float(x) for x in input().split(' ')]
numbers_and_occurrences = {}

for num in numbers:
    if num not in numbers_and_occurrences:
        numbers_and_occurrences[num] = 0
    numbers_and_occurrences[num] += 1

for number, occurrence in numbers_and_occurrences.items():
    print(f"{number:.1f} - {occurrence} times")
