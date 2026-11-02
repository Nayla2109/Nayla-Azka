# Exercise 4-13: Buffet
# Membuat daftar menu makanan
makanan = ("Nasi Goreng", "Mie Goreng", "Sate Ayam", "Rendang", "Gado-Gado")

# Menampilkan menu awal restoran
print("Menu awal restoran:")
for menu in makanan:
    print(menu)

# Mencoba mengubah menu makanan dalam tuple
print("\nMencoba mengubah menu makanan...")

try:
    makanan[0] = "Nasi Uduk"  
except TypeError:
    print("Error: Tuple tidak dapat diubah!")

# Membuat tuple baru dengan menu yang diperbarui
makanan = ("Nasi Uduk", "Mie Goreng", "Sate Ayam", "Gudeg", "Gado-Gado")

# Menampilkan menu yang diperbarui
print("\nMenu baru:")
for menu in makanan:
    print(menu)
