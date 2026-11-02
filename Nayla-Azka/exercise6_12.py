# Exercise 6-12: Extensions
# Membuat dictionary informasi kota
cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': 10600000,
        'fact': 'ibu kota indonesia',
        'language': 'indonesian',
        'currency': 'rupiah'
    },

    'tokyo': {
        'country': 'japan',
        'population': 14000000,
        'fact': 'memiliki menara tokyo',
        'language': 'japanese',
        'currency': 'yen'
    },

    'paris': {
        'country': 'france',
        'population': 2100000,
        'fact': 'terkenal dengan menara eiffel',
        'language': 'french',
        'currency': 'euro'
    }
}

# Menampilkan informasi lengkap setiap kota
for city, information in cities.items():
    print("\n========================")
    print(f"KOTA: {city.upper()}")
    print("========================")

    print(f"Negara: {information['country'].title()}")
    print(f"Populasi: {information['population']:,}")
    print(f"Fakta: {information['fact'].capitalize()}")
    print(f"Bahasa: {information['language'].title()}")
    print(f"Mata uang: {information['currency'].title()}")