# Exercise 7-6: Three Exits
# Menentukan kondisi awal perulangan
active = True

# Perulangan berjalan selama active bernilai True
while active:
    topping = input("\nMasukkan topping pizza: ")

    # Jika pengguna mengetik quit, kondisi menjadi False
    if topping == 'quit':
        active = False
    else:
        print(f"Topping {topping} berhasil ditambahkan.")

print("\nProgram selesai.")