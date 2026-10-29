def hitung_parkir():
    print("=== Program Menghitung Tarif Parkir ===")
    print("1. Mobil")
    print("2. Motor")   

    kendaraan = input("Pilih jenis kendaraan (1/2): ")

    jam_masuk = int(input("Masukkan jam masuk (0-23): "))
    jam_keluar = int(input("Masukkan jam keluar (0-23): "))

    masuk = jam_masuk
    keluar = jam_keluar

    # Menghitung durasi parkir
    durasi = keluar - masuk

    # Jika keluar pada hari berikutnya, tambahkan 24 jam
    if durasi < 0:
        durasi += 24
    # Pembulatan durasi ke atas
    durasi = int(durasi) + (1 if durasi % 1 > 0 else 0)

    # Menghitung tarif parkir berdasarkan jenis kendaraan
    if kendaraan == "1":
        tarif_per_jam = 3000
        tarif_total = durasi * tarif_per_jam
        print(f"Tarif parkir untuk mobil selama {durasi} jam adalah: Rp {tarif_total}")
    elif kendaraan == "2":
        tarif_per_jam = 1500
        tarif_total = durasi * tarif_per_jam
        print(f"Tarif parkir untuk motor selama {durasi} jam adalah: Rp {tarif_total}")
    else:
        print("Jenis kendaraan tidak valid. Silakan pilih 1 atau 2.")

    # Menghitung biaya parkir
    biaya_parkir = tarif_total

    # Menampilkan hasil perhitungan
    print("=== Hasil Perhitungan Tarif Parkir ===")
    print("Kendaraan:", "Mobil" if kendaraan == "1" else "Motor")
    print("Jam Masuk:", jam_masuk)
    print("Jam Keluar:", jam_keluar)
    print("Durasi Parkir:", durasi, "jam")
    print("Biaya Parkir: Rp", biaya_parkir)

# Memanggil fungsi hitung_parkir() untuk menjalankan program
hitung_parkir()