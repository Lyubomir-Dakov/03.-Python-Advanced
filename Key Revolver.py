from collections import deque


def bullet_in_lock(all_bullets: deque, all_locks: deque):
    size_of_bullet = all_bullets.pop()
    size_of_lock = all_locks[0]
    if size_of_lock >= size_of_bullet:
        print('Bang!')
        all_locks.popleft()
    else:
        print("Ping!")
    return all_bullets, all_locks


def reloading(the_shot_bullets: int, barrel_limit: int, all_bullets: int):
    if the_shot_bullets % barrel_limit == 0 and all_bullets > 0:
        print("Reloading!")


price = int(input())
barrel = int(input())
bullets = deque(int(x) for x in input().split(' '))
locks = deque(int(x) for x in input().split(' '))
intelligence = int(input())

shot_bullets = 0
safe_is_opened = False

while bullets:
    bullets, locks = bullet_in_lock(bullets, locks)
    shot_bullets += 1
    reloading(shot_bullets, barrel, len(bullets))

    if not locks:
        safe_is_opened = True
        break

money_earned = intelligence - shot_bullets * price
if safe_is_opened:
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
