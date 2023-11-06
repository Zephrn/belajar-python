import datetime

panjang = 45

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
print("Minuman : ")
minuman = {
    "Robusta Coffe Milk": 17000,
    "Black Sasame Coffe": 23000,
    "Cappicino Cincau": 28000,
    "Arabica Coffe Milk": 20000,
    "Coffe Latte \t": 22000,
    "Americano Arabica": 14000
}
for item, price in minuman.items():
    print(f"{item} \t: Rp{price}")

print("\nMakanan : ")
makanan = {
    "Beef Bulgogi": 35000,
    "Chicken Steak": 30000,
    "Chicken Katsu": 26000,
    "Nasi Goreng": 35000,
    "Mie Goreng ": 35000,
    "Bakso Goreng": 35000
}

for item, price in makanan.items():
    print(f"{item} \t: Rp{price}")

nama = str(input("nama pelanggan : "))
meja = int(input("nomor meja : "))

total = 0
pesanan = {}

while True:
    pilihan = input("Masukkan nama makanan atau ketik 'selesai' untuk mengakhiri: ")
    if pilihan.lower() == 'selesai':
        break
    elif pilihan in makanan:
        if pilihan in pesanan:
            pesanan[pilihan] += 1
        else:
            pesanan[pilihan] = 1
        total += makanan[pilihan]
        print(f"{pilihan} ditambahkan ke daftar pesanan.")

print("\nDaftar Pesanan:")
for item, quantity in pesanan.items():
    print(f"{item:15} : {quantity}")

print(f"\nTotal harga yang harus dibayar: Rp{total}")

tanggal_sekarang = datetime.datetime.now()
print(f"Waktu Pembayaran: {tanggal_sekarang}")
