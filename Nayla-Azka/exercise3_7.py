# Exercise 3-7: Shrinking Guest List
# Mengurangi daftar tamu undangan
guests = ["Keifa", "Kanea", "Danes", "Aiko", "Nada", "Nikheisya"]

print("Maaf, meja makan yang baru tidak dapat tiba tepat waktu.")
print("Saya hanya bisa mengundang dua tamu untuk makan malam.")

# Menghapus tamu dari daftar hingga hanya tersisa dua tamu
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Maaf {removed_guest}, saya tidak bisa mengundang kamu untuk makan malam.")

# Mengirim pesan kepada dua tamu yang tersisa
for guest in guests:
    print(f"Halo {guest}, kamu tetap diundang untuk makan malam.")

# Menghapus dua tamu terakhir
del guests[0]
del guests[0]

print("Daftar tamu terakhir:", guests)
