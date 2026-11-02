# Exercise 5-2: More Conditional Tests
# Pengujian kesamaan dan ketidaksamaan string
nama = "nayla"

print("Pengujian string:")
print(nama == "nayla")
print(nama != "azka")

# Pengujian menggunakan lower
kota = "JAKARTA"

print("\nPengujian lower():")
print(kota.lower() == "jakarta")
print(kota.lower() == "bandung")

# Pengujian angka
angka = 20

print("\nPengujian angka:")
print(angka == 20)
print(angka != 20)
print(angka > 10)
print(angka < 10)
print(angka >= 20)
print(angka <= 10)

# Pengujian menggunakan and dan or
umur = 18

print("\nPengujian and dan or:")
print(umur >= 17 and umur <= 25)
print(umur < 17 and umur > 10)
print(umur == 18 or umur == 20)
print(umur == 15 or umur == 16)

# Pengujian apakah item ada dalam list
buah = ["apel", "jeruk", "pisang"]

print("\nPengujian item dalam list:")
print("apel" in buah)
print("mangga" in buah)

# Pengujian apakah item tidak ada dalam list
print("\nPengujian item tidak ada dalam list:")
print("mangga" not in buah)
print("jeruk" not in buah)
