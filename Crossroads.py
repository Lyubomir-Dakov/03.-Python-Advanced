from collections import deque

green_light = int(input())
free_light = int(input())

successfully_passed = 0
cars = deque()
passed_cars = []
current_car = deque()
crashed = False

while True:
    new_input = input()
    if new_input == 'END':
        break
    if new_input == 'green':
        green_seconds = green_light
        free_seconds = free_light
        while cars:
            if green_seconds == 0:
                break
            passed_cars.append(cars.popleft())
            current_car = deque([x for x in passed_cars[-1]])
            for _ in range(len(current_car)):
                current_car.popleft()
                green_seconds -= 1
                if green_seconds == 0:
                    break

            if not current_car:
                successfully_passed += 1

            if current_car and green_seconds == 0:
                if free_seconds == 0:
                    print("A crash happened!")
                    print(f"{passed_cars[-1]} was hit at {current_car[0]}.")
                    crashed = True
                    break
                for _ in range(len(current_car)):
                    current_car.popleft()
                    free_seconds -= 1
                    if free_seconds == 0:
                        break
                if current_car:
                    print("A crash happened!")
                    print(f"{passed_cars[-1]} was hit at {current_car[0]}.")
                    crashed = True
                    break
                else:
                    successfully_passed += 1

    else:
        cars.append(new_input)
    if crashed:
        break

if not crashed:
    print("Everyone is safe.")
    print(f"{successfully_passed} total cars passed the crossroads.")
