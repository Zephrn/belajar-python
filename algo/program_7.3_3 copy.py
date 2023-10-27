my_list = ['rusa', 'buaya', 'kucing', 'elang', 'bebek']
new_element = "a"

extended_list = []

# Menambahkan setiap elemen dari list asli ke list yang diperpanjang
for item in my_list:
    extended_list.append(new_element)
    extended_list.append(item)

# Menampilkan list yang telah diperpanjang
print("Original List: ",my_list)
print("memasukkan huruf 'a' di antara setiap isi list: ",extended_list)
