# Exercise 7-5: Movie Tickets
# Meminta pengguna memasukkan usia
prompt = "\nBerapa usia Anda? "
prompt += "\nKetik 'quit untuk selesai:"

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Tiket gratis.")
    elif age <= 12:
        print("Harga tiker adalah $10.")
    else:
        print("Harga tiket adalah $15.")

print("\nTerimakasih!")