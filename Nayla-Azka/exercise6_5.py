# Exercise 6-5: Rivers
# Membuat dictionary berisi nama sungai dan negaranya
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# Menampilkan informasi setiap sungai
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nNama-nama sungai:")

# Menampilkan nama setiap sungai
for river in rivers.keys():
    print(river.title())

print("\nNama-nama negara:")

# Menampilkan nama setiap negara
for country in rivers.values():
    print(country.title())