from collections import deque

# import sys
# from io import StringIO
#
# input_1 = """0
# 0
# """
# input_2 = """-10, -2, -30, 10
# -5
# """
# input_3 = """2, 3, 3, 7, 2
# 2, 7, 3, 3, 2, 14, 6
# """
#
# sys.stdin = StringIO(input_2)

chocolate = deque(int(x) for x in input().split(', '))
milk = deque(int(x) for x in input().split(', '))

shakes = 0

while True:
    if not chocolate or not milk or shakes == 5:
        break

    if chocolate[-1] <= 0 and milk[0] <= 0:
        chocolate.pop()
        milk.popleft()
        continue

    if chocolate[-1] <= 0:
        chocolate.pop()
        continue

    if milk[0] <= 0:
        milk.popleft()
        continue

    if chocolate[-1] == milk[0]:
        shakes += 1
        chocolate.pop()
        milk.popleft()
    else:
        chocolate[-1] -= 5
        milk.append(milk.popleft())

if shakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    chocolate = [str(x) for x in chocolate]
    print(f"Chocolate: {', '.join(chocolate)}")
else:
    print("Chocolate: empty")

if milk:
    milk = [str(x) for x in milk]
    print(f"Milk: {', '.join(milk)}")
else:
    print("Milk: empty")

