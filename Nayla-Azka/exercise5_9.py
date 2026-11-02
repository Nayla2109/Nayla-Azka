# Exercise 5-9: No Users
usernames = ['nayla', 'sarah', 'kia']

if usernames:
    print("Pengguna tersedia.")
else:
    print("Kita perlu mencari beberapa pengguna!")

# Menghapus semua nama pengguna
usernames.clear()

if not usernames:
    print("Kita perlu mencari beberapa pengguna!")