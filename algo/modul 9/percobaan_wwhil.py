#Membuat sebuah list kosong untuk menampung belanja
barang =[]
stop = False
i = 0

print(">>>>> Selamat Datang di Alti MART <<<<<")
print("Silahkan masukkan barang belanjaan anda!")
while(not stop):
    barang_baru = str(input("Masukkan barang yang ke-{}: ".format(i)))
    barang.append(barang_baru)
    
    #increment i
    i += 1
    
    tanya = str(input("Mau mengisi belanja lagi? (y/t): "))
    if(tanya == "t"):
        stop = True
        
#mencetak semua baranag baru yang dimasukkan

print('~'*30)
print("Kamu Belanja sebanyak {} barang".format(len(barang)))
for barangku in barang:
    print("-{}".format(barang_baru))
print('~'*30)