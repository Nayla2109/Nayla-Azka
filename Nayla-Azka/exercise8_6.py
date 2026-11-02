# Exercise 8-6: City Names
def cityCountry(city, country):
    """Mengembalikan string berupa 'Kota, Negara'."""
    return f"{city.title()}, {country.title()}"

city1 = cityCountry('santiago', 'chile')
city2 = cityCountry('tokyo', 'jepang')
city3 = cityCountry('paris', 'perancis')

print(city1)
print(city2)
print(city3)