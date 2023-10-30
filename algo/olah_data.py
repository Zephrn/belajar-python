# with open("algo/wala.txt", "r") as file:
#     wala = file.read()
# wala1 = wala.split()
# # print(wala1)
# kelas1a = set(wala1)
# print(kelas1a)


with open("algo/kelas1a.txt", "r") as file:
    kelas1a = file.read()
with open("algo/kelas1b.txt", "r") as file:
    kelas1b = file.read()
with open("algo/kelas1c.txt", "r") as file:
    kelas1c = file.read()
with open("algo/kelas1d.txt", "r") as file:
    kelas1d = file.read()
with open("algo/kelas1e.txt", "r") as file:
    kelas1e = file.read()

# print(kelas1a)
# print(kelas1b)
# print(kelas1c)
# print(kelas1d)
# print(kelas1e)

# mensplit data menjadi perkata 
kelas_1A = kelas1a.split()
kelas_1B = kelas1b.split()
kelas_1C = kelas1c.split()
kelas_1D = kelas1d.split()
kelas_1E = kelas1e.split()
list_kelas = (kelas_1A + kelas_1B + kelas_1C + kelas_1D + kelas_1E)
# mengubah data list menjadi set 
set_a = set(kelas_1A)
set_b = set(kelas_1B)
set_c = set(kelas_1C)
set_d = set(kelas_1D)
set_e = set(kelas_1E)

# print(set(set_a), "\n")
# print(set(set_b), "\n")
# print(set(set_c), "\n")
# print(set(set_d), "\n")
# print(set(set_e), "\n")


# fungsi union 
print("="*20, "union", "="*20, "\n")

print("="*20, "program 1a", "="*20)
# program 1.a
# data sebelum union 1 a
union_1a = set_a.union(set_b, set_c, set_d, set_e)
jumlah_1a =  len(list_kelas) - len(union_1a)

# jumlah data 1 a
# Menentukan jumlah baris
jumlah_baris = len(union_1a)

# Melakukan iterasi untuk mencetak data dengan new line setiap 10 baris
for i, data in enumerate(union_1a, 1):
    print({data}, end="\n" if i % 5 == 0 else " ")

# analisin data 1 b 
print("\n\n", "="*20, "PROGRAM 1B", "="*20)
print("hasil analisin program union : ")
irisan_1a = set_a.intersection(set_b, set_c, set_d, set_e)
print(f"kata yang sama \t\t: {irisan_1a}\njumlah kata union \t: {len(union_1a)} \nselisih union dan list \t: {jumlah_1a}")
print("="*53,"\n")
print("*"*100,"\n")


# ===========================================================================================


# program 2.a 
# irisan 2 kelas
irisan_2a = set_a.intersection(set_b)
pj = f"nama-nama irisan antara 2 kelas A dan B : {irisan_2a}"
pja = len(pj) // 2
print("PROGRAM 2 A : ")
print("=" *pja * 2)
print(pj)
print("=" *pja * 2, "\n")
# program 2.b 
# irisan tiga kelas
print("="*20, "program 2b", "="*20)
irisan_2b = set_c.intersection(set_d).union(set_c.intersection(set_e))
irisan_2b_b = set_c.intersection(set_d, set_e)
print(f"diantara 3 kelas ada beberapa nama yang masuk irisan or yaitu : \n {irisan_2b}")
print(f"diantara 3 kelas ada beberapa nama yang masuk irisan and yaitu : \n {irisan_2b_b} \n")

# program 2.c
# irisan lima kelas 
print("="*20, "program 2c", "="*20)
irisan_2c = set_a.intersection(set_b, set_c, set_d, set_e)
print(f"diantara 5 kelas ada beberapa nama yang masuk irisan yaitu : {irisan_2c} \n")
print("*"*100,"\n")



# program 3 fungsi difference

# prog 3a 
union_3a = set_a.union(set_b)
difference_3a = set_a.difference(set_b)

# prog 3b 
union_3b = set_c.union(set_d)
difference_3b = set_c.difference(set_d)

# prog 3c 
union_3c = set_e.union(set_a)
difference_3c = set_e.difference(set_a)





# mencetak program A 
print("PROGRAM 3 A : \n")
print("gabungan dari kelas A dan B : \n")


# Melakukan iterasi untuk mencetak data dengan new line setiap 10 baris
for i, data in enumerate(union_3a, 1):
    print({data}, end="\n" if i % 5 == 0 else " ")

print("\n\ndifference dari kelas A dan B : \n")

for i, data in enumerate(difference_3a, 1):
    print({data}, end="\n" if i % 5 == 0 else " ")


# mencetak program b 

print("PROGRAM 3 B : \n")
print("gabungan dari kelas C dan D : \n")


# Melakukan iterasi untuk mencetak data dengan new line setiap 10 baris
for i, data in enumerate(union_3b, 1):
    print({data}, end="\n" if i % 5 == 0 else " ")

print("\n\ndifference dari kelas C dan D : \n")

for i, data in enumerate(difference_3b, 1):
    print({data}, end="\n" if i % 5 == 0 else " ")



print("PROGRAM 3 C : \n")
print("gabungan dari kelas E dan A : \n")


# Melakukan iterasi untuk mencetak data dengan new line setiap 10 baris
for i, data in enumerate(union_3c, 1):
    print({data}, end="\n" if i % 5 == 0 else " ")

print("\n\ndifference dari kelas E dan A : \n")

for i, data in enumerate(difference_3c, 1):
    print({data}, end="\n" if i % 5 == 0 else " ")


print("PROGRAM 4 A")

s_dif_a = set_a.symmetric_difference(set_b)
spa = len(s_dif_a)
# Perbedaan simetris antara set_a dan set_b, set_c
s_dif_b = set_a.symmetric_difference(set_b).symmetric_difference(set_c)
spb = len(s_dif_b)

# Perbedaan simetris antara set_a, set_b, set_c, set_d, set_e
s_dif_c = set_a.symmetric_difference(set_b).symmetric_difference(set_c).symmetric_difference(set_d).symmetric_difference(set_e)
spc = len(s_dif_c)


# mencetak program A 
print("\nPROGRAM 4 A : \n")
print("symmentric different dari kelas A dan B : \n")


# Melakukan iterasi untuk mencetak data dengan new line setiap 10 baris
for i, data in enumerate(s_dif_a, 1):
    print({data}, end="\n" if i % 5 == 0 else " ")
print(spa)

# mencetak program B 


print("\nPROGRAM 4 B : \n")
print("symmentric different dari kelas A, B dan C : \n")


# Melakukan iterasi untuk mencetak data dengan new line setiap 10 baris
for i, data in enumerate(s_dif_b, 1):
    print({data}, end="\n" if i % 5 == 0 else " ")
print(spb)



# mencetak program c 


print("\nPROGRAM 4 C : \n")
print("symmentric different dari semua kelas : \n")


# Melakukan iterasi untuk mencetak data dengan new line setiap 10 baris
for i, data in enumerate(s_dif_c, 1):
    print({data}, end="\n" if i % 5 == 0 else " ")
print(spc)

