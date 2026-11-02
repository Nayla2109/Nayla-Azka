# Exercise 8-10: Sending Messages
def sendMessages(messages, sentMessages):
    """Mencetak setiap pesan dan memindahkannya ke daftar sentMessages"""
    while messages:
        currentMessage = messages.pop(0)
        print(f"Mengirim pesan: {currentMessage}")
        sentMessages.append(currentMessage)

messages = ["Halo dunia!", "Belajar Python itu menyenangkan.", "Tetap semangat!"]
sentMessages = []

# Memanggil fungsi
sendMessages(messages, sentMessages)

print("\nDaftar pesan awal (messages):", messages)
print("Daftar pesan terkirim (sentMessages):", sentMessages)