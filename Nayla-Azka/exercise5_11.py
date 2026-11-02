# Exercise 5-11: Ordinal Numbers
# Membuat daftar angka dari 1 sampai 9
numbers = list(range(1, 10))

# Melakukan perulangan untuk setiap angka
for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")