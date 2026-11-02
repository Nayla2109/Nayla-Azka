# Exercise 6-8: Pets
# Membuat dictionary hewan pertama
pet_1 = {
    'animal': 'kucing',
    'owner': 'nayla'
}

# Membuat dictionary hewan kedua
pet_2 = {
    'animal': 'anjing',
    'owner': 'kia'
}

# Membuat dictionary hewan ketiga
pet_3 = {
    'animal': 'kelinci',
    'owner': 'sarah'
}

# Menyimpan semua hewan dalam sebuah list
pets = [pet_1, pet_2, pet_3]

# Menampilkan informasi setiap hewan
for pet in pets:
    print(f"Hewan: {pet['animal'].title()}")
    print(f"Pemilik: {pet['owner'].title()}")
    print()