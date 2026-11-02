# Exercise 5-8: Hello Admin
usernames = ['admin', 'nayla', 'sarah', 'kia', 'naya']

for username in usernames:
    if username == 'admin':
        print("Halo admin, apakah Anda ingin melihat laporan status?")
    else:
        print(f"Halo {username}, terima kasih telah login kembali.")