# Exercise 7-2: Restaurant Seating
# Meminta jumlah orang dalam kelompok makan
people = input("Berapa orang dalam kelompok makan Anda? ")
people = int(people)

if people > 8:
    print("\nMaaf, Anda harus menunggu meja.")
else:
    print("\nMeja Anda sudah siap.")