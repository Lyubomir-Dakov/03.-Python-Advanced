command = input()
numbers = [int(x) for x in input().split()]

parity = 0 if command == 'Even' else 1
result = sum(filter(lambda x: x % 2 == parity, numbers))
print(result * len(numbers))
