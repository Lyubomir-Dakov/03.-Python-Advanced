from collections import deque


def all_bombs_collected(the_bombs_collected: dict):
    for x in the_bombs_collected.values():
        if x < 3:
            return False
    return True


effect = deque(int(x) for x in input().split(', '))
casing = [int(x) for x in input().split(', ')]

bombs = {
    40: 'Datura Bombs',
    60: 'Cherry Bombs',
    120: 'Smoke Decoy Bombs'
}

collected_bombs = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}

while True:
    if not casing or not effect:
        break

    current_effect = effect[0]
    current_casing = casing[-1]

    mix = current_effect + current_casing

    if mix in bombs:
        collected_bomb = bombs[mix]
        collected_bombs[collected_bomb] += 1
        effect.popleft()
        casing.pop()
    else:
        casing[-1] -= 5

    if all_bombs_collected(collected_bombs):
        break

if all_bombs_collected(collected_bombs):
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if effect:
    result = ', '.join(str(x) for x in effect)
    print(f"Bomb Effects: {result}")

else:
    print("Bomb Effects: empty")

if casing:
    result = ', '.join(str(x) for x in casing)
    print(f"Bomb Casings: {result}")
else:
    print("Bomb Casings: empty")

for bomb, count in sorted(collected_bombs.items()):
    print(f'{bomb}: {count}')
