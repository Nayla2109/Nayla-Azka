# Exercise 3-8: Seeing the World
# Daftar tempat wisata yang ingin dikunjungi

places = ["Maldives", "Jepang", "New York", "Thailand", "Swiss"]

# Menampilkan daftar asli
print("Daftar tempat wisata yang ingin saya kunjungi:")
print(places)

# Menampilkan daftar dalam urutan abjad
print("\nDaftar tempat wisata dalam urutan abjad:")
print(sorted(places))

# Menampilkan daftar asli lagi
print("\nDaftar tempat wisata yang ingin saya kunjungi:")
print(places)

# Menampilkan daftar dalam urutan abjad terbalik
print("\nDaftar tempat wisata dalam urutan abjad terbalik:")
print(sorted(places, reverse=True))

# Menampilkan daftar asli lagi
print("\nDaftar tempat wisata yang ingin saya kunjungi:")
print(places)

# Membalik urutan daftar
places.reverse()
print("\nDaftar tempat wisata setelah reverse():")
print(places)

# Mengembalikan ke urutan asli
places.reverse()
print("\nDaftar tempat wisata kembali ke urutan asli:")
print(places)

# Mengurutkan daftar sesuai abjad
places.sort()
print("\nDaftar tempat wisata setelah sort():")
print(places)

# Mengurutkan daftar sesuai abjad terbalik
places.sort(reverse=True)
print("\nDaftar tempat wisata setelah sort(reverse=True):")
print(places)