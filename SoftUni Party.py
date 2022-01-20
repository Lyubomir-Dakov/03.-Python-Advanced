guests_num = int(input())
regular_guests = set()
vip_guests = set()


def sort_data(my_set: set):
    return sorted(my_set)


for guest in range(guests_num):
    new_guest = input()
    if new_guest[0].isdigit():
        vip_guests.add(new_guest)
    else:
        regular_guests.add(new_guest)

while True:
    come_to_party = input()
    if come_to_party == 'END':
        break

    if come_to_party[0].isdigit():
        vip_guests.discard(come_to_party)
    else:
        regular_guests.discard(come_to_party)

vip_guests = sort_data(vip_guests)
regular_guests = sort_data(regular_guests)

missing_guests = len(vip_guests) + len(regular_guests)
print(missing_guests)

for guest in vip_guests:
    print(guest)
for guest in regular_guests:
    print(guest)
