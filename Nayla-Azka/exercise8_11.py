# Exercise 8-11: Archived Messages
def sendMessages(messages, setMessages):
    """Mencetak setiap pesan dan memindahkannya ke daftar sentMessages"""
    while messages:
        currentMessage = messages.pop(0)
        print(f"Mengirim pesan: {currentMessage}")
        sentMessages.append(currentMessage)

messages = ["Pesan satu", "Pesan dua", "Pesan tiga"]
sentMessages = []

sendMessages(messages[:], sentMessages)

print("\nDaftar pesan asli setelah fungsi dipanggil (tetap utuh):", messages)
print("Daftar pesan terkirim (sentMessages):", sentMessages)
        