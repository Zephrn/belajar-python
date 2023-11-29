#List teman
teman = ["Hafidz","Riki","Adit","Fadhil","Lutfi"]

#Isi list Indeks nomer 3
print("teman nomor ke-3 adalah : ", format(teman[3]))
print("="*50)
#Output Semua teman dengan perulangan
for bro in teman:
    print(bro)
print("="*50)
#panjang list
print("Semua temanku: ada {} orang".format(len(teman)))
print("="*50)
#Menambahkan satu teman di awal bernama Nizar
teman.insert(0,"Nizar")
teman.append("Ferdi")

for bro in teman:
    print(bro)
print("="*50)
print("Semua temanku: ada {} orang".format(len(teman)))
print("="*50)

