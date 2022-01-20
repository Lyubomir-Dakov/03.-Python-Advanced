from collections import deque

import sys
from io import StringIO

input_1 = """10 -5 20 15 -30 10
40 60 10 4 10 0
"""

input_2 = """30 5 15 60 0 30
-15 10 5 -15 25
"""

sys.stdin = StringIO(input_1)


def magic_level_match_toys(the_toys: dict, the_materials: deque, the_magic_values: deque, the_magic: int):
    the_toys[the_magic][1] += 1
    the_materials.pop()
    the_magic_values.popleft()
    return the_toys, the_materials, the_magic_values


def negative_magic_level(the_materials: deque, the_magic_values: deque):
    the_materials.append(the_materials.pop() + the_magic_values.popleft())
    return the_materials, the_magic_values


def positive_magic_level_doesnt_match_toys(the_materials: deque, the_magic_values: deque):
    the_magic_values.popleft()
    the_materials[-1] += 15
    return the_materials, the_magic_values


toys = {
    150: ['Doll', 0],
    250: ['Wooden train', 0],
    300: ['Teddy bear', 0],
    400: ['Bicycle', 0]
}

materials = deque(int(x) for x in input().split())
magic_values = deque(int(x) for x in input().split())

while True:
    if not materials or not magic_values:
        break
    material = materials[-1]
    magic = magic_values[0]
    if material == magic == 0:
        materials.pop()
        magic_values.popleft()
        continue
    elif material == 0:
        materials.pop()
        continue
    elif magic == 0:
        magic_values.popleft()
        continue
    magic_level = material * magic
    if magic_level in toys:
        magic_level_match_toys(toys, materials, magic_values, magic_level)
    elif magic_level < 0:
        negative_magic_level(materials, magic_values)
    elif magic_level not in toys:
        positive_magic_level_doesnt_match_toys(materials, magic_values)

crafted_toys = {v[0]: v[1] for k, v in toys.items() if v[1] > 0}
sorted_crafted_toys = {k: v for k, v in sorted(crafted_toys.items(), key=lambda kvp: kvp[0])}

if 'Doll' in sorted_crafted_toys and 'Wooden train' in sorted_crafted_toys:
    print("The presents are crafted! Merry Christmas!")
elif 'Teddy bear' in sorted_crafted_toys and 'Bicycle' in sorted_crafted_toys:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    materials = ', '.join(str(x) for x in list(materials)[::-1])
    print(f"Materials left: {materials}")
if magic_values:
    magic_values = ', '.join(str(x) for x in list(materials)[::-1])
    print(f"Magic left: {magic_values}")

for toy, amount in sorted_crafted_toys.items():
    print(f"{toy}: {amount}")
