def even_odd(*args):
    even_nums = []
    odd_nums = []
    command = None
    for x in range(len(args)):
        if x == len(args) - 1:
            command = args[x]
            break
        if int(args[x]) % 2 == 0:
            even_nums.append(args[x])
        else:
            odd_nums.append(args[x])

    if command == 'even':
        return even_nums
    elif command == 'odd':
        return odd_nums


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
