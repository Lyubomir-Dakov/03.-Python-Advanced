num_commands = int(input())
cars = set()


def car_in(all_cars: set, new_car: str):
    all_cars.add(new_car)
    return all_cars


def car_out(all_cars: set, car_goes_out: str):
    all_cars.discard(car_goes_out)
    return all_cars


for _ in range(num_commands):
    direction, car_number = input().split(', ')
    if direction == "IN":
        cars = car_in(cars, car_number)
    elif direction == "OUT":
        cars = car_out(cars, car_number)

if cars:
    for car in cars:
        print(car)
else:
    print("Parking Lot is Empty")
