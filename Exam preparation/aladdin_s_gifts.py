from collections import deque

# import sys
# from io import StringIO
#
# input_1 = """105 20 30 25
# 120 60 11 400 10 1
# """
#
# input_2 = """30 5 21 6 0 91
# 15 9 5 15 8
# """
#
# input_3 = """200
# 5 15 32 20 10 5
# """
#
# sys.stdin = StringIO(input_3)

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

crafted_presents = {}

while True:
    if not materials or not magic:
        break

    current_material = materials.pop()
    current_magic = magic.popleft()
    current_mix = current_material + current_magic

    if current_mix < 100:
        if current_mix % 2 == 0:
            current_material *= 2
            current_magic *= 3
            current_mix = current_material + current_magic
        else:
            current_mix *= 2

    if current_mix > 499:
        current_mix /= 2

    if 100 <= current_mix <= 199:
        if 'Gemstone' not in crafted_presents:
            crafted_presents['Gemstone'] = 0
        crafted_presents['Gemstone'] += 1

    elif 200 <= current_mix <= 299:
        if 'Porcelain Sculpture' not in crafted_presents:
            crafted_presents['Porcelain Sculpture'] = 0
        crafted_presents['Porcelain Sculpture'] += 1

    elif 300 <= current_mix <= 399:
        if 'Gold' not in crafted_presents:
            crafted_presents['Gold'] = 0
        crafted_presents['Gold'] += 1

    elif 400 <= current_mix <= 499:
        if 'Diamond Jewellery' not in crafted_presents:
            crafted_presents['Diamond Jewellery'] = 0
        crafted_presents['Diamond Jewellery'] += 1

if ('Gemstone' in crafted_presents and 'Porcelain Sculpture' in crafted_presents) or ('Gold' in crafted_presents and 'Diamond Jewellery' in crafted_presents):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    materials = ', '.join(str(x) for x in materials)
    print(f"Materials left: {materials}")

if magic:
    magic = ', '.join(str(x) for x in magic)
    print(f"Magic left: {magic}")

for present, amount in sorted(crafted_presents.items()):
    print(f"{present}: {amount}")
