# Exercise 6-6: Polling
# Dictionary berisi nama dan bahasa pemrograman favorit
favoriteLanguages = {
    'nayla': 'python',
    'sarah': 'c',
    'rakha': 'rust',
    'kia': 'python'
}

# Daftar orang yang harus mengikuti polling
people = ['nayla', 'rama', 'sarah', 'rakha', 'kia', 'indra']

for person in people:
    if person in favoriteLanguages:
        print(f"Thank you, {person.title()}, for taking the poll.")
    else:
        print(f"{person.title()}, please take our favorite languages poll.")
