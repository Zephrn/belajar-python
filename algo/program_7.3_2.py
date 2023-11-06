# kata yang ingin di filter menampilkan lebih dari 5 huruf
original_string = "Pada hari Senin, Saya Belajar Mata Kuliah Algoritma Pemrograman di Kelas TI-A\n Gedung Teori Bersama di Jurusan Teknik Elektro Program Studi D3 Teknik\n Informatika yahg berada di lantai 2 pada Pukul 07.00 WIB sampai dengan 14.40\n WIB. Perkuliahan di laksanakan menggunakan bantuan papan tulis, proyektor,\n spidol, e-learning, power point, spidol, dan pena."
filter_kata = 5

print(" ini adalah original string : \n", original_string)
print("\n")

# fungsi memfilter kata 

kata = original_string.split()
filter = [kata for kata in kata if len(kata) > filter_kata]
filter_k = [kata for kata in kata if len(kata) < filter_kata]
filter_string = ' '.join(filter)
print("ini merupakan kata yang sudah di filter lebih dari 5 kata: \n", filter_string.split())
print(f"\nterdapa {len(filter)} kata yang terfilter lebih dari 5")
