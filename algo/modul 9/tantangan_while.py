from datetime import datetime, timedelta
waktu = datetime(2023,11,20,8,0)
nasabah = 1


while (nasabah <= 25):
    mulai = waktu + timedelta(minutes=(nasabah-1)*15)
    selesai = waktu + timedelta(minutes=(nasabah)*15)
    wkmulai = mulai.strftime("%H:%M WIB")
    wkselesai = selesai.strftime("%H:%M WIB")
    print(f"Anda antrian ke-{nasabah} \nwaktu mulai \t : {wkmulai} \nwaktu selesai \t : {wkselesai} \n")
    nasabah += 1
