# Exercise 7-4: Pizza Toppings
# Membuat perulangan untuk memasukkan topping pizza
prompt = "\nMasukkan topping pizza yang Anda inginkan"
prompt += "\nKetik 'quit' untuk selesai: "

while True:
    # Meminta pengguna memasukkan topping
    topping = input(prompt)

    # Menghentikan program jika pengguna mengetik quit
    if topping == 'quit':
        break

    # Menampilkan topping yang ditambahkan
    print(f"Saya akan menambahkan {topping} ke pizza Anda.")

print("\nPizza Anda sedang disiapkan!")