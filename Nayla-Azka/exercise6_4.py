# Exercise 6-4: Glossary 2
# Membuat dictionary berisi istilah Python dan artinya
glossary = {
    'variable': 'Tempat menyimpan data dalam program.',
    'list': 'Kumpulan beberapa data dalam satu variabel.',
    'dictionary': 'Struktur data yang menyimpan pasangan key and value.',
    'loop': 'Perulangan untuk menjalankan kode berkali-kali.',
    'ifStatement': 'Digunakan untuk memeriksa suatu kondisi.',

    # Menambahkan lima istilah baru
    'string': 'Tipe data yang berisi teks.',
    'integer': 'Tipe data berupa bilangan bulat.',
    'float': 'Tipe data berupa bilangan desimal.',
    'boolean': 'Tipe data yang bernilai True atau False.',
    'function': 'Blok kode yang dapat digunakan kembali.'
}

# Menampilkan judul program
print("PYTHON PROGRAM")
print("========================")

# Perulangan untuk membaca dictionary
for word, meaning in glossary.items():
    print(f"\n{word.upper()}:")
    print(f" {meaning}")