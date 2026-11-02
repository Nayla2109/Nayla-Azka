# Exercise 8-4: Large Shirts
def makeShirt(size='large', message='I love Pythone'):
    """Membuat kaos dengan ukuran dan pesan default."""
    print(f"Membuat kaos ukuran {size.title()} dengan teks: '{message}'.")
          
makeShirt()

makeShirt(size='medium')
makeShirt(size='small', message='Belajar Python itu seru!')