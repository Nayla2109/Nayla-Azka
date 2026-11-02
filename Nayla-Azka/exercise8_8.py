# Exercise 8-8: User Albums
def makeAlbum(artistName, albumTitle):
    """Membangun dictionary yang berisi informasi tentang album musik"""
    album = {
        'artist': artistName.title(),
        'title': albumTitle.title()
    }
    return album

print("Masukkan informasi album (ketik 'q' kapan saja untuk keluar).")

while True:
    artist = input("\nNama Artis: ")
    if artist.lower() == 'q':
        break

    title = input("Judul Album: ")
    if title.lower() == 'q':
        break

userAlbum = makeAlbum(artist, title)
print(f"\nAlbum tercipta: {userAlbum}")