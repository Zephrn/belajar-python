from data import Tes


def tambah_buku():
    kt = "Fiksi", "Non-Fiksi", "Sains", "Komedi"
    ts_instance = Tes()
    judul = input("Masukkan judul buku: ")
    total = int(input("Masukkan jumlah total stok buku: "))
    kategori = input("Masukkan kategori buku: ")
    if kategori not in kt:
        print("kategori tidak tersedia di perpus ini")
    else:
        ts_instance.tambah_buku(judul, total, kategori)
        ts_instance.save_to_file()

# Contoh pemanggilan fungsi tambah_buku
tambah_buku()