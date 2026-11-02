# Exercise 8-7: Album
def makeAlbum(artistName, albumTitle, numberOfSongs=None):
    """Membangun dictionary yang berisi informasi tentang album musik."""
    album = {
        'artist': artistName.title(),
        'title': albumTitle.title()
    }

    if numberOfSongs:
        album['songs'] = numberOfSongs

    return album

album1 = makeAlbum('sheila on 7', 'film favorit')
album2 = makeAlbum('dewa 19', 'risalah hati')
album3 = makeAlbum('hivi', 'pelangi')

print(album1)
print(album2)
print(album3)