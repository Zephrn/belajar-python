import datetime
import subprocess

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
    "RCM": {"name": "Robusta Coffe Milk", "price": 17000},
    "BSM": {"name": "Black Sasame Coffe", "price": 23000},
    "CC": {"name": "Cappicino Cincau", "price": 28000},
    "ACM": {"name": "Arabica Coffe Milk", "price": 20000},
    "CL": {"name": "Coffe Latte", "price": 22000},
    "AA": {"name": "Americano Arabica", "price": 14000}
}

makanan = {
    "BB": {"name": "Beef Bulgogi", "price": 35000},
    "CS": {"name": "Chicken Steak", "price": 30000},
    "CK": {"name": "Chicken Katsu", "price": 26000},
    "NG": {"name": "Nasi Goreng", "price": 35000},
    "MG": {"name": "Mie Goreng", "price": 35000},
    "BG": {"name": "Bakso Goreng", "price": 35000}
}

# Cetak daftar menu
# print("Minuman : ")
# for key, item in minuman.items():
#     print(f"{key}: {item['name']} \t: Rp{item['price']}")

# print("\nMakanan : ")
# for key, item in makanan.items():
#     print(f"{key}: {item['name']} \t\t: Rp{item['price']}")
print("Menu Minuman:")
print("{:<5} {:<25} {:<10}".format("Kode", "Nama Minuman", "Harga\t"))
for code, item in minuman.items():
    print("{:<5} {:<25} {:<10}".format(code, item["name"], item["price"]))

print("\nMenu Makanan:")
print("{:<5} {:<25} {:<10}".format("Kode", "Nama Makanan", "Harga"))
for code, item in makanan.items():
    print("{:<5} {:<25} {:<10}".format(code, item["name"], item["price"]))

# Input nama pelanggan dan nomor meja
print("")
nama = str(input("Nama pelanggan: "))
meja = str(input("Nomor meja: "))
while True:

    letak = str(input("letak meja atas atau bawah : "))

    if not letak:
        print("tidak boleh kosong")
        continue

    if letak == "atas":
        break
    elif letak == "bawah":
        break
    
    else:
        print("input salah")

while True:

    DINEIN_OR_T = str(input("denien or take away  : "))

    if not DINEIN_OR_T:
        print("tidak boleh kosong")
        continue

    if DINEIN_OR_T == "denien":
        break
    elif DINEIN_OR_T == "take away":
        break
    
    else:
        print("input salah")

print("")
# Inisialisasi variabel total dan pesanan
total = 0
pesanan = {}

# Pilih menu
while True:
    pilihan = input("Isi menu. 'x' untuk end: ")
    if pilihan.lower() == 'x':
        break
    elif pilihan in makanan or pilihan in minuman:
        jenis = ''
        if pilihan in makanan:
            jenis = 'makanan'
        elif pilihan in minuman:
            jenis = 'minuman'
        jumlah = int(input(f"Masukkan jumlah {pilihan} {jenis} yang dipesan: "))
        if jenis == 'makanan':
            item = makanan[pilihan]
        elif jenis == 'minuman':
            item = minuman[pilihan]

        if pilihan in pesanan:
            pesanan[pilihan]['jumlah'] += jumlah
        else:
            pesanan[pilihan] = {'item': item, 'jumlah': jumlah}

        total += item['price'] * jumlah
        print(f"{pilihan} ditambahkan ke daftar pesanan.")
    else:
        print("Menu tidak valid. Silakan pilih menu yang tersedia.")


# Cetak pesanan dan total
for item, jumlah in pesanan.items():
    print(print(f"{item}: {jumlah['item']['name']} \t\t: Rp{jumlah['item']['price']}"))

# Hitung pajak dan total harga
pajak = total * 0.11
total_pajak = pajak + total
print("\ntotal : ",total)
print("total dengan pajak 11%: ",int(total_pajak))

# Pilih metode pembayaran
while True:
    metode = input("metode pembayaran cash or e-money: ")

    if not metode:
        print("tidak boleh kosong")
        continue

    if metode == "e-money":
        e = total_pajak
        eme = "e-money"
        sungsong = 0
        break

    elif metode == "cash":
        while True:
            try:
                bayar = int(input("bayaran : "))
                if bayar < total_pajak:
                    print("uang tidak cukup")
                    continue
                else:
                    bayar
                    em = "cash"
                    sungsong = bayar - total_pajak
                    break
            except ValueError:
                print("masukan nominal angka")
        break
    else:
        print("input salah")



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
pesanana = f"{meja} {letak}" 

# Cetak struk
receipt = f"""
{tokoh.center(panjang)}
{jln.center(panjang)}
{alamat.center(panjang)}
{kota.center(panjang)}
{no_hp.center(panjang)}
{f"Receipt No.\t{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}".center(panjang)}
{DINEIN_OR_T.center(panjang)}

{"=" * panjang}
{'%-24s %20s' % ("Order Date", tanggal_waktu_diformat)}
{'%-24s %20s' % ("Cashier", casir)}
{"=" * panjang}

Nama pemesan : {nama}
Pesanan: 
"""

for item, pesanan_detail in pesanan.items():
    if item in makanan:
        harga_item = makanan[item]['price']
        receipt += f"{'%-1s %-22s %20s' % (pesanan_detail['jumlah'], makanan[item]['name'], harga_item * pesanan_detail['jumlah'])}\n"
    elif item in minuman:
        harga_item = minuman[item]['price']
        receipt += f"{'%-1s %-22s %20s' % (pesanan_detail['jumlah'], minuman[item]['name'], harga_item * pesanan_detail['jumlah'])}\n"
    else:
        receipt += f"Menu {item} tidak ditemukan.\n"

receipt += f"""{"=" * panjang}
{'%-24s %20s' % ("Subtotal", total)}
{'%-24s %20s' % ("pajak 11%", int(pajak))}
{'%-24s %20s' % ("Total", int(total_pajak))}
"""

if metode == "cash":
    receipt += f"{'%-24s %20s' % (em, bayar)}\n"
elif metode == "e-money":
    receipt += f"{'%-24s %20s' % (eme, int(e))}\n"

receipt += f"{'%-24s %20s' % ('Kembali', int(sungsong))}\n"
receipt += f"""

{ "CWCoffe.id".center(panjang)}
\n
{pesanana.center(panjang)}
{'Thanks for stopping by.'.center(panjang)}
"""

print(receipt)

ntpd = "receipt.txt"

with open(ntpd, "w") as file:
    file.write(receipt)

print(f"Receipt saved to {ntpd}")



# Buka Notepad dengan file program sementara
subprocess.run(["notepad.exe", ntpd])

# Opsional: Tambahkan penundaan agar Notepad memiliki waktu untuk membuka file
import time
time.sleep(2)

# Hapus file program sementara setelah Notepad ditutup
import os
os.remove(ntpd)