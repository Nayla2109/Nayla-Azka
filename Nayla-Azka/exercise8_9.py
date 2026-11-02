# Exercise 8-9: Messages
def showMessages(messages):
    """Mencetak setiap pesan teks dari dalam daftar"""
    for message in messages:
        print(message)

# Daftar pesan singkat
textMessages = [
    "Halo, apa kabar?",
    "Jangan lupa kerjakan tugas Python ya,",
    "Sampai jumpa besok!"
]

# Memanggil fungsi
showMessages(textMessages)