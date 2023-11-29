bio = dict(
    nama={"nm1": "Fadil Rahman Hakim", "nm2": "Hafidz Syadi Ismallah", "nm3": "Ferrossi Pratama", "nm4": "Adityo Dwi Saputro", "nm5": "Mas Febri Aditya"},
    panggilan={"pg1": "fadil", "pg2": "hafidz", "pg3": "ferosi", "pg4": "adit", "pg5": "febri"},
    tempat_lahir={"tpl1": "sanggau", "tpl2": "singkawang", "tpl3": "siantan", "tpl4": "serdam", "tpl5": "kuale"},
    tanggal_lahir={"tgl1": "25 september 2005", "tgl2": "26 september 2004", "tgl3": "27 september 2003", "tgl4": "28 september 2002", "tgl5": "29 september 2001"},
    jenis_kelamin={"jk1": "laki laki", "jk2": "laki laki", "jk3": "laki laki", "jk4": "laki laki", "jk5": "laki laki"},
    Agama={"agm1": "islam", "agm2": "islam", "agm3": "islam", "agm4": "islam", "agm5": "islam"},
    Alamat_rumah={"ar1": "pasiran", "ar2": "jalan tani", "ar3": "jalan mahmud", "ar4": "nilam permai", "ar5": "kuale dalam"},
    Nomor_Telepon={"nt1": "082253889636", "nt2": "082253879636", "nt3": "082233889636", "nt4": "086253889636", "nt5": "082253839636"},
    Alamat_email={"mail1": "fadilrahmanhakim@gmail.com", "mail2": "hafidz@gmail.com", "mail3": "rosi@gmail.com", "mail4": "adit@gmail.com", "mail5": "mas@gmail.com"},
    Hobi={"hb1": "berburu mutan kaki 8", "hb2": "nebang pohon", "hb3": "jelajahi gua", "hb4": "lawan mutan", "hb5": "nangkap ikan"},
    Cita_Cita={"ct1": "kapal laut", "ct2": "pns", "ct3": "balap", "ct4": "presiden", "ct5": "full stack"}
)


tampung = bio["nama"] 
tampung1 = bio["panggilan"]
tampung2 = bio["tempat_lahir"]
tampung3 = bio["tanggal_lahir"]
tampung4 = bio["jenis_kelamin"]
tampung5 = bio["Agama"]
tampung6 = bio["Alamat_rumah"]
tampung7 = bio["Nomor_Telepon"]
tampung8 = bio["Alamat_email"]
tampung9 = bio["Hobi"]
tampung10 = bio["Cita_Cita"]

for kunci, kunci1, kunci2, kunci3, kunci4, kunci5, kunci6, kunci7, kunci8, kunci9, kunci10 in zip(tampung, tampung1, tampung2, tampung3, tampung4, tampung5, tampung6, tampung7, tampung8, tampung9, tampung10):
    print(f" Nama\t\t: {tampung[kunci]}\n Panggilan\t: {tampung1[kunci1]}\n tempat_lahir\t: {tampung2[kunci2]}\n tanggal_lahir\t: {tampung3[kunci3]}\n jenis_kelamin\t: {tampung4[kunci4]}\n Agama\t\t: {tampung5[kunci5]}\n Alamat_rumah\t: {tampung6[kunci6]}\n Nomor_Telepon\t: {tampung7[kunci7]}\n Alamat_email\t: {tampung8[kunci8]}\n Hobi\t\t: {tampung9[kunci9]}\n Cita_Cita\t: {tampung10[kunci10]}\n {'='*40}")



