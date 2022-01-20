from collections import deque

cups = deque(int(x) for x in input().split(' '))
bottles = deque(int(x) for x in input().split(' '))

wasted_water = 0
filled_all_cups = True


def fill_up_the_cup(all_cups: deque, all_bottles: deque, the_wasted_water: int):
    the_current_bottle = all_bottles.pop()
    if the_current_bottle >= all_cups[0]:
        the_wasted_water += the_current_bottle - all_cups.popleft()
    else:
        all_cups[0] -= the_current_bottle
    return all_cups, all_bottles, the_wasted_water


while cups:
    cups, bottles, wasted_water = fill_up_the_cup(cups, bottles, wasted_water)
    if not bottles:
        filled_all_cups = False
        break

if filled_all_cups:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")
else:
    print(f"Cups: {' '.join([str(x) for x in cups])}")

print(f"Wasted litters of water: {wasted_water}")

