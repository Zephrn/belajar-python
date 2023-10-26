def balok():
    print("hitung ('1' luas) ('2'volume)")
    hasilj = int(input())
    if hasilj == 1:
        print("masukan panjang")
        pl = int(input())
        print("masukan lebar")
        lt = int(input())
        print("masukan tinggi")
        pt = int(input())
        luas = 2 * (pl + lt + pt)
        print("luas balok adalah = " + str(luas))
    else:
        if hasilj == 2:
            print("masukan panjang")
            p = int(input())
            print("lebar")
            l = int(input())
            print("tinggi")
            t = int(input())
            volume = p * l * t
            print("volume balok adalah = " + str(volume))

def bola():
    print("hitung ('1' luas) ('2'volume)")
    hasill = int(input())
    if hasill == 1:
        print("masukan r")
        r = float(input())
        luas = 4 * 3.14 * (r * r)
        print("luas dari bola adalah : " + str(luas))
    else:
        if hasill == 2:
            print("masukan r")
            r = float(input())
            volume = float(4) / 3 * 3.14 * (r * r * r)
            print("volume dari bola adalah : " + str(volume))

def kubus():
    print("hitung ('1' luas) ('2'volume)")
    hasilp = int(input())
    if hasilp == 1:
        print("masukan sisi")
        sisi = int(input())
        luas = 6 * (sisi * sisi)
        print("luas kubus adalah = " + str(luas))
    else:
        if hasilp == 2:
            print("masukan sisi")
            sisi = int(input())
            volume = sisi * sisi * sisi
            print("volume kubus adalah = " + str(volume))

def limassegiempat():
    print("hitung ('1' luas) ('2'volume)")
    hasil = int(input())
    if hasil == 1:
        print("masukan sisi")
        sisi = int(input())
        print("masukan luas sisi")
        luassisi = int(input())
        luas = sisi * sisi + 4 * luassisi
        print("hasil dari luas limas segiempat : " + str(luas))
    else:
        if hasil == 2:
            print("masukan sisi")
            sisi = int(input())
            print("masukan tinggi")
            tinggi = float(input())
            volume = float(1) / 3 * (sisi * sisi) * tinggi
            print("hasil dari volume limas segiempat : " + str(volume))

def selimutkerucut():
    print("hitung ('1' luas) ('2'luas permukaan ('3'volume))")
    hasilps = int(input())
    if hasilps == 1:
        print("masukan r")
        jari = float(input())
        luas = 3.14 * (jari * jari)
        print("luas dari selimut kerucut adalah = " + str(luas))
    else:
        if hasilps == 2:
            print("masukan r")
            jari = float(input())
            print("masukan garis")
            garis = float(input())
            luasalas = 3.14 * jari * (garis + jari)
            print("luas permukaan dari selimut kerucut adalah = " + str(luasalas))
        else:
            if hasilps == 3:
                print("masukan r")
                jari = float(input())
                print("masukan garis")
                garis = float(input())
                volume = 3.14 * jari * garis
                print("volume dari selimut kerucut adalah = " + str(volume))

def selimuttabung():
    print("hitung ('1' luas) ('2'luas alas) ('3' volume)")
    hasilkt = int(input())
    if hasilkt == 1:
        print("masukan jari")
        jari = float(input())
        print("masukan tinggi")
        tinggi = float(input())
        luas = 2 * 3.14 * jari * tinggi
        print("luas dari selimut tabung adalah = " + str(luas))
    else:
        if hasilkt == 2:
            print("masukan jari")
            jari = float(input())
            luasalas = 3.14 * (jari * jari)
            print("luas alas dari selimut tabung adalah = " + str(luasalas))
        else:
            if hasilkt == 3:
                print("masukan jari")
                jari = float(input())
                print("masukan tinggi")
                tinggi = float(input())
                volume = 3.14 * (jari * jari) * tinggi
                print("volume dari selimut tabung adalah = " + str(volume))

def main():
    x = True
    while x:
        print("perhitungan volume dan luas")
        print("masukan pilihan :")
        print("1. kubus")
        print("2. limas segi empat")
        print("3. balok")
        print("4. selimut kerucut")
        print("5. bola")
        print("6. selimut tabung")
        print("")
        pilihan = int(input())
        if pilihan == 1:
            print("perhitungan  kubus")
            kubus()
        elif pilihan == 2:
            print(" limas segiempat")
            limassegiempat()
        elif pilihan == 3:
            print("perhitungan  balok")
            balok()
        elif pilihan == 4:
            print("perhitungan  selimut kerucut")
            selimutkerucut()
        elif pilihan == 5:
            print("perhitungan bola")
            bola()
        elif pilihan == 6:
            print("perhitungan  selimut tabung")
            selimuttabung()
        else:
            print("input anda salah")

        print("Apakah anda ingin menghitung bangun datar yang lain? 'Ya' 'Tidak'")
        pilihanulang = input()
        if pilihanulang == "Ya":
            x = True
        elif pilihanulang == "Tidak":
            x = False
            print("terima kasih telah menggunakan program kami")
        elif pilihanulang != "Tidak":
            x = False
            print("input salah")

            

main()