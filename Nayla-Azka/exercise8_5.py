# Exercise 8_5: Cities
def describeCity(city, country='island'):
    """Menampilkan deskripsi kota dan negaranya."""
    print(f"{city.title()} berada di {country.title()}.")

describeCity('reykjavik', 'iceland')
describeCity('tokyo', 'jepang')
describeCity('akureyri')