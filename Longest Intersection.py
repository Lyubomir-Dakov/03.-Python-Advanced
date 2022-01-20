def create_list_of_numbers(start: int, end: int):
    my_set = {x for x in range(start, end + 1)}
    return my_set


num = int(input())
last_result = ''

for _ in range(num):
    range_1, range_2 = input().split('-')

    start_1, end_1 = [int(x) for x in range_1.split(',')]
    set_1 = create_list_of_numbers(start_1, end_1)

    start_2, end_2 = [int(x) for x in range_2.split(',')]
    set_2 = create_list_of_numbers(start_2, end_2)

    result = set_1.intersection(set_2)
    if len(last_result) < len(result):
        last_result = result

print(f"Longest intersection is {list(last_result)} with length {len(last_result)}")
