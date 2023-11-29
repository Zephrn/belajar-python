# import luas.lingkaran as ll
# import luas.persegi as lp
# import luas.segitiga as ls

# lk = int(input("masukan radius lingkaran : "))
# print(f"luas lingkarang adalah {ll.luas_lingkaran(radius=lk)}")


# # menghitung persegi
# print()
# lps = int(input("masukan sisi persegi : "))
# print(f"luas persegi adalah {lp.luas_persegi(sisi=lps)}")


# # mengitung segitiga
# print()
# lpsg = int(input("masukan alas persegi : "))
# lpsg1 = int(input("masukan tinggi persegi : "))
# print(f"luas segitiga adalah {ls.luas_segitiga(alas=lpsg, tinggi=lpsg1)}")


import volume.bola as vb
import volume.kubik as vk
import volume.trapesium as vt
print()
# menghitung bola 
a = int(input("masukan jari bola : "))
(f"volume bola adalah {vb.bola(jari=20)}")


print()
b = int(input("masukan sisi persegi : "))
(f"volume persegi adalah {vk.kubik(sisi=b)}")


print()
c = int(input("masukan tinggi trapesium : "))
d = int(input("masukan alas1 trapesium : "))
e = int(input("masukan alas2 trapesium : "))
(f"volume persegi adalah {vt.trapesium(tinggi=c, alas1=d, alas2=e)}")