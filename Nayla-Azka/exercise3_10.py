# Exercise 3-10: Every Function
# Mempelajari penggunaan fungsi dan metode list Python

buah = ["apel", "pisang", "jeruk", "mangga"]

print("Daftar buah:")
print(buah)

# Mengakses elemen list
print(f"Buah pertama: {buah[0]}.")

# Mengubah elemen list
buah[1] = "anggur"
print("Daftar buah setelah diubah:")
print(buah)

# Menambahkan buah di akhir list
buah.append("kiwi")
print("Daftar buah setelah ditambahkan:")
print(buah)

# Menambahkan buah di posisi tertentu
buah.insert(2, "nanas")
print("Daftar buah setelah ditambahkan:")
print(buah)

# Menghapus buah dari list dengan del
del buah[3]
print("Daftar buah setelah dihapus:")
print(buah)

# Menghapus buah dari list dengan pop
buah.pop(1)
print("Daftar buah setelah dihapus:")
print(buah)

# Menghapus elemen berdasarkan nilai
buah.remove("kiwi")
print("Daftar buah setelah dihapus:")
print(buah)

# Mengurutkan sesuai abjad
buah.sort()
print("Daftar buah setelah diurutkan:")
print(buah)

# Mengurutkan sesuai abjad secara terbalik
buah.sort(reverse=True)
print("Daftar buah setelah diurutkan secara terbalik:")
print(buah)

# Menggunakan sorted() untuk menampilkan daftar buah dalam urutan abjad tanpa mengubah list asli
print("\nMenggunakan sorted():")
print(sorted(buah))

# Membalik urutan list
buah.reverse()
print("Daftar buah setelah dibalik:")
print(buah)

# Menghitung jumlah elemen dalam list
print(f"Jumlah buah: {len(buah)}.")