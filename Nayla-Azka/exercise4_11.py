# Exercise 4-11: My Pizzas, Your Pizzas
# Membuat daftar pizza yang berbeda

# Daftar pizza favorit saya
pizzas = ["Pizza Pepperoni", "Pizza Keju", "Pizza Meat Lover"]

# Menyalin daftar pizza
friend_pizzas = pizzas[:]

# Menambahkan pizza baru ke daftar saya
pizzas.append("Pizza BBQ")

# Menambahkan pizza baru ke daftar teman saya
friend_pizzas.append("Pizza Vegetarian")

# Menampilkan daftar pizza saya
print("Daftar pizza favorit saya:")
for pizza in pizzas:
    print(pizza) 

# Menampilkan daftar pizza teman saya
print("\nDaftar pizza favorit teman saya:")
for pizza in friend_pizzas:
    print(pizza)
