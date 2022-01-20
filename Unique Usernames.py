num_usernames = int(input())
usernames = set()

for _ in range(num_usernames):
    username = input()
    usernames.add(username)

[print(name) for name in usernames]
