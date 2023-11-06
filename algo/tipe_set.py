# # menggunakan tipe data set 
# # tipe data set menggunakan kurung kurawal {} 

# print('>>>> set dengan kurung kurawal')
# newprov = {'papua tengah', 'papua penggunungan', 'papua selatan', 'papua barat daya'}
# print(newprov)

# # mengkonversu list ke dalam set 
# print('>>>> konverensi list kedalam set')
# gugusan_pulau = set(['sumatera', 'jawa', 'kalimantan', 'sulawesi', 'maluku', 'papua', 'bali'])
# print(gugusan_pulau)


# # set dengan tipe data yang berbeda
# print('>>>> set tipe data yang berbeda-beda')
# set_campuran = {'mahasiswa', 'teknik informatika', 3, True,('A', 'B')}
# print(set_campuran)

# lagu_guruku = ['pagi', 'ku', 'cerah', 'ku', 'matahari', 'bersinar', 'ku', 'gendong', 'tas', 'merah', 'ku', 'dipundang']
# print(set(lagu_guruku))


# # menggunakan fungsi add dan update pada tipe data set
# huruf_abjad = {'a', 'b', 'c', 'd', 'e'}
# print("Anggota set data awal. \n",  huruf_abjad)

# # menambah data dalam setsatu per satu 
# huruf_abjad.add('g')
# huruf_abjad.add('f')


# # menambah data dalam set lebih dari satu anggota sekaligus 
# # menambah dangan data set 

# huruf_abjad.update({'h', 'i'})
# # menambah data list 
# huruf_abjad.update(['j', 'k'])


# print("\n anggota set setelah berfungsi add dan update." , huruf_abjad)

# # menggunakan funsi remove untuk menghilangkan data 
# huruf_abjad.remove('h')
# print(huruf_abjad)
# huruf_abjad.discard('k')
# print(huruf_abjad)
# huruf_hapus = huruf_abjad.pop()
# print(huruf_abjad)


# dua buah set 

grup_smp = {'andi', 'fadil', 'adit', 'rayhan', 'akmal'}
grup_sma = {'andi', 'budi', 'adit', 'agus', 'ratna'}
# union atau gabungan 
print(grup_smp | grup_sma)
print(grup_smp.union(grup_sma))
# irisan 
print(grup_smp & grup_sma)
print(grup_smp.intersection(grup_sma))
# difference 
print(grup_smp - grup_sma)
print(grup_smp.difference(grup_sma))
print(grup_sma - grup_smp)
print(grup_sma.difference(grup_smp))
# symmetric 
print(grup_smp.symmetric_difference(grup_sma))
