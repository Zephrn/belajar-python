def belahKetupat():
    print("hitung ('1' luas) ('2'keliling)")
    hasilkt = int(input())
    if hasilkt == 1:
        luasKt()
    else:
        if hasilkt == 2:
            kelilingKt()

def jajargenjang():
    print("hitung ('1' luas) ('2'keliling)")
    hasilj = int(input())
    if hasilj == 1:
        jajarGenjangLuas()
    else:
        if hasilj == 2:
            jajarGenjangKeliling()

def jajarGenjangKeliling():
    print("masukan sisiA")
    sisiA = int(input())
    print("masukan sisiB")
    sisiB = int(input())
    keliling = 2 * (sisiA + sisiB)
    print("keliling dari jajar genjang adalah = " + str(keliling))

def jajarGenjangLuas():
    print("masukan panjang")
    alas = int(input())
    print("masukan lebar")
    tinggi = int(input())
    luas = alas * tinggi
    print("luas jajar genjang adalah = " + str(luas))

def kelilingKt():
    print("masukan sisi")
    sisi = int(input())
    keliling = 4 * sisi
    print("keliling dari ketupat adalah = " + str(keliling))

def kelilingL():
    print("masukan r")
    r = float(input())
    hasil = float(2 * 22) / 7 * r
    print(hasil)

def kelilingLayang():
    print("masukan sisi")
    sisi = int(input())
    keliling = 4 * sisi
    print("keliling dari layang-layang adalah = " + str(keliling))

def kelilingT():
    print("masukan A")
    a = int(input())
    print("masukan B")
    b = int(input())
    print("masukan C")
    c = int(input())
    print("masukan D")
    d = int(input())
    hasil = a + b + c + d
    print(hasil)

def layang():
    print("hitung ('1' luas) ('2'keliling)")
    hasill = int(input())
    if hasill == 1:
        luasLayang()
    else:
        if hasill == 2:
            kelilingLayang()

def lingkaran():
    print("hitung ('1' luas) ('2'keliling)")
    hasill = int(input())
    if hasill == 1:
        luasL()
    else:
        if hasill == 2:
            kelilingL()

def luasKt():
    print("masukan sisi")
    sisi = int(input())
    print("masukan diagonal1")
    diagonal1 = int(input())
    print("masukan diagonal2")
    diagonal2 = int(input())
    luas = float(diagonal1 * diagonal2) / sisi
    print("luas dari ketupat adalah = " + str(luas))

def luasL():
    print("masukan r")
    r = float(input())
    hasil = float(22) / 7 * (r * r)
    print(hasil)

def luasLayang():
    print("masukan sisia")
    sisia = int(input())
    print("masukan sisib")
    sisib = int(input())
    print("masukan diagonal1")
    diagonal1 = int(input())
    print("masukan diagonal2")
    diagonal2 = int(input())
    luas = float(diagonal1 * diagonal2) / 2
    print("luas dari layang-layang adalah = " + str(luas))

def luasT():
    print("masukan alasA")
    a = int(input())
    print("masukan alasB")
    b = int(input())
    print("masukan tinggi")
    t = int(input())
    hasil = float(1) / 2 * (a + b) * t
    print(hasil)

def persegi():
    print("hitung ('1' luas) ('2'keliling)")
    hasilps = int(input())
    if hasilps == 1:
        persegiLuas()
    else:
        if hasilps == 2:
            persegiKeliling()

def persegiKeliling():
    print("masukan sisi")
    sisi = int(input())
    keliling = 4 * sisi
    print("keliling dari persegi adalah = " + str(keliling))

def persegiLuas():
    print("masukan sisi")
    sisi = float(input())
    luas = sisi * sisi
    print("luas dari persegi adalah = " + str(luas))

def persegiPanjang():
    print("hitung ('1' luas) ('2'keliling)")
    hasilp = int(input())
    if hasilp == 1:
        persegiPanjangLuas()
    else:
        if hasilp == 2:
            persegiPanjangKeliling()

def persegiPanjangKeliling():
    print("masukan panjang")
    panjang = int(input())
    print("masukan lebar")
    lebar = int(input())
    keliling = 2 * (panjang + lebar)
    print("keliling dari persegi panjang adalah = " + str(keliling))

def persegiPanjangLuas():
    print("masukan panjang")
    panjang = int(input())
    print("masukan lebar")
    lebar = int(input())
    luas = panjang * lebar
    print("luas persegi panjang adalah = " + str(luas))

def segitiga():
    print("hitung ('1' luas) ('2'keliling)")
    hasilsg = int(input())
    if hasilsg == 1:
        segitigaLuas()
    else:
        if hasilsg == 2:
            segitigaKeliling()

def segitigaKeliling():
    print("masukan alas")
    alas = int(input())
    print("masukan tinggi")
    tinggi = int(input())
    keliling = float(1) / 2 * (alas * tinggi)
    print("keliling dari segitiga adalah = " + str(keliling))

def segitigaLuas():
    print("masukan sisi")
    sisi = int(input())
    luas = 3 * sisi
    print("keliling dari segitiga adalah = " + str(luas))

def trapesium():
    print("hitung ('1' luas) ('2'keliling)")
    hasil = int(input())
    if hasil == 1:
        luasT()
    else:
        if hasil == 2:
            kelilingT()

def main():
    x = True
    while x:
        print("masukan pilihan   (1)persegiPanjang)   (2)trapesium)  (3)jajargenjang)  (4)persegi)   (5)lingkaran (6)ketupat) (7)layang-layang) (8)segitiga))")
        pilihan = int(input())
        if pilihan == 1:
            print("perhitungan persegi panjang")
            persegiPanjang()
        elif pilihan == 2:
            print("perhitungan trapesium")
            trapesium()
        elif pilihan == 3:
            print("perhitungan jajar genjang")
            jajargenjang()
        elif pilihan == 4:
            print("perhitungan persegi")
            persegi()
        elif pilihan == 5:            
            print("perhitungan lingkaran")
            lingkaran()
        elif pilihan == 6:
            print("perhitungan ketupat")
            belahKetupat()
        elif pilihan == 7:
            print("perhitungan layang-layang")
            layang()
        elif pilihan == 8:
            print("perhitungan segitiga")
            segitiga()
        elif pilihan < 1 and pilihan > 8:
            print("input anda salah")
            
        print("Apakah anda ingin menghitung bangun datar yang lain? 'Ya' 'Tidak'")
        pilihanulang = input()
        if pilihanulang == "Tidak":
            x = False
            print("terima kasih telah menggunakan program kami")
        elif pilihanulang == "Ya":
            x = True

            

main()