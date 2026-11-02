# Exercise 5-10: Checking Usernames
currentUsers = ['nayla', 'kayla', 'daffa', 'adib', 'rafel']

newUsers = ['NAYLA', 'Kanea', 'Aiko', 'ADIB', 'Nada']

currentUsersLower = []

for user in currentUsers:
    currentUsersLower.append(user.lower())

for newUser in newUsers:
    if newUser.lower() in currentUsersLower:
        print(f"Maaf, {newUser} sudah digunakan.")
    else:
        print(f"{newUser} masih tersedia.")