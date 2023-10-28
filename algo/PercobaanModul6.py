#Percobaan 7.1
#contoh sederhana menbuat List menggunakan bahasa penrogranan python
list1 = ["Teknik Informatika", "Teknik Elektro" ,2009,2022]
list2 = [3,20,22,16,150]
list3 = ["C","B","Sangat Baik" ,"Unggul"]

print(list1)
print(list2)
print(list3)

#percoboon 7. 2
# scoro mengokses ni loi di dolan list pdo python 
list1 = ['Teknik Informatika', 'Teknik Elektro', 2009, 2022]
list2 = [3,20,22,16,150] 
list3 = ["C", "B", "Sangat Baik", "Unggul"]
print("Mengakses Nilai Listl[0] :", list1[0]) 
print("Mengakses Nilai List2[2] :" ,list2[2])
print("Mengakses Nilai List3[1:5]:" ,list3[1:5])

# percobaan 7.3 
# mengupdate nilai dalam list 
print("sebelum melakukan update")
list1 = ['Teknik Informatika', 'Tenik Elektro', 2001, 2002]
print("Nilai List pada index 0 adalah" ,list1[0])
print("nilai List poda index 2 odalah" ,list1[2]) 
print ('-'*70)
#sekarang kita update nilai pada index 0 dan index 2
print("Setelah melakukan update")
list1[2] = 2009 
list1[0] = 'Teknologi Informasi'
print("Nilai Baru pada index 0 sekarang adalah" ,list1[0]) 
print("Nilai Baru pada index 2 sekarang adalah" ,list1[2])
print('-'*70) 
#mengupdate List dengon data range
list1[0:2] = ['D4' 'Rekayasa Perangkat Lunak']
# lln1engecek senuo niloi podo List1 seteLah di update 
print("nilai Semua pada list1 setelah di update", list1)


#Percobaoon 7.4 
# menanbah nilai list dengan fungsi insert dan append 
list1 = ['Teknik Informatika', 'Teknik Elektro' ,2009,2022]
list2 = [3,20,22,16,150]
list3 = [ "c", "8", "Sangat Baik", "Unggul"] 
print("Nilai list sebelum di tambah")
print('Listl >>' ,list1)
print('List2 >> ',list2) 
print('List3 >>' ,list3) 
# menambah list dori a<tal Li st dengon fungsi insert 
print("Nilai list setelah ditambah di awal dengan fungsi insert")
list1.insert(0,'Teknologi Informasi')
print(list1) 
# menambah list dari mana saja dengan fungsi insert 
print("Nilai list setelah ditambah dari mana saja dengan fungsi insert")
list2.insert(3,300) 
print(list2) 
# menanbah list dari akhir list dengon fungsi append 
print("Nilai list setelah ditambah di akhir dengan fungsi append")
list3.append('A') 
print(list3)

# percobaan 7.5
# menghapus nilai pada list
list1 = ['Teknik Informatika', 'Teknik Elektro' ,2009,2022]
list2 = [3,20,22,16,150]
list3 = [ "C", "B", "BAIK", "Sangat Baik", "Unggul"] 
# menghapus nilai list diakhir menggunakan fungsi pop
print("Menghapus nilai list dengan fungsi pop")
list1.pop()
print(list1)
# menghapus nilai list menggunakan index dengan fungsi del 
print("Menghapus nilai list menggunakan index dengan fungsi del")
del list2[4]
print(list2)
# menghapus nilai list dengan fungsi remove 
print("Menghapus nilai list dengan fungsi remove")
list3.remove("C")
print(list3)

#Praktikun 7.7 
#Nenggunakon operasi dasar pada List python dengon expression concatenation
#menggobungkon List string dengon operator +
print("Menggabungkan list tipe data string dengan operator +")
a = "Resolusiku" 
b = "di Tahun" 
c = "2023" 
d = "Mendapatkan"
e = "Indeks Prestasi Kumulatif (IPK) " 
f = "4.00"
my_goals = a + b + c + d + e + f 
print(my_goals)
#menggobungkon List integer dengon operator t 
print('>> Menggabungkan list tipe data integer dengan operator +')
nil_aktifitas = 100 
nil_tugas  = 95
nil_UTS = 90 
nil_UAS = 90
nilai_Alpro = nil_aktifitas*0.1 + nil_tugas*0.2 + nil_UTS*0.3 + nil_UAS*0.4
print('Target Nilai Algoritma Pemrograman ku adalah',nilai_Alpro)
#menggobungkon List canpuron dengon dengon operator t 
print('>> Menggabungkan list tipe data campuran dengan operator +')
listl = ['alpa', False, 'Hadir', True, 8, 'jam', 'kuliah']
list2 = [ 'kuliah' ,1, 'minggu' ,5, 'hari', 50.00, 'menit'] 
aktivitas = listl + list2
print(aktivitas) 
#menggobungkon List dengon operator ~
print('>> Menggabungkan list dengan operator *') 
tugas_mhs = ['Kuliah', 'Tugas', 'PKL', 'TA', 'Wisuda']
cetak_tugas_mhs = tugas_mhs * 3 
print( 'Tugas Mahasiswa adalah' ,cetak_tugas_mhs)


#Praktikun 7.8
#Nenggunakon operosi dosor podo List python dengon Nenbership I Keonggotoon 
mata_kuliah = [ 'Matematika 1', 'Pancasila', 'Algoritma', 'Pemrograman', 'Paket Terapan', 'Praktik']
cek_mk = 'Algoritma' in mata_kuliah 
print("Apakah ada Mata Kuliah Algoritma :",cek_mk)
sem_ganjil = [1,2,3,4,5]
print('Saya sekarang semester 1 :' ,1 in sem_ganjil) 


#Praktikun 7. 9
#Menggunakan operosi dosor podo Li st python dengan i terotion 
nama_mhs = ['AZIZ NUR ASHIDIQ', 'NIZAR KHAWARIZMI',
'FATA HUMAN ASADILLAH', 'AWANG PRAJA ANUGERAH', 
'FAHMI YAZID', 'BELVA MIEKO SUPARWANTO'] 
# mencetak List dengan iterasi berurut kesamping
print('>> Cetak iterasi berurut kesamping')
for cetak in nama_mhs: 
    print (cetak,end = ' ' ) 
# mencetak list dengan iterasi berturut kebawah
print('\n', '-'*70)
print('>> Cetak iterasi berurut kebawah') 
for cetak in nama_mhs:
    print(cetak) 


#Praktikun 7.10 
#menggunakan indexing,, slicing dan matrik pada list python 
bhs_pemrograman = ['Pascal', 'Java', 'Python', 'HTML', 'PHP', 'SQL']
print('Index 2 :' ,bhs_pemrograman[2]) 
print('Index -2 :' ,bhs_pemrograman[-2])
print('Index kiri 1 kanan bebas :' ,bhs_pemrograman[1:]) 
print('Index kiri bebas kanan -2 :' ,bhs_pemrograman[ :-2])
print('Index kiri 1 kanan 3 :' ,bhs_pemrograman[1:3]) 
print('Index kiri 0 kanan -3 :' ,bhs_pemrograman[-5:-3])
print('Index kiri 0 kanan 3 :' ,bhs_pemrograman[0:3]) 
print('Index kiri -6 kanan -3' ,bhs_pemrograman[-6:-3])


#Praktikun 7.ll 
# menggunakan method don fungsi built-in podo List python
# menggunakan fungsi built-in pada list python 
bhs_pemrograman = ['Pascal', 'Java', 'Python', 'HTML', 'PHP', 'SQL ']
print('Jumlah Bahasa Pemrograman yang akan dipelajari ada :' ,len(bhs_pemrograman))
print('Nilai maksimum dari list Bahasa Pemrograman : ',max(bhs_pemrograman)) 
print('Nilai minimum dari list Bahasa Pemrograman : ',min(bhs_pemrograman))
print(list(bhs_pemrograman))
print(bhs_pemrograman.count('Java')) 

# pratikum 7.12
# Menggunakan methods built-in pada List python
bhs_pemrograman = ["Pascal", "Java", "Python", "HTML", "PHP", "SQL"]

# 7.12.1 Menggunakan method append
bhs_pemrograman.append("Laravel")
print(bhs_pemrograman)

# 7.12.2 Menggunakan method count
print(bhs_pemrograman.count("Python"))

# 7.12.3 Menggunakan method extend
bhs_pemrograman.extend(["C#", "JS", "C++"])
print(bhs_pemrograman)

# 7.12.4 Menggunakan method index
print(bhs_pemrograman.index("SQL"))

# 7.12.5 Menggunakan method insert
bhs_pemrograman.insert(1, "C++")
print(bhs_pemrograman)

# 7.12.6 Menggunakan method pop pada List
bhs_pemrograman.pop()
print(bhs_pemrograman)

# 7.12.7 Menggunakan method remove
bhs_pemrograman.remove("Python")
print(bhs_pemrograman)

# 7.12.8 Menggunakan method reverse
bhs_pemrograman.reverse()
print(bhs_pemrograman)

# 7.12.9 Menggunakan method sort
bhs_pemrograman.sort()
print(bhs_pemrograman)

# Percobaan 7.13
# Contoh program untuk menentukan bilangan genap dan ganjil dalam sebuah list

baris_angka = [-1, 3, 17, 14, 11, 6, 18, 93, 88, 208, 16, 17]

print("Baris Angka:", baris_angka)

bil_genap = [genap for genap in baris_angka if genap % 2 == 0]

print("Bilangan Genap ada", len(bil_genap), "angka, yaitu", bil_genap)

bil_ganjil = [ganjil for ganjil in baris_angka if ganjil % 2 != 0]

print("Bilangan Ganjil ada", len(bil_ganjil), "angka, yaitu", bil_ganjil)

# Percobaan 7.14
# Menggunakan fungsi join untuk menggabungkan elemen-elemen list

nama_prodi = ['Teknik', 'Informatika', 'Manajemen', 'Informatika', 'Teknik', 'Elektro', 'Sistem', 'Komputer']

program_studi = ' '.join(nama_prodi)
print("Program Studi D3:", program_studi)

kampus = ["Tepat", 'Hak', "Tepat", "Ukuran", "Tepat", "Aturan"]
motto = ' '.join(kampus)
print("Motto Polnep:", motto)

TTL = ['Pontianak', "/", "11", "November", "2003"]
tempat_tanggal_lahir = ' / '.join(TTL)
print("Tempat / Tanggal Lahir:", tempat_tanggal_lahir)

nama = ['Awang', 'Praja', 'Anugerah']
nama_mhs = ' '.join(nama)
print("Nama Mahasiswa:", nama_mhs)