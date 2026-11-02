# Exercise 7-3: Multiples of Ten
# Meminta pengguna memasukkan sebuah angka
number = input("Masukkan sebuah angka: ")
number = int(number)

if number % 10 == 0:
    print(f"\n{number} adalah kelipatan 10.")
else:
    print(f"\n{number} bukan kelipatan 10.")