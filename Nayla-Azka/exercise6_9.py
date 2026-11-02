# Exercise 6-9: Favorite Places
# Membuat dictionary tempat favorit
favoritePlaces = {
    'nayla': ['bali', 'lombok', 'banyuwangi'],
    'kayla': ['jakarta', 'jogja', 'semarang'],
    'aan': ['bandung', 'malang', 'surabaya']
}

for name, places in favoritePlaces.items():
    print(f"\nTempat favorit {name.title()}:")

    # Menampilkan setiap tempat favorit
    for place in places:
        print(f"- {place.title()}")