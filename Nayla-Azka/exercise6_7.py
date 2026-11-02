# Exercise 6-7: People
# Membuat dictionary untuk orang pertama
person_1 = {
    'firstName': 'nayla',
    'lastName': 'azka',
    'age': 18,
    'city': 'surakarta'
}

# Membuat dictionary untuk orang kedua
person_2 = {
    'firstName': 'haikal',
    'lastName': 'zamzami',
    'age': 27,
    'city': 'sukoharjo'
}

# Membuat dictionary untuk orang ketiga
person_3 = {
    'firstName': 'dayu',
    'lastName': 'nugraheni',
    'age': 30,
    'city': 'malang'
}

people = [person_1, person_2, person_3]

# Menampilkan informasi setiap orang
for person in people:
    print(f"Nama depan: {person['firstName'].title()}")
    print(f"Nama belakang: {person['lastName'].title()}")
    print(f"Umur: {person['age']}")
    print(f"Kota: {person['city'].title()}")
    print()
        
        