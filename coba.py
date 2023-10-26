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

def kelilingL():
    print("masukan r")
    r = float(input())
    hasil = float(2 * 22) / 7 * r
    print(hasil)

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

def lingkaran():
    print("hitung ('1' luas) ('2'keliling)")
    hasill = int(input())
    if hasill == 1:
        luasL()
    else:
        if hasill == 2:
            kelilingL()

def luasL():
    print("masukan r")
    r = float(input())
    hasil = float(22) / 7 * (r * r)
    print(hasil)

def luasT():
    print("masukan alasA")
    a = int(input())
    print("masukan alasB")
    b = int(input())
    print("masukan tinggi")
    t = int(input())
    hasil = float(1) / 2 * (a + b) * t
    print(hasil)

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

def segilima():
    print("hitung ('1' luas) ('2'keliling)")
    hasils = int(input())
    if hasils == 1:
        segiLimaLuas()
    else:
        if hasils == 2:
            segiLimaKeliling()

def segiLimaKeliling():
    print("masukan sisi")
    sisi = int(input())
    keliling = 5 * sisi
    print("keliling dari segi lima adalah = " + str(keliling))

def segiLimaLuas():
    print("masukan sisi")
    sisi = float(input())
    luas = float(5) / 4 * (sisi * sisi) * (float(1376381920) / 1000000000)
    print("luas dari segi lima adalah = " + str(luas))

def trapesium():
    print("hitung ('1' luas) ('2'keliling)")
    hasil = int(input())
    if hasil == 1:
        luasT()
    else:
        if hasil == 2:
            kelilingT()

# Main
print("masukan pilihan   (1)persegiPanjang)   (2)trapesium)  (3)jajargenjang)  (4)segi lima)   (5)lingkaran')")
pilihan = int(input())
if pilihan == 1:
    print("perhitungan persegi panjang")
    persegiPanjang()
else:
    if pilihan == 2:
        print("perhitungan trapesium")
        trapesium()
    else:
        if pilihan == 3:
            print("perhitungan jajar genjang")
            jajargenjang()
        else:
            if pilihan == 4:
                print("perhitungan segilima")
                segilima()
            else:
                if pilihan == 5:
                    print("perhitungan lingkaran")
                    lingkaran()
