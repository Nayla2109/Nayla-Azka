# Exercise 6-10: Favorite Numbers
# Membuat dictionary angka favorit
favoriteNumbers = {
    'nayla': [2, 1, 9],
    'kayla': [1, 15],
    'daffa': [9, 13, 20],
    'adib': [1, 8, 22],
    'rafel': [4, 10]
}

# Menampilkan nama dan angka favorit setiap orang
for name, numbers in favoriteNumbers.items():
    print(f"\nAngka favorit {name.title()}:")
    for number in numbers:
        print(number)