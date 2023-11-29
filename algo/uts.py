import datetime

# Panjang teks
panjang = 45

# Login
print("Login Casher CwCoffe".center(panjang), "\n") 
while True:
    try:
        keys = "admin"
        login = str(input("masukan id \t: "))
        pw = str(input("masukan pw \t: "))
        if login == keys and pw == keys:
            print("\n","anda berhasil login".center(panjang))
            break
        else:
            print("\n","password salah".center(panjang))
    except ValueError:
        print("password salah".center(panjang))
print("\n")
print("Selamat Datang Di".center(panjang))
print(" CwCoffe & Eatery".center(panjang))
print("\n","MENU".center(panjang),"\n")

# Daftar menu dan harganya
minuman = {
    1: {"name": "Robusta Coffe Milk", "price": 17000},
    2: {"name": "Black Sasame Coffe", "price": 23000},
    3: {"name": "Cappicino Cincau", "price": 28000},
    4: {"name": "Arabica Coffe Milk", "price": 20000},
    5: {"name": "Coffe Latte", "price": 22000},
    6: {"name": "Americano Arabica", "price": 14000}
}

makanan = {
    1: {"name": "Beef Bulgogi", "price": 35000},
    2: {"name": "Chicken Steak", "price": 30000},
    3: {"name": "Chicken Katsu", "price": 26000},
    4: {"name": "Nasi Goreng", "price": 35000},
    5: {"name": "Mie Goreng", "price": 35000},
    6: {"name": "Bakso Goreng", "price": 35000}
}

# Cetak daftar menu
print("Minuman : ")
for item in minuman.values():
    print(f"{item['name']} \t: Rp{item['price']}")

print("\nMakanan : ")
for item in makanan.values():
    print(f"{item['name']} \t\t: Rp{item['price']}")

# Input nama pelanggan dan nomor meja
print("")
nama = str(input("nama pelanggan : "))
meja = str(input("nomor meja : "))
print("")
# Inisialisasi variabel total dan pesanan
total = 0
pesanan = {}

# Pilih menu
while True:
    pilihan = input("isi menu. 'x' untuk end: ")
    if pilihan.lower() == 'x':
        break
    elif pilihan in [item['name'] for item in makanan.values()] or pilihan in [item['name'] for item in minuman.values()]:
        jenis = ''
        if pilihan in [item['name'] for item in makanan.values()]:
            jenis = 'makanan'
        elif pilihan in [item['name'] for item in minuman.values()]:
            jenis = 'minuman'
        jumlah = int(input(f"Masukkan jumlah {pilihan} {jenis} yang dipesan: "))
        if jenis == 'makanan':
            for item in makanan.values():
                if item['name'] == pilihan:
                    if pilihan in pesanan:
                        pesanan[pilihan] += jumlah
                    else:
                        pesanan[pilihan] = jumlah
                    total += item['price'] * jumlah
                    print(f"{pilihan} ditambahkan ke daftar pesanan.")
        elif jenis == 'minuman':
            for item in minuman.values():
                if item['name'] == pilihan:
                    if pilihan in pesanan:
                        pesanan[pilihan] += jumlah
                    else:
                        pesanan[pilihan] = jumlah
                    total += item['price'] * jumlah
                    print(f"{pilihan} ditambahkan ke daftar pesanan.")
    else:
        print("Menu tidak valid. Silakan pilih menu yang tersedia.")

# Cetak pesanan dan total
for item, jumlah in pesanan.items():
    print(f"{item} \t: {jumlah}")

# Hitung pajak dan total harga
pajak = total * 0.11
total_pajak = pajak + total
print("\ntotal : ",total)
print("ntrtotal dengan pajak 11%: ",int(total_pajak))

# Pilih metode pembayaran
while True:
    metode = input("metode pembayaran cash or e-money : ")
    if metode == "e-money":
        e = total_pajak
        eme = "e-money"
        sungsong = 0
        break
    elif metode == "cash":
        bayar = int(input("bayaran : "))
        em = "cash"
        sungsong = bayar - total
        while bayar < total_pajak:
                print("uang tidak cukup")
                bayar = int(input("bayaran : "))
        bayar1 = bayar
        sungsong = bayar - total_pajak
        break


            
        
       

print("\n\n")

# Informasi toko
tokoh = "CWCoffe & Eatery"
jln = "Dansen"
alamat = "Jl Danau Sentarum No. 30, Sungai Bangkok, Kec."
kota = "Pontianak Kota"
no_hp = "08517441286"
tanggal_waktu_sekarang = datetime.datetime.now()
tanggal_waktu_diformat = tanggal_waktu_sekarang.strftime("%d/%m/%Y %H:%M:%S")
casir = "Dansen Cw Coffe"
makanan_names = [item['name'] for item in makanan.values()]
minuman_names = [item['name'] for item in minuman.values()]


# Cetak struk
print(tokoh.center(panjang))
print(jln.center(panjang))
print(alamat.center(panjang))
print(kota.center(panjang))
print(no_hp.center(panjang))
print(f"Nomor meja : {meja}".center(panjang))
print("")
print("="*panjang)
print( '%-24s %20s' % ("Order Date", tanggal_waktu_diformat))
print( '%-24s %20s' % ("Cashier", casir))
print("="*panjang)
print("")
print("Nama pemesan : ", nama)
print("Pesanan: ")
for item, jumlah in pesanan.items():
    if item in makanan_names:
        for makanan_item in makanan.values():
            if makanan_item['name'] == item:
                harga_item = makanan_item['price']
                print('%-1s %-22s %20s' % (jumlah, item, harga_item * jumlah))
                break
    elif item in minuman_names:
        for minuman_item in minuman.values():
            if minuman_item['name'] == item:
                harga_item = minuman_item['price']
                print('%-1s %-22s %20s' % (jumlah, item, harga_item * jumlah))
                break
    else:
        print(f"Menu {item} tidak ditemukan.")
print("="*panjang)
print( '%-24s %20s' % ("Subtotal", total))
print( '%-24s %20s' % ("pajak 11%", int(pajak)))
print( '%-24s %20s' % ("Total", int(total_pajak)))
print("")

if metode == "cash":
    print( '%-24s %20s' % (em, bayar1))
elif metode == "e-money":
        print( '%-24s %20s' % (eme, int(e)))
print( '%-24s %20s' % ("Kembali", int(sungsong)))
print("")
print("CWCoffe.id".center(panjang))
print("\n")
print("Thanks for stopping by.".center(panjang))
