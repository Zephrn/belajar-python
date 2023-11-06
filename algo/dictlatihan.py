bio = {
    "nama" : "fadil rahman hakim",
    "panggilan" : "fadil",
    "tempat lahir" : "sanggau",
    "tanggal lahir" : "25 september 2005",
    "jenis kelamin" : "laki laki",
    "Agama" : "islam",
    "Alamat rumah" : "jalan kesatriaan nomo 80",
    "Nomor Telepon" : "082253889636",
    "Alamat email" : "fadilrahmanhakim@gmail.com",
    "Hobi" : "olahraga",
    "Cita Cita" : "kapal laut" 
}
# bio = dict (
# nama = "fadil rahman hakim",
# panggilan = "fadil",
# tempat_lahir = "sanggau",
# tanggal_lahir = "25 september 2005",
# jenis_kelamin = "laki laki",
# Agama = "islam",
# Alamat_rumah = "jalan kesatriaan nomo 80",
# Nomor_Telepon = "082253889636",
# Alamat_email = "fadilrahmanhakim@gmail.com",
# Hobi = "olahraga",
# Cita_Cita = "kapal laut" 
# )

print("nama lengkap \t:",bio["nama"])
print("panggilan \t:",bio["panggilan"])
print("tempat lahir \t:",bio["tempat lahir"])
print("tanggal lahir \t:",bio["tanggal lahir"])
print("jenis kelamin \t:",bio["jenis kelamin"])
print("agama \t\t:",bio["Agama"])
print("alamat rumah \t:",bio["Alamat rumah"])
print("nomor telepon \t:",bio["Nomor Telepon"])
print("alamat email \t:",bio["Alamat email"])
print("hobi \t\t:",bio["Hobi"])
print("ciita cita \t:",bio["Cita Cita"])

print("\n")
# menggunakan get agar tidak eror saat kesalahan memanggil menjadi none
print(bio.get("nama saya"))
print("panggilan \t: ",bio.get("panggilan"))
print("tempat lahir \t: ",bio.get("tempat lahir"))
print("tanggal lahir \t: ",bio.get("tanggal lahir"))
print("jenis kelamin \t: ",bio.get("jenis kelamin"))
print("agama \t\t: ",bio.get("Agama"))
print("alamat rumah \t: ",bio.get("Alamat rumah"))
print("nomor telepon \t: ",bio.get("Nomor Telepon"))
print("alamat email \t: ",bio.get("Alamat email"))
print("hobi \t\t: ",bio.get("Hobi"))
print("ciita cita \t: ",bio.get("Cita Cita"))

print("\n")

# print menggunakan perulangan 
for kunci in bio:
    print(kunci, ' \t:',bio[kunci])

print("\n")

# merubah value 
print("nama awal\t\t: ", bio.get("nama")) 
bio["nama"] = "pudidil"
print("setelah nama diubah\t: ", bio.get("nama"))

print("\n")

# manambah data 
bio["makanan enak"] = "ayam goreng"
print("makanan favorite dari {} adalah {}" .format(bio.get("nama"), bio.get("makanan enak")))

print("\n")

# coba menimpa key baru 
bio["makanan enak"] = "ayam semur"
print("makanan favorite dari {} adalah {}" .format(bio.get("nama"), bio.get("makanan enak")))

# mencoba print loop 
for kunci in bio:
    print(kunci, ' \t:',bio[kunci])

print("\n")

# mencoba menghapus key 
del bio["Hobi"]
bio.pop("Alamat rumah")

for kunci in bio:
    print(kunci, ' \t:',bio[kunci])

print("\n")

# pesan 
pesan_singkat = {"isi": "ISI PESAN INI HANYA BISA DIBACA SEKALI SAJA!! 😱"}
isi_pesan = pesan_singkat.pop('isi')
# akses langsung dari dictionary
# ouput: None
print('isi pesan:', pesan_singkat.get('isi'))
# akses dari hasil kembalian yang telah disimpan
print('isi pesan:', isi_pesan)

print("\n")

# operator keanggotaan 
siswa = {"nama" : "fadil rahman"}
print("nama" in siswa)

print("\n")

# menghitung key 
print("jumlah data di bio adalah : ", len(bio))


# multi dictionary list
multi_dict1 = dict(
    nama = ['Muhammad', 'adli',  'barry', 'ananda'],
    umur = ['17', '18', '17', '18'],
    alamat = ['siantan', 'punggur', 'serdam', 'kobar']
)

# multi_dict1["nama"] = 'riki'
# multi_dict1["umur"] = '18'
# multi_dict1["alamat"] = 'sungai duri'

print(multi_dict1.get("nama")[0], multi_dict1.get("umur")[0])
print(multi_dict1["nama"][1])
print("akhir dari dict\n")

# multi dictionary2 data tuple
multi_dict2 = dict(
    nama = ('Muhammad', 'adli',  'barry', 'ananda'),
    umur = ('17', '18', '17', '18'),
    alamat = ('siantan', 'punggur', 'serdam', 'kobar')
)

# multi_dict1["nama"] = 'riki'
# multi_dict1["umur"] = '18'
# multi_dict1["alamat"] = 'sungai duri'
tampung = multi_dict2["nama"][2], multi_dict2["umur"][2], multi_dict2["alamat"][2]
print(tampung)
print("akhir dari dict\n")

# multi dictionary3 data tuple
multi_dict3 = {
    'nama': {'mhs1': 'Muhammad', 'mhs2': 'adli', 'mhs3': 'barry', 'mhs4': 'ananda'},
    'umur': {'umur1': '17', 'umur2': '18', 'umur3': '17', 'umur4': '18'},
    'alamat': {'alt1': 'siantan', 'alt2': 'punggur', 'alt3': 'serdam', 'alt4': 'kobar'}
}


# # Merubah data pada dictionary
# multi_dict3["nama"]["mhs1"] = 'riki'
# multi_dict3["umur"]["umur1"] = '18'
# multi_dict3["alamat"]['alt1'] = 'sungai duri'

# Menampilkan data setelah perubahan

# Memasukkan data ke variabel tampung
tampung = multi_dict3["nama"]["mhs1"], multi_dict3["umur"]["umur1"], multi_dict3["alamat"]['alt1']

# Menampilkan nilai yang ditampung
print(tampung)
print("akhir dari dict\n")

