# Exercise 7-10: Dream Vacation
responses = {}
pollingActive = True

while pollingActive:
    name = input("\nSiapa nama Anda? ")
    response = input("Jika Anda bisa mengunjungi satu tempat di dunia, di mana Anda akan pergi? ")

    responses[name] = response

    repeat = input("Apakah ada orang lain yang ingin ikut polling? (ya/tidak): ")
    if repeat.lower() == 'tidak':
        pollingActive = False

print("\n--- Hasil Polling Liburan Impian ---")
for name, location in responses.items():
    print(f"{name} ingin mengunjungi {location}.")