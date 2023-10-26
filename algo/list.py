buah = ['Pisang', 'Nanas', 'Melon', 'Durian', 'Duku', 'Semangka', 'a', '21', 'buah', 'a', 'd']
print("list buah")

# positif
# print(buah [0])
# print(buah [1])
# print(buah [2])
# print(buah [3])
# print(buah [4])
# print(buah [5])
# negatif
# print("\n")
# print(buah [-1])
# print(buah [-2])
# print(buah [-3])
# print(buah [-4])
# print(buah [-5])
# print(buah [-6])
# print("\n")
# # slicer
# print(buah [:5])
# print(buah [3:])
# print(buah [2:6])
# print(buah [-5:])
# print(buah [:-3])
# print(buah [2:-3])
# print(buah [-2:5])
# ubah list
buah[0] = "banana"
buah[-3] = "apel"
buah[-1] = "buah naga"
buah[4] = "alpukat"
buah[1] =  "rambutan"
buah[2:3] = ["lemon"]
print(buah)
# mengubah list sekaligus
buah[3:6] = ['manggis', 'anggur', 'sirsak']
# memasukan data menggunakan append
buah.append("kiwi")
print(buah)
# memasukan menggunakan insert
buah.insert(6, 'jambu')
print(buah)
buah.insert(7, 'jambu')
print(buah)
# penghapusan pop
buah.pop()
print(buah)
# menggunakan remove untuk menghapus sesuai data
buah.remove('sirsak')
print(buah)
# menghapus secara banyak menggunakan del
del buah[0:2]
print(buah)
# mengurutkan sort
buah.sort()
print(buah)
# mengurutkan reverse
buah.reverse()
print(buah)
# mengurutkan huruf angka
a = ['a', 'B', '1', 'C']
a.sort()
print(a)
