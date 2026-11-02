# Exercise 6-11: Cities
# Membuat dictionary berisi informasi tiga kota
cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': 10600000,
        'fact': 'ibu kota indonesia'
    }, 

    'tokyo': {
        'country': 'japan',
        'population': 14000000,
        'fact': 'memiliki menara tokyo'
    },

    'paris': {
        'country': 'france',
        'population': 2100000,
        'fact': 'terkenal dengan menara eiffel'
    }
}

for city, information in cities.items():
    print(f"\nNama kota: {city.title()}")
    print(f"Negara: {information['country'].title()}")
    print(f"Populasi: {information['population']:,}")
    print(f"Fakta: {information['fact'].capitalize()}")