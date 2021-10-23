with open('users.json') as users_file:
    users = json.load(users_file)

print(len(users['users']))
