from collections import deque
from itertools import islice

# import sys
# from io import StringIO
#
# input_1 = """d yel blu e low redd"""
# input_2 = """r ue nge ora bl ed"""
# input_3 = """re ple blu pop e pur d"""
#
# sys.stdin = StringIO(input_1)


def add_elements_at_the_middle(main_data: deque, sub_str_1, sub_str_2):
    need_to_add = deque()
    if sub_str_1 == sub_str_2 == "":
        return main_data
    elif sub_str_1 == "":
        need_to_add.append(sub_str_2)
    elif sub_str_2 == "":
        need_to_add.append(sub_str_1)
    else:
        need_to_add.append(sub_str_1)
        need_to_add.append(sub_str_2)

    if len(main_data) % 2 == 0:
        left_part = deque(islice(main_data, len(main_data) // 2))
        right_part = deque(islice(main_data, len(main_data) // 2, len(main_data)))
        main_data = left_part + need_to_add + right_part
    else:
        left_part = deque(islice(main_data, len(main_data) // 2 + 1))
        right_part = deque(islice(main_data, len(main_data) // 2 + 1, len(main_data)))
        main_data = left_part + need_to_add + right_part
    return main_data


def check_if_valid_color(sub_str_1: str, sub_str_2: str, main_data: deque, the_result: list):
    sum_1 = sub_str_1 + sub_str_2
    sum_2 = sub_str_2 + sub_str_1
    if sum_1 in main_colors or sum_1 in secondary_colors:
        the_result.append(sum_1)
    elif sum_2 in main_colors or sum_2 in secondary_colors:
        the_result.append(sum_2)
    else:
        sub_str_1 = sub_str_1[:-1]
        sub_str_2 = sub_str_2[:-1]
        main_data = add_elements_at_the_middle(main_data, sub_str_1, sub_str_2)
    main_data.pop()
    main_data.popleft()
    return main_data, the_result


data = deque(input().split())
main_colors = ['red', 'yellow', 'blue']
secondary_colors = ['orange', 'purple', 'green']
result = []

while data:
    if len(data) > 1:
        str_1 = data[0]
        str_2 = data[-1]
        data, result = check_if_valid_color(str_1, str_2, data, result)
    else:
        if data[0] in main_colors or data[0] in secondary_colors:
            result.append(data[0])
        data.pop()

for color in result:
    if color in secondary_colors:
        if color == 'orange':
            if 'red' in result and 'yellow' in result:
                pass
            else:
                result.remove(color)

        elif color == 'purple':
            if 'red' in result and 'blue' in result:
                pass
            else:
                result.remove(color)

        elif color == 'green':
            if 'yellow' in result and 'blue' in result:
                pass
            else:
                result.remove(color)

print(result)
