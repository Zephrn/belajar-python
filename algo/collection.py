# # membuat tuple data mahasiswa 
# nama_mhs = ('fadil rahman hakim', 'sanggau', '18')

# # mengekstrak data 
# # dengan sequence unpacking 
# nama, tempatlahir, umur = nama_mhs


# print("nama Mahasiswa \t: ", nama, "index", nama_mhs[0])
# print("tempat lahir  \t: ", tempatlahir, "index", nama_mhs[1])
# print("umur  \t\t: ", umur, "index", nama_mhs[2])



# # menggabungakn dua buah tupel 
# no_urut = (1, 2, 3, 4, 5 )
# nilai = (78,76,88,90)
# NA = no_urut + nilai
# print(NA)

# NIM = ('001', '002', '003', '004', '005')
# Nama = ('Diana','Desi','Tekla')
# daftar_mhs = NIM + Nama
# print(daftar_mhs)




# print(f" NO : {NA[0]} \n NIM : {NIM[0]} \n NAMA : {Nama[0]} \n Nilai : {nilai[0]}")

# menggunakan fungsi pada tupel 

nama_mhs = ('Dwiky', 'Surya', 'Riki', 'Afriza', 'Wagina')
huruf = '88', '89', 'gita', 'Andi', 'a', 'z', '3.5', '4.0'
nilai_alpro = ('88','89','80','90','92','87','75')

print("="*20,"maximal","="*20)
print("nilai tertinggi : ", max(nama_mhs))
print("nilai tertinggi : ", max(huruf)) 
print("nilai tertinggi : ", max(nilai_alpro)) 
print("="*20,"minimal","="*20)
print("nilai tertinggi : ", min(nama_mhs))
print("nilai tertinggi : ", min(huruf)) 
print("nilai tertinggi : ", min(nilai_alpro)) 
print("="*20,"panjang huruf","="*20)
print("nilai tertinggi : ", len(huruf)) 
print("nilai tertinggi : ", len(nama_mhs))
print("nilai tertinggi : ", len(nilai_alpro)) 