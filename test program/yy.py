import streamlit as st
import datetime

# Panjang teks
panjang = 45

# Login
def login():
    keys = "admin"
    login = st.text_input("masukan id \t: ")
    pw = st.text_input("masukan pw \t: ")
    if login == keys and pw == keys:
        st.write("\n", "anda berhasil login".center(panjang))
        return True
    else:
        st.write("\n", "password salah".center(panjang))
        return False

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
def cetak_menu():
    st.write("Minuman : ")
    for item in minuman.values():
        st.write(f"{item['name']} \t: Rp{item['price']}")

    st.write("\nMakanan : ")
    for item in makanan.values():
        st.write(f"{item['name']} \t\t: Rp{item['price']}")

# Input nama pelanggan dan nomor meja
def input_pelanggan():
    global nama
    nama = st.text_input("nama pelanggan : ")

    global meja
    meja = st.text_input("nomor meja : ")

# Pilih menu
def pilih_menu():
    global pesanan
    pilihan = st.text_input("isi menu. 'x' untuk end: ")
    if pilihan.lower() == 'x':
        return
    elif pilihan in [item['name'] for item in makanan.values()] or pilihan in [item['name'] for item in minuman.values()]:
        jenis = ''
        if pilihan in [item['name'] for item in makanan.values()]:
            jenis = 'makanan'
        elif pilihan in [item['name'] for item in minuman.values()]:
            jenis = 'minuman'
        jumlah = int(st.text_input(f"Masukkan jumlah {pilihan} {jenis} yang dipesan: "))
        if jenis == 'makanan':
            for item in makanan.values():
                if item['name'] == pilihan:
                    if pilihan in pesanan:
                        pesanan[pilihan] += jumlah
                    else:
                        pesanan[pilihan] = jumlah
                    st.write(f"{pilihan} ditambahkan ke daftar pesanan.")
        elif jenis == 'minuman':
            for item in minuman.values():
                if item['name'] == pilihan:
                    if pilihan in pesanan:
                        pesanan[pilihan] += jumlah
                    else:
                        pesanan[pilihan] = jumlah
                    st.write(f"{pilihan} ditambahkan ke daftar pesanan.")
        else:
            st.write("Menu tidak valid. Silakan pilih menu yang tersedia")
