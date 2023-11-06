# Percobaan 8.1
# Menggunakan tipe data set
# Tipe data set menggunakan kurung kurawal {}

print('>>>>>> Membuat set dengan kurung kurawal')
nama_dosen = {'Grace Kelly HS', 'Halasan Sihombing', 'Tommi Suryanto'}
print(nama_dosen)

# Mengkonversi list ke dalam set
print('>>>>> Membuat set menggunakan konversi list ke dalam set')
Nama_Dosen = set(['Muhammad Hasbi', 'Neny Firdyanti', 'Suharsono'])
print(Nama_Dosen)

# Set dengan tipe data yang berbeda-beda
print('>>>>> Set dengan tipe data yang berbeda-beda')
set_campuran = {('Pancasila', 2, 'SKS', 'Grace Kelly HS', 'PTI', 3, 'sks', True)}
print(set_campuran)
nilai_set = {'a', 'k', 'u'}

# Percobaan 8.2
nilai_set = {'a', 'k', 'u'}

# Untuk mengakses nilai di dalam set, Anda bisa menggunakan perulangan
for nilai in nilai_set:
    print(nilai)

#percobaan 8.3
#membuktikan sifat wordered pada tipe data set
nama_mahasiswa = {'Desi V','Andika JN','Awang PA','Fadli N'}
print(nama_mahasiswa)

# Percobaan 8.4
# Anggota set harus dari tipe data yang immutable

# Set ini mencampur tipe data yang berbeda, termasuk angka, string, dan boolean. Set harus memiliki anggota dengan tipe data yang immutable.
# Juga ada beberapa kesalahan dalam penulisan. Anda perlu memisahkan anggota-anggota set dengan koma, dan string harus dalam tanda kutip.

nama_mahasiswa = {'Desi V', 64, 'Andika JN', 68, 'Awang PA', 63, 'Fadli N', True}
print(nama_mahasiswa)

# Kita juga menjalankan tuple sebagai anggota set
# Karena tuple bersifat immutable
# Dalam set, tuple boleh digunakan.

papan_angka = {
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9),
    (0,)  # Anda perlu menambahkan tanda koma jika hanya ada satu angka dalam tuple
}
print(papan_angka)

# Percobaan 8.5
# Membuktikan bahwa list tidak dapat dimasukkan ke dalam set
# Karena list bersifat mutable

# Anda akan mendapatkan kesalahan jika mencoba memasukkan list ke dalam set
# Mengganti list dengan tuple

nilai_mahasiswa = {'Alpro', 'PPT', 'PTI', ('A', 'B', 'C', 'D', 'E')}
print(nilai_mahasiswa)

# Percobaan 8.6
# List mencetak semua nilai yang ada didalam List
motto_polnep = ['Tepat', 'Waktu', 'Tepat', 'Aturan', 'Tepat', 'Ukuran']
print("Cetak List Motto Polnep:", motto_polnep)

# Membuktikan set akan mencetak nilai yang sama (duplikat) satu kali saja
motto_polnep = {'Tepat', 'Waktu', 'Tepat', 'Aturan', 'Tepat', 'Ukuran'}
print("Cetak Set Motto Polnep:", motto_polnep)

# Mengubah list menjadi set menggunakan fungsi set
motto_polnep = set(['Tepat', 'Waktu', 'Tepat', 'Aturan', 'Tepat', 'Ukuran'])
print("Cetak List diubah menjadi set:", motto_polnep)

# Percobaan 8.7
# Menambah anggota baru pada set menggunakan fungsi add() dan update()

print(">>>>> Nilai awal set mata kuliah")
mata_kuliah = {'Pancasila', 'Matematika 1', 'PTI', 'Pemrograman Terstruktur'}
print(mata_kuliah)

print(">>>>> Menambah set dengan fungsi add")
mata_kuliah.add('Paket Program Terapan')
print(mata_kuliah)

# Tidak perlu memberikan dua nilai dalam fungsi add, hanya satu nilai pada setiap pemanggilan
# Juga memperbaiki tanda kutip yang salah

mata_kuliah.add('Algoritma Pemrograman')
print(mata_kuliah)

# Menggunakan fungsi update() untuk menambah beberapa anggota sekaligus
print(">>>>> Menambah set dengan fungsi update")
mata_kuliah.update({'Algoritma Pemrograman', 'Praktikum Pemrograman Terstruktur'})
mata_kuliah.update({'Praktikum Paket Program Terapan'})
print(mata_kuliah)

# Percobaan 8.8
# Cara membuat set dan melakukan operasi pada set

kumpulan = {'manggis', 'mangga', 150, ('x', 'y'), False, True}
print(kumpulan)

# Menggunakan fungsi remove untuk menghapus nilai dari set jika nilai ada dalam set
kumpulan.remove(150)
print(kumpulan)

# Menggunakan fungsi remove untuk menghapus nilai dari set yang tidak ada dalam set akan menghasilkan KeyError
# Anda bisa menghindari kesalahan ini dengan menggunakan discard
kumpulan.discard(200)
print(kumpulan)

# Menggunakan fungsi discard, tidak akan error, ada maupun tidak ada nilai dalam set
kumpulan.discard(('x', 'y'))
print(kumpulan)

# Menggunakan fungsi pop untuk menghapus nilai dari set, namun perlu diingat bahwa set adalah koleksi yang tidak terurut
# sehingga kita tidak tahu nilai apa yang akan dihapus
kumpulan.pop()
print(kumpulan)

# Menggunakan fungsi clear untuk menghapus semua nilai dalam set
kumpulan.clear()
print(kumpulan)

# Percobaan 8.9
# Menggunakan fungsi union

mahasiswa = set(['Andika', 'Jaya', 'Nanda', 'Andyka', 'Fajar', 'Pratama', 'Diana', 'Dwi', 'Apita'])
mhs = set(['Nanda', 'Ikhwanul', 'Nadlirin', 'Fajar', 'Ulfah', 'Dwi', 'Nazarina'])

print("Kelompok 1:\n", mahasiswa)
print("Kelompok 2:\n", mhs)
print("\n")

# Menggunakan fungsi union cara 1 dengan simbol pipe |
print(">>>> Cara 1 fungsi union dengan simbol pipe | <<<<")
print(mahasiswa | mhs)
print('\n')

# Menggunakan fungsi union cara 2 dengan fungsi set.union
print(">>>> Cara 2 fungsi union dengan set.union <<<<")
print(mahasiswa.union(mhs))

# Percobaan 8.10
# Menggunakan fungsi set.intersection

mahasiswa = set(['Andika', 'Jaya', 'Nanda', 'Andyka', 'Fajar', 'Pratama', 'Diana', 'Dwi', 'Apita'])
mhs = set(['Nanda', 'Ikhwanul', 'Nadlirin', 'Fajar', 'Ulfah', 'Dwi', 'Nazarina'])

print("Kelompok 1:\n", mahasiswa)
print("Kelompok 2:\n", mhs)
print("\n")

# Cara 1 menggunakan fungsi dengan simbol &
print(">>>>>> Cara 1 menggunakan fungsi set.intersection dengan simbol &")
print(mahasiswa & mhs)
print("\n")

# Cara 2 menggunakan fungsi set.intersection
print(">>>>>> Cara 2 menggunakan fungsi set.intersection")
print(mahasiswa.intersection(mhs))

# Percobaan 8.11
# Menggunakan fungsi set.difference (selisih)

mahasiswa = set(['Andika', 'Jaya', 'Nanda', 'Andyka', 'Fajar', 'Pratama', 'Diana', 'Dwi', 'Apita'])
mhs = set(['Nanda', 'Ikhwanul', 'Nadlirin', 'Fajar', 'Ulfah', 'Dwi', 'Nazarina'])

print("Kelompok 1:\n", mahasiswa)
print("Kelompok 2:\n", mhs)
print("\n")

# Cara 1 menggunakan fungsi difference dengan simbol -
print("Cara 1 fungsi difference dengan simbol -")
print(mahasiswa - mhs)
print("\n")

# Cara 2 menggunakan fungsi difference dengan memanggil fungsi set.difference
print("Cara 2 fungsi difference dengan memanggil fungsi set.difference")
print(mahasiswa.difference(mhs))

# Percobaan 8.12
# Menggunakan fungsi symmetric_difference (anggota yang hanya ada dalam satu grup saja)

mahasiswa = set(['Andika', 'Jaya', 'Nanda', 'Andyka', 'Fajar', 'Pratama', 'Diana', 'Dwi', 'Apita'])
mhs = set(['Nanda', 'Ikhwanul', 'Nadlirin', 'Fajar', 'Ulfah', 'Dwi', 'Nazarina'])

print("Nama Mahasiswa yang hanya ikut dalam satu grup saja")
print(mahasiswa.symmetric_difference(mhs))

# Percobaan 8.14
# Menggunakan perulangan untuk menampilkan set

mhs = {'Nanda', 'Ikhwanul', 'Nadlirin', 'Fajar', 'Ulfah', 'Dwi', 'Nazarina'}
for mahasiswa in mhs:
    print(mahasiswa)