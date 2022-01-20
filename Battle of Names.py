from math import floor

num = int(input())


def ascii_sum(word: str, the_row: int):
    numbers = [ord(x) for x in word]
    return floor(sum(numbers) / the_row)


even_set = set()
odd_set = set()

for row in range(1, num + 1):
    name = input()
    special_number = ascii_sum(name, row)
    if special_number % 2 == 0:
        even_set.add(special_number)
    else:
        odd_set.add(special_number)

if sum(even_set) == sum(odd_set):
    the_union = [str(x) for x in even_set.union(odd_set)]
    print(', '.join(the_union))
elif sum(even_set) > sum(odd_set):
    the_symmetric_dif = [str(x) for x in even_set.symmetric_difference(odd_set)]
    print(', '.join(the_symmetric_dif))
else:
    the_different = [str(x) for x in odd_set.difference(even_set)]
    print(', '.join(the_different))
