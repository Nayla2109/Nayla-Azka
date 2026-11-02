# Menentukan jumlah perulangan
active = 3

while active > 0:
    topping = input("\nMasukkan topping pizza: ")

    print(f"Topping {topping} berhasil ditambahkan.")

    # Mengurangi jumlah perulangan
    active -= 1

print("\nBatas topping sudah tercapai.")